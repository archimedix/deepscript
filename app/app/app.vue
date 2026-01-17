<template>
  <div class="app-container">
    <!-- Header -->
    <header class="app-header">
      <div class="logo">
        <span class="logo-mark">DS</span>
        <span class="logo-text">DeepScript</span>
      </div>
      <div class="header-stats" v-if="stats">
        <span class="stat">{{ stats.nodes }} nodes</span>
        <span class="stat-sep">/</span>
        <span class="stat">{{ stats.edges }} edges</span>
      </div>
    </header>

    <!-- Main content -->
    <main class="app-main">
      <!-- Search Panel -->
      <aside class="panel panel-search" :class="{ collapsed: searchCollapsed }">
        <button class="panel-toggle" @click="searchCollapsed = !searchCollapsed">
          <span v-if="searchCollapsed">&#9654;</span>
          <span v-else>&#9664;</span>
        </button>
        <div class="panel-content" v-show="!searchCollapsed">
          <SearchPanel
            @select="handleNodeSelect"
            :selected-id="selectedNodeId"
          />
        </div>
      </aside>

      <!-- Graph Canvas -->
      <section class="panel panel-graph">
        <GraphCanvas
          ref="graphRef"
          :nodes="graphNodes"
          :edges="graphEdges"
          :selected-id="selectedNodeId"
          @node-click="handleNodeClick"
          @node-expand="handleNodeExpand"
          @clear="handleClearGraph"
        />
        <div class="graph-status">
          <span>Nodes: {{ graphNodes.length }}</span>
          <span class="status-sep">|</span>
          <span>Edges: {{ graphEdges.length }}</span>
          <span v-if="selectedNodeId" class="status-sep">|</span>
          <span v-if="selectedNodeId" class="status-selected">{{ selectedNodeId }}</span>
        </div>
      </section>

      <!-- Scheda Panel -->
      <aside class="panel panel-scheda" :class="{ collapsed: schedaCollapsed }">
        <button class="panel-toggle panel-toggle-right" @click="schedaCollapsed = !schedaCollapsed">
          <span v-if="schedaCollapsed">&#9664;</span>
          <span v-else>&#9654;</span>
        </button>
        <div class="panel-content" v-show="!schedaCollapsed">
          <SchedaPanel
            :scheda-path="selectedSchedaPath"
            @link-click="handleLinkClick"
          />
        </div>
      </aside>
    </main>
  </div>
</template>

<script setup lang="ts">
interface GraphNode {
  id: string
  labels: string[]
  name: string
  schedasPath?: string | null
  [key: string]: any
}

interface GraphEdge {
  id: string
  source: string
  target: string
  type: string
  [key: string]: any
}

const graphRef = ref()
const searchCollapsed = ref(false)
const schedaCollapsed = ref(false)

const graphNodes = ref<GraphNode[]>([])
const graphEdges = ref<GraphEdge[]>([])
const selectedNodeId = ref<string | null>(null)
const selectedSchedaPath = ref<string | null>(null)

const stats = ref<{ nodes: number; edges: number } | null>(null)

// Load initial stats
onMounted(async () => {
  // Simple count from loaded graph
  updateStats()
})

function updateStats() {
  stats.value = {
    nodes: graphNodes.value.length,
    edges: graphEdges.value.length
  }
}

async function handleNodeSelect(node: GraphNode) {
  await loadNodeWithConnections(node.id)
}

async function handleNodeClick(nodeId: string) {
  selectedNodeId.value = nodeId
  const node = graphNodes.value.find(n => n.id === nodeId)
  if (node?.schedasPath) {
    selectedSchedaPath.value = node.schedasPath
  }
}

async function handleNodeExpand(nodeId: string) {
  await loadNodeWithConnections(nodeId, true)
}

async function loadNodeWithConnections(nodeId: string, expand = false) {
  try {
    const data = await $fetch(`/api/node/${nodeId}`)

    if (!expand) {
      // Replace graph
      graphNodes.value = [data.node, ...data.connectedNodes]
      graphEdges.value = data.edges
    } else {
      // Merge into existing graph
      const existingIds = new Set(graphNodes.value.map(n => n.id))

      if (!existingIds.has(data.node.id)) {
        graphNodes.value.push(data.node)
      }

      for (const node of data.connectedNodes) {
        if (!existingIds.has(node.id)) {
          graphNodes.value.push(node)
        }
      }

      const existingEdgeIds = new Set(graphEdges.value.map(e => e.id))
      for (const edge of data.edges) {
        if (!existingEdgeIds.has(edge.id)) {
          graphEdges.value.push(edge)
        }
      }
    }

    selectedNodeId.value = nodeId
    selectedSchedaPath.value = data.node.schedasPath
    updateStats()
  } catch (error) {
    console.error('Error loading node:', error)
  }
}

