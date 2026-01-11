import { runQuery, getSchedaPath } from '../../utils/neo4j'

export default defineEventHandler(async (event) => {
  const id = getRouterParam(event, 'id')

  if (!id) {
    throw createError({ statusCode: 400, message: 'Missing node id' })
  }

  // Get node with all its relationships
  const results = await runQuery(`
    MATCH (n {id: $id})
    OPTIONAL MATCH (n)-[r]-(m)
    RETURN n, collect(DISTINCT {
      rel: r,
      node: m,
      direction: CASE WHEN startNode(r) = n THEN 'out' ELSE 'in' END
    }) as connections
  `, { id })

  if (results.length === 0) {
    throw createError({ statusCode: 404, message: 'Node not found' })
  }

  const { n: node, connections } = results[0]

  // Process edges and connected nodes
  const edges: any[] = []
  const connectedNodes: any[] = []
  const seenNodes = new Set<string>()

  for (const conn of connections) {
    if (!conn.rel || !conn.node) continue

    const connectedId = conn.node.id
    if (seenNodes.has(connectedId)) continue
    seenNodes.add(connectedId)

    // Add edge
    edges.push({
      id: `${node.id}-${conn.rel.type}-${connectedId}`,
      source: conn.direction === 'out' ? node.id : connectedId,
      target: conn.direction === 'out' ? connectedId : node.id,
      type: conn.rel.type,
      ...conn.rel
    })

    // Add connected node
    connectedNodes.push({
      ...conn.node,
      schedasPath: getSchedaPath(conn.node.labels, conn.node.id)
    })
  }

  return {
    node: {
      ...node,
      schedasPath: getSchedaPath(node.labels, node.id)
    },
    edges,
    connectedNodes
  }
})
