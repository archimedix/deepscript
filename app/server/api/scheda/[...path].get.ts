import { readFile } from 'fs/promises'
import { existsSync } from 'fs'
import { join } from 'path'

export default defineEventHandler(async (event) => {
  const path = getRouterParam(event, 'path')

  if (!path) {
    throw createError({ statusCode: 400, message: 'Missing path' })
  }

  // Resolve path relative to project root (deepscript/docs/)
  const docsDir = join(process.cwd(), '..', 'docs')
  const filePath = join(docsDir, `${path}.md`)

  // Security: ensure path doesn't escape docs directory
  if (!filePath.startsWith(docsDir)) {
    throw createError({ statusCode: 403, message: 'Invalid path' })
  }

  if (!existsSync(filePath)) {
    return {
      exists: false,
      content: null,
      internalLinks: []
    }
  }

  try {
    const content = await readFile(filePath, 'utf-8')

    // Extract internal links: [[id]] or [text](../type/id.md)
    const internalLinks: { id: string; type?: string }[] = []

    // Match [[entity-id]]
    const wikiLinks = content.matchAll(/\[\[([a-z0-9-]+)\]\]/g)
    for (const match of wikiLinks) {
      internalLinks.push({ id: match[1] })
    }

    // Match [text](../type/id.md) - relative links to other docs
    const mdLinks = content.matchAll(/\[([^\]]+)\]\(\.\.\/([^/]+)\/([^)]+)\.md\)/g)
    for (const match of mdLinks) {
      internalLinks.push({ id: match[3], type: match[2] })
    }

    // Deduplicate
    const uniqueLinks = Array.from(
      new Map(internalLinks.map(l => [l.id, l])).values()
    )

    return {
      exists: true,
      content,
      internalLinks: uniqueLinks
    }
  } catch (error) {
    throw createError({ statusCode: 500, message: 'Error reading file' })
  }
})