async function handleLinkClick(entityId: string) {
  // Check if node already in graph
  const existing = graphNodes.value.find(n => n.id === entityId)
  if (existing) {
    selectedNodeId.value = entityId
    selectedSchedaPath.value = existing.schedasPath || null
    graphRef.value?.centerOnNode(entityId)
  } else {
    // Load and expand
    await loadNodeWithConnections(entityId, true)
  }
}

function handleClearGraph() {
  graphNodes.value = []
  graphEdges.value = []
  selectedNodeId.value = null
  selectedSchedaPath.value = null
  updateStats()
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&family=Outfit:wght@300;400;500;600&display=swap');

:root {
  --bg-primary: #0a0a0c;
  --bg-secondary: #111114;
  --bg-tertiary: #18181c;
  --bg-hover: #1f1f24;

  --text-primary: #f0f0f2;
  --text-secondary: #a0a0a8;
  --text-muted: #606068;

  --border-color: #2a2a30;
  --border-accent: #3a3a42;

  /* Main types */
  --color-person: #3B82F6;
  --color-organization: #10B981;
  --color-family: #8B5CF6;
  --color-event: #F59E0B;

  /* Organization sublabels - Financial */
  --color-bank: #059669;
  --color-centralbank: #047857;
  --color-assetmanager: #0D9488;
  --color-privateequity: #0891B2;
  --color-hedgefund: #0E7490;
  --color-swf: #14B8A6;

  /* Organization sublabels - Government */
  --color-government: #DC2626;
  --color-agency: #EA580C;
  --color-party: #E11D48;

  /* Organization sublabels - Knowledge */
  --color-foundation: #7C3AED;
  --color-thinktank: #6366F1;
  --color-university: #8B5CF6;

  /* Organization sublabels - Business */
  --color-company: #10B981;
  --color-defense: #64748B;
  --color-pharma: #EC4899;
  --color-automaker: #78716C;
  --color-sportsclub: #22C55E;

  /* Organization sublabels - Other */
  --color-media: #F472B6;
  --color-forum: #FBBF24;

  --font-display: 'Instrument Serif', Georgia, serif;
  --font-body: 'Outfit', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  --header-height: 52px;
  --panel-search-width: 280px;
  --panel-scheda-width: 380px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%;
  background: var(--bg-primary);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 14px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.app-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background:
    radial-gradient(ellipse at 20% 0%, rgba(59, 130, 246, 0.03) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 100%, rgba(139, 92, 246, 0.03) 0%, transparent 50%),
    var(--bg-primary);
}

/* Header */
.app-header {
  height: var(--header-height);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-secondary);
  flex-shrink: 0;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-mark {
  font-family: var(--font-display);
  font-size: 20px;
  font-style: italic;
  color: var(--color-person);
  background: linear-gradient(135deg, var(--color-person), var(--color-family));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.logo-text {
  font-family: var(--font-display);
  font-size: 18px;
  letter-spacing: -0.02em;
}

.header-stats {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-muted);
}

.stat-sep {
  margin: 0 8px;
  opacity: 0.4;
}

/* Main layout */
.app-main {
  flex: 1;
  display: flex;
  overflow: hidden;
}

/* Panels */
.panel {
  position: relative;
  display: flex;
  flex-direction: column;
  border-right: 1px solid var(--border-color);
}

.panel:last-child {
  border-right: none;
  border-left: 1px solid var(--border-color);
}

.panel-search {
  width: var(--panel-search-width);
  background: var(--bg-secondary);
  transition: width 0.2s ease;
}

.panel-search.collapsed {
  width: 40px;
}

.panel-scheda {
  width: var(--panel-scheda-width);
  background: var(--bg-secondary);
  transition: width 0.2s ease;
}

.panel-scheda.collapsed {
  width: 40px;
}

.panel-graph {
  flex: 1;
  display: flex;
  flex-direction: column;
  background: var(--bg-primary);
  border: none;
}

.panel-content {
  flex: 1;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.panel-toggle {
  position: absolute;
  top: 50%;
  right: -12px;
  transform: translateY(-50%);
  width: 24px;
  height: 48px;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: 0 6px 6px 0;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 10px;
  z-index: 10;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.panel-toggle:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.panel-toggle-right {
  right: auto;
  left: -12px;
  border-radius: 6px 0 0 6px;
}

/* Graph status bar */
.graph-status {
  padding: 8px 16px;
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
  background: var(--bg-secondary);
  border-top: 1px solid var(--border-color);
}

.status-sep {
  margin: 0 12px;
  opacity: 0.3;
}

.status-selected {
  color: var(--color-person);
}
</style>
