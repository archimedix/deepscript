<template>
  <div class="graph-canvas" ref="containerRef">
    <ClientOnly>
      <div ref="cyRef" class="cytoscape-container"></div>
      <template #fallback>
        <div class="graph-loading">
          <div class="loading-spinner"></div>
          <p>Initializing graph...</p>
        </div>
      </template>
    </ClientOnly>

    <!-- Top toolbar with filters -->
    <div class="graph-toolbar" v-if="nodes.length > 0">
      <!-- Node type filters -->
      <div class="filter-group">
        <span class="filter-label">Nodes</span>
        <button
          v-for="nt in nodeTypes"
          :key="nt.key"
          class="filter-chip"
          :class="{ active: activeNodeTypes.has(nt.key), [nt.class]: true }"
          @click="toggleNodeType(nt.key)"
          :title="nt.label"
        >
          {{ nt.short }}
        </button>
      </div>

      <!-- Edge type filters -->
      <div class="filter-group">
        <span class="filter-label">Edges</span>
        <button
          v-for="et in edgeTypes"
          :key="et.key"
          class="filter-chip filter-edge"
          :class="{ active: activeEdgeTypes.has(et.key) }"
          @click="toggleEdgeType(et.key)"
          :title="et.label"
        >
          {{ et.short }}
        </button>
      </div>

      <!-- Layout selector -->
      <div class="filter-group">
        <span class="filter-label">Layout</span>
        <select v-model="currentLayout" @change="runLayout" class="layout-select">
          <option value="cose-bilkent">Force (COSE)</option>
          <option value="concentric">Concentric</option>
          <option value="circle">Circle</option>
          <option value="grid">Grid</option>
          <option value="breadthfirst">Tree</option>
        </select>
      </div>

      <!-- Clear button -->
      <button class="clear-btn" @click="$emit('clear')" title="Clear graph">
        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
        Clear
      </button>
    </div>

    <!-- Controls -->
    <div class="graph-controls">
      <button class="control-btn" @click="zoomIn" title="Zoom in">
        <svg viewBox="0 0 20 20" fill="currentColor"><path d="M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z"/></svg>
      </button>
      <button class="control-btn" @click="zoomOut" title="Zoom out">
        <svg viewBox="0 0 20 20" fill="currentColor"><path d="M5 10a1 1 0 011-1h8a1 1 0 110 2H6a1 1 0 01-1-1z"/></svg>
      </button>
      <button class="control-btn" @click="fitGraph" title="Fit to view">
        <svg viewBox="0 0 20 20" fill="currentColor"><path d="M3 4a1 1 0 011-1h4a1 1 0 010 2H6.414l2.293 2.293a1 1 0 01-1.414 1.414L5 6.414V8a1 1 0 01-2 0V4zm9 1a1 1 0 010-2h4a1 1 0 011 1v4a1 1 0 01-2 0V6.414l-2.293 2.293a1 1 0 11-1.414-1.414L13.586 5H12zm-9 7a1 1 0 012 0v1.586l2.293-2.293a1 1 0 011.414 1.414L6.414 15H8a1 1 0 010 2H4a1 1 0 01-1-1v-4zm13 0a1 1 0 012 0v4a1 1 0 01-1 1h-4a1 1 0 010-2h1.586l-2.293-2.293a1 1 0 011.414-1.414L15 13.586V12z"/></svg>
      </button>
      <div class="control-separator"></div>
      <button class="control-btn" @click="runLayout" title="Re-layout">
        <svg viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clip-rule="evenodd"/></svg>
      </button>
    </div>

    <!-- Empty state -->
    <div v-if="nodes.length === 0" class="graph-empty">
      <div class="empty-content">
        <svg class="empty-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1">
          <circle cx="8" cy="8" r="3"/>
          <circle cx="16" cy="16" r="3"/>
          <circle cx="16" cy="8" r="3"/>
          <path d="M11 8h2M13 13.5l-2.5-2.5M8 11v2"/>
        </svg>
        <h3>No nodes loaded</h3>
        <p>Search for an entity to start exploring the network</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import type { Core, NodeSingular, EventObject } from 'cytoscape'

interface GraphNode {
  id: string
  labels: string[]
  name: string
  [key: string]: any
}

interface GraphEdge {
  id: string
  source: string
  target: string
  type: string
  [key: string]: any
}

const props = defineProps<{
  nodes: GraphNode[]
  edges: GraphEdge[]
  selectedId?: string | null
}>()

