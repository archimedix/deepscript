import { runQuery, getSchedaPath } from '../utils/neo4j'

export default defineEventHandler(async (event) => {
  const query = getQuery(event)
  const q = (query.q as string || '').trim()

  if (!q || q.length < 2) {
    return { results: [], total: 0 }
  }

  const searchPattern = `(?i).*${q}.*`

  const results = await runQuery(`
    MATCH (n)
    WHERE n.name =~ $pattern OR n.id =~ $pattern
    RETURN n
    ORDER BY
      CASE WHEN n.name =~ '(?i)^' + $q + '.*' THEN 0 ELSE 1 END,
      n.name
    LIMIT 50
  `, { pattern: searchPattern, q })

  return {
    results: results.map(r => ({
      ...r.n,
      schedasPath: getSchedaPath(r.n.labels, r.n.id)
    })),
    total: results.length
  }
})
