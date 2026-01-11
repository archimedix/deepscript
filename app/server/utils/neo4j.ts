import neo4j, { Driver, Session } from 'neo4j-driver'

let driver: Driver | null = null

export function getDriver(): Driver {
  if (!driver) {
    const config = useRuntimeConfig()
    driver = neo4j.driver(
      config.neo4j.uri,
      neo4j.auth.basic(config.neo4j.user, config.neo4j.password)
    )
  }
  return driver
}

export function getNeo4jSession(): Session {
  return getDriver().session()
}

export async function runQuery<T = any>(
  query: string,
  params: Record<string, any> = {}
): Promise<T[]> {
  const session = getNeo4jSession()
  try {
    const result = await session.run(query, params)
    return result.records.map(record => {
      const obj: any = {}
      record.keys.forEach(key => {
        obj[key] = toNative(record.get(key))
      })
      return obj
    })
  } finally {
    await session.close()
  }
}

// Convert Neo4j types to native JS
function toNative(value: any): any {
  if (value === null || value === undefined) return value
  if (neo4j.isInt(value)) return value.toNumber()
  if (Array.isArray(value)) return value.map(toNative)
  if (typeof value === 'object') {
    // Node
    if (value.labels && value.properties) {
      return {
        id: toNative(value.properties.id),
        labels: value.labels,
        ...Object.fromEntries(
          Object.entries(value.properties).map(([k, v]) => [k, toNative(v)])
        )
      }
    }
    // Relationship
    if (value.type && value.properties) {
      return {
        type: value.type,
        ...Object.fromEntries(
          Object.entries(value.properties).map(([k, v]) => [k, toNative(v)])
        )
      }
    }
    // Plain object
    return Object.fromEntries(
      Object.entries(value).map(([k, v]) => [k, toNative(v)])
    )
  }
  return value
}

// Docs path mapping from schema.yaml
const docsPathMapping: Record<string, string> = {
  Person: 'persons',
  Family: 'family',
  Event: 'events',
  Forum: 'forum',
  Bank: 'bank',
  CentralBank: 'central-bank',
  AssetManager: 'asset-manager',
  PrivateEquity: 'private-equity',
  HedgeFund: 'hedge-fund',
  SWF: 'swf',
  Government: 'government',
  Party: 'party',
  Foundation: 'foundation',
  ThinkTank: 'think-tank',
  Company: 'company',
  University: 'university',
  Agency: 'agency',
  Media: 'media',
  Defense: 'defense',
  Pharma: 'pharma',
  SportsClub: 'sports-club',
  Automaker: 'automaker'
}

export function getSchedaPath(labels: string[], id: string): string | null {
  // Find the most specific label (sublabel > main label)
  for (const label of labels) {
    if (label !== 'Organization' && docsPathMapping[label]) {
      return `${docsPathMapping[label]}/${id}`
    }
  }
  // Fallback to main label
  for (const label of labels) {
    if (docsPathMapping[label]) {
      return `${docsPathMapping[label]}/${id}`
    }
  }
  return null
}