const emit = defineEmits<{
  nodeClick: [nodeId: string]
  nodeExpand: [nodeId: string]
  clear: []
}>()

const containerRef = ref<HTMLElement>()
const cyRef = ref<HTMLElement>()
let cy: Core | null = null

// Filter definitions
const nodeTypes = [
  { key: 'Person', short: 'P', label: 'Person', class: 'type-person' },
  { key: 'Organization', short: 'O', label: 'Organization', class: 'type-organization' },
  { key: 'Family', short: 'F', label: 'Family', class: 'type-family' },
  { key: 'Event', short: 'E', label: 'Event', class: 'type-event' }
]

const edgeTypes = [
  { key: 'AFFILIATED_WITH', short: 'AFF', label: 'Affiliated With' },
  { key: 'STAKE_IN', short: 'STK', label: 'Stake In' },
  { key: 'MEMBER_OF', short: 'MEM', label: 'Member Of' },
  { key: 'RELATED_TO', short: 'REL', label: 'Related To' },
  { key: 'PARTICIPATED_IN', short: 'PAR', label: 'Participated In' },
  { key: 'INVOLVED_IN', short: 'INV', label: 'Involved In' }
]

// Active filters (all active by default)
const activeNodeTypes = ref(new Set(nodeTypes.map(t => t.key)))
const activeEdgeTypes = ref(new Set(edgeTypes.map(t => t.key)))
const currentLayout = ref('cose-bilkent')

function toggleNodeType(key: string) {
  if (activeNodeTypes.value.has(key)) {
    activeNodeTypes.value.delete(key)
  } else {
    activeNodeTypes.value.add(key)
  }
  activeNodeTypes.value = new Set(activeNodeTypes.value) // trigger reactivity
  applyFilters()
}

function toggleEdgeType(key: string) {
  if (activeEdgeTypes.value.has(key)) {
    activeEdgeTypes.value.delete(key)
  } else {
    activeEdgeTypes.value.add(key)
  }
  activeEdgeTypes.value = new Set(activeEdgeTypes.value)
  applyFilters()
}

function applyFilters() {
  if (!cy) return

  // Show/hide nodes based on type
  cy.nodes().forEach(node => {
    const nodeType = node.data('nodeType')
    if (activeNodeTypes.value.has(nodeType)) {
      node.style('display', 'element')
    } else {
      node.style('display', 'none')
    }
  })

  // Show/hide edges based on type
  cy.edges().forEach(edge => {
    const edgeType = edge.data('edgeType')
    const sourceVisible = edge.source().style('display') === 'element'
    const targetVisible = edge.target().style('display') === 'element'

    if (activeEdgeTypes.value.has(edgeType) && sourceVisible && targetVisible) {
      edge.style('display', 'element')
    } else {
      edge.style('display', 'none')
    }
  })
}

// Node colors by type
const nodeColors: Record<string, string> = {
  Person: '#3B82F6',
  Organization: '#10B981',
  Family: '#8B5CF6',
  Event: '#F59E0B'
}

// Edge colors by type
const edgeColors: Record<string, string> = {
  AFFILIATED_WITH: '#6b7280',
  STAKE_IN: '#10B981',
  MEMBER_OF: '#8B5CF6',
  RELATED_TO: '#3B82F6',
  PARTICIPATED_IN: '#F59E0B',
  INVOLVED_IN: '#F59E0B'
}

function getNodeColor(labels: string[]): string {
  for (const label of labels) {
    if (nodeColors[label]) return nodeColors[label]
  }
  return nodeColors.Organization
}

function getNodeShape(labels: string[]): string {
  if (labels.includes('Person')) return 'ellipse'
  if (labels.includes('Family')) return 'diamond'
  if (labels.includes('Event')) return 'octagon'
  return 'round-rectangle'
}

async function initCytoscape() {
  if (!cyRef.value || typeof window === 'undefined') return

  const cytoscape = (await import('cytoscape')).default
  const coseBilkent = (await import('cytoscape-cose-bilkent')).default

  cytoscape.use(coseBilkent)

  cy = cytoscape({
    container: cyRef.value,
    style: [
      {
        selector: 'node',
        style: {
          'background-color': 'data(color)',
          'label': 'data(label)',
          'color': '#f0f0f2',
          'text-valign': 'bottom',
          'text-margin-y': 8,
          'font-size': 11,
          'font-family': 'Outfit, system-ui, sans-serif',
          'text-outline-color': '#0a0a0c',
          'text-outline-width': 2,
          'width': 40,
          'height': 40,
          'shape': 'data(shape)',
          'border-width': 2,
          'border-color': 'data(color)',
          'border-opacity': 0.3
        }
      },
      {
        selector: 'node:selected',
        style: {
          'border-width': 3,
          'border-color': '#ffffff',
          'border-opacity': 1
        }
      },
      {
        selector: 'edge',
        style: {
          'width': 1.5,
          'line-color': 'data(color)',
          'target-arrow-color': 'data(color)',
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier',
          'opacity': 0.6,
          'label': 'data(label)',
          'font-size': 9,
          'font-family': 'JetBrains Mono, monospace',
          'text-rotation': 'autorotate',
          'text-margin-y': -8,
          'color': '#606068',
          'text-outline-color': '#0a0a0c',
          'text-outline-width': 1
        }
      },
      {
        selector: 'edge:selected',
        style: {
          'opacity': 1,
          'width': 2
        }
      }
    ],
    layout: { name: 'preset' },
    wheelSensitivity: 0.3,
    minZoom: 0.2,
    maxZoom: 3
  })

  // Events
  cy.on('tap', 'node', (evt: EventObject) => {
    const node = evt.target as NodeSingular
    emit('nodeClick', node.id())
  })

  cy.on('dbltap', 'node', (evt: EventObject) => {
    const node = evt.target as NodeSingular
    emit('nodeExpand', node.id())
  })

  // Initial data - render any data that arrived before cy was ready
  if (props.nodes.length > 0) {
    updateGraph()
  }
}

function getNodeType(labels: string[]): string {
  if (labels.includes('Person')) return 'Person'
  if (labels.includes('Family')) return 'Family'
  if (labels.includes('Event')) return 'Event'
  return 'Organization'
}

function updateGraph() {
  if (!cy) return

  // Convert nodes
  const cyNodes = props.nodes.map(node => ({
    data: {
      id: node.id,
      label: node.name || node.id,
      color: getNodeColor(node.labels),
      shape: getNodeShape(node.labels),
      nodeType: getNodeType(node.labels)
    }
  }))

  // Convert edges
  const cyEdges = props.edges.map(edge => ({
    data: {
      id: edge.id,
      source: edge.source,
      target: edge.target,
      label: edge.role || edge.type.toLowerCase().replace(/_/g, ' '),
      color: edgeColors[edge.type] || '#6b7280',
      edgeType: edge.type
    }
  }))

  // Update graph
  cy.elements().remove()
  cy.add([...cyNodes, ...cyEdges])

  // Apply current filters
  applyFilters()

  // Run layout
  runLayout()
}

function runLayout() {
  if (!cy || cy.nodes().length === 0) return

  const layoutConfigs: Record<string, any> = {
    'cose-bilkent': {
      name: 'cose-bilkent',
      animate: true,
      animationDuration: 500,
      nodeRepulsion: 8000,
      idealEdgeLength: 100,
      edgeElasticity: 0.1,
      nestingFactor: 0.1,
      gravity: 0.25,
      numIter: 2500,
      tile: true,
      fit: true,
      padding: 50
    },
    concentric: {
      name: 'concentric',
      animate: true,
      animationDuration: 500,
      fit: true,
      padding: 50,
      concentric: (node: any) => node.degree(),
      levelWidth: () => 2
    },
    circle: {
      name: 'circle',
      animate: true,
      animationDuration: 500,
      fit: true,
      padding: 50
    },
    grid: {
      name: 'grid',
      animate: true,
      animationDuration: 500,
      fit: true,
      padding: 50,
      rows: Math.ceil(Math.sqrt(cy.nodes().length))
    },
    breadthfirst: {
      name: 'breadthfirst',
      animate: true,
      animationDuration: 500,
      fit: true,
      padding: 50,
      directed: true,
      spacingFactor: 1.5
    }
  }

  const config = layoutConfigs[currentLayout.value] || layoutConfigs['cose-bilkent']
  cy.layout(config).run()
}

function zoomIn() {
  if (!cy) return
  cy.zoom(cy.zoom() * 1.3)
}

function zoomOut() {
  if (!cy) return
  cy.zoom(cy.zoom() * 0.7)
}

function fitGraph() {
  if (!cy) return
  cy.fit(undefined, 50)
}

function centerOnNode(nodeId: string) {
  if (!cy) return
  const node = cy.getElementById(nodeId)
  if (node.length > 0) {
    cy.animate({
      center: { eles: node },
      zoom: 1.5,
      duration: 300
    })
    node.select()
  }
}

// Expose methods
defineExpose({ centerOnNode })

// Watch for data changes
watch([() => props.nodes, () => props.edges], () => {
  if (cy) {
    updateGraph()
  }
}, { deep: true })

// Also watch nodes length specifically to catch initial load
watch(() => props.nodes.length, () => {
  if (cy && props.nodes.length > 0) {
    nextTick(() => updateGraph())
  }
})

// Watch for selection changes
watch(() => props.selectedId, (newId) => {
  if (!cy || !newId) return
  cy.nodes().unselect()
  const node = cy.getElementById(newId)
  if (node.length > 0) {
    node.select()
  }
})

// Initialize when cyRef becomes available (handles ClientOnly)
watch(cyRef, (newRef) => {
  if (newRef && !cy) {
    initCytoscape()
  }
}, { immediate: true })

// Cleanup
onUnmounted(() => {
  if (cy) {
    cy.destroy()
    cy = null
  }
})
</script>

<style scoped>
.graph-canvas {
  position: relative;
  flex: 1;
  overflow: hidden;
  background:
    radial-gradient(circle at 50% 50%, rgba(59, 130, 246, 0.02) 0%, transparent 70%),
    linear-gradient(rgba(255,255,255,0.01) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.01) 1px, transparent 1px);
  background-size: 100% 100%, 40px 40px, 40px 40px;
}

.cytoscape-container {
  position: absolute;
  inset: 0;
}

/* Toolbar */
.graph-toolbar {
  position: absolute;
  top: 12px;
  left: 12px;
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 8px 12px;
  z-index: 10;
}

.filter-group {
  display: flex;
  align-items: center;
  gap: 6px;
}

.filter-label {
  font-size: 10px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-right: 4px;
}

.filter-chip {
  padding: 4px 8px;
  font-family: var(--font-mono);
  font-size: 10px;
  font-weight: 500;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background: var(--bg-tertiary);
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
  opacity: 0.5;
}

.filter-chip:hover {
  opacity: 0.8;
}

.filter-chip.active {
  opacity: 1;
  border-color: currentColor;
}

.filter-chip.type-person.active {
  color: var(--color-person);
  background: rgba(59, 130, 246, 0.1);
}

.filter-chip.type-organization.active {
  color: var(--color-organization);
  background: rgba(16, 185, 129, 0.1);
}

.filter-chip.type-family.active {
  color: var(--color-family);
  background: rgba(139, 92, 246, 0.1);
}

.filter-chip.type-event.active {
  color: var(--color-event);
  background: rgba(245, 158, 11, 0.1);
}

.filter-chip.filter-edge.active {
  color: var(--text-primary);
  background: var(--bg-hover);
}

.layout-select {
  padding: 4px 8px;
  font-family: var(--font-body);
  font-size: 11px;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background: var(--bg-tertiary);
  color: var(--text-primary);
  cursor: pointer;
  outline: none;
}

.layout-select:focus {
  border-color: var(--color-person);
}

.clear-btn {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 10px;
  font-family: var(--font-body);
  font-size: 11px;
  border: 1px solid var(--border-color);
  border-radius: 4px;
  background: var(--bg-tertiary);
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
}

.clear-btn:hover {
  background: rgba(239, 68, 68, 0.1);
  border-color: #ef4444;
  color: #ef4444;
}

.clear-btn svg {
  width: 14px;
  height: 14px;
}

.graph-controls {
  position: absolute;
  top: 12px;
  right: 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  border-radius: 8px;
  padding: 4px;
}

.control-btn {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  border-radius: 6px;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s;
}

.control-btn:hover {
  background: var(--bg-hover);
  color: var(--text-primary);
}

.control-btn svg {
  width: 16px;
  height: 16px;
}

.control-separator {
  height: 1px;
  background: var(--border-color);
  margin: 4px 0;
}

.graph-empty {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  pointer-events: none;
}

.empty-content {
  text-align: center;
  color: var(--text-muted);
}

.empty-icon {
  width: 64px;
  height: 64px;
  margin: 0 auto 16px;
  opacity: 0.3;
}

.empty-content h3 {
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 400;
  margin: 0 0 8px 0;
  color: var(--text-secondary);
}

.empty-content p {
  font-size: 13px;
  margin: 0;
}

.graph-loading {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  color: var(--text-muted);
}

.loading-spinner {
  width: 24px;
  height: 24px;
  border: 2px solid var(--border-color);
  border-top-color: var(--color-person);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
