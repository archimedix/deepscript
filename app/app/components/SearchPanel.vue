<template>
  <div class="search-panel">
    <div class="search-input-wrapper">
      <svg class="search-icon" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
      </svg>
      <input
        ref="inputRef"
        v-model="query"
        type="text"
        class="search-input"
        placeholder="Search entities..."
        @input="debouncedSearch"
        @keydown.down.prevent="navigateResults(1)"
        @keydown.up.prevent="navigateResults(-1)"
        @keydown.enter.prevent="selectHighlighted"
      />
      <span v-if="loading" class="search-loading">...</span>
      <button v-else-if="query" class="search-clear" @click="clearSearch">
        <svg viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
      </button>
    </div>

    <div class="search-results" v-if="results.length > 0">
      <div
        v-for="(result, index) in results"
        :key="result.id"
        class="result-item"
        :class="{
          'result-selected': result.id === selectedId,
          'result-highlighted': index === highlightedIndex
        }"
        @click="selectResult(result)"
        @mouseenter="highlightedIndex = index"
      >
        <span class="result-type" :class="getTypeClass(result.labels)">
          {{ getTypeLabel(result.labels) }}
        </span>
        <span class="result-name">{{ result.name || result.id }}</span>
        <span v-if="result.nationality" class="result-meta">{{ result.nationality }}</span>
      </div>
    </div>

    <div v-else-if="query && !loading && searched" class="search-empty">
      No results for "{{ query }}"
    </div>

    <div v-else class="search-hint">
      <p>Type to search people, organizations, families, and events.</p>
      <div class="hint-legend">
        <span class="legend-item"><span class="legend-dot type-person"></span>Person</span>
        <span class="legend-item"><span class="legend-dot type-organization"></span>Organization</span>
        <span class="legend-item"><span class="legend-dot type-family"></span>Family</span>
        <span class="legend-item"><span class="legend-dot type-event"></span>Event</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface SearchResult {
  id: string
  labels: string[]
  name?: string
  nationality?: string
  schedasPath?: string | null
}

const props = defineProps<{
  selectedId?: string | null
}>()

const emit = defineEmits<{
  select: [result: SearchResult]
}>()

const inputRef = ref<HTMLInputElement>()
const query = ref('')
const results = ref<SearchResult[]>([])
const loading = ref(false)
const searched = ref(false)
const highlightedIndex = ref(-1)

let searchTimeout: ReturnType<typeof setTimeout> | null = null

function debouncedSearch() {
  if (searchTimeout) clearTimeout(searchTimeout)
  searched.value = false
  highlightedIndex.value = -1

  if (query.value.length < 2) {
    results.value = []
    return
  }

  loading.value = true
  searchTimeout = setTimeout(async () => {
    try {
      const data = await $fetch('/api/search', {
        query: { q: query.value }
      })
      results.value = data.results
      searched.value = true
    } catch (error) {
      console.error('Search error:', error)
      results.value = []
    } finally {
      loading.value = false
    }
  }, 300)
}

function clearSearch() {
  query.value = ''
  results.value = []
  searched.value = false
  highlightedIndex.value = -1
  inputRef.value?.focus()
}

function selectResult(result: SearchResult) {
  emit('select', result)
}

function navigateResults(direction: number) {
  if (results.value.length === 0) return

  highlightedIndex.value += direction
  if (highlightedIndex.value < 0) highlightedIndex.value = results.value.length - 1
  if (highlightedIndex.value >= results.value.length) highlightedIndex.value = 0
}

function selectHighlighted() {
  if (highlightedIndex.value >= 0 && highlightedIndex.value < results.value.length) {
    selectResult(results.value[highlightedIndex.value])
  }
}

function getTypeLabel(labels: string[]): string {
  if (labels.includes('Person')) return 'P'
  if (labels.includes('Family')) return 'F'
  if (labels.includes('Event')) return 'E'
  // Organization sublabels
  const sublabel = labels.find(l => l !== 'Organization')
  if (sublabel) return sublabel.substring(0, 3).toUpperCase()
  return 'ORG'
}

function getTypeClass(labels: string[]): string {
  if (labels.includes('Person')) return 'type-person'
  if (labels.includes('Family')) return 'type-family'
  if (labels.includes('Event')) return 'type-event'
  return 'type-organization'
}

// Focus search on mount
onMounted(() => {
  inputRef.value?.focus()
})
</script>

<style scoped>
.search-panel {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.search-input-wrapper {
  position: relative;
  padding: 12px;
  border-bottom: 1px solid var(--border-color);
}

.search-icon {
  position: absolute;
  left: 22px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: var(--text-muted);
  pointer-events: none;
}

.search-input {
  width: 100%;
  padding: 10px 32px 10px 36px;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: 6px;
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 13px;
  outline: none;
  transition: all 0.15s ease;
}

.search-input:focus {
  border-color: var(--color-person);
  box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1);
}

.search-input::placeholder {
  color: var(--text-muted);
}

.search-loading {
  position: absolute;
  right: 22px;
  top: 50%;
  transform: translateY(-50%);
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--text-muted);
  animation: pulse 1s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.4; }
}

.search-clear {
  position: absolute;
  right: 18px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  padding: 0;
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.15s;
}

.search-clear:hover {
  color: var(--text-primary);
}

.search-clear svg {
  width: 14px;
  height: 14px;
}

.search-results {
  flex: 1;
  overflow-y: auto;
  padding: 8px 0;
}

.result-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  cursor: pointer;
  transition: background 0.1s;
}

.result-item:hover,
.result-highlighted {
  background: var(--bg-hover);
}

.result-selected {
  background: var(--bg-tertiary);
  border-left: 2px solid var(--color-person);
}

.result-type {
  flex-shrink: 0;
  width: 32px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-mono);
  font-size: 9px;
  font-weight: 500;
  border-radius: 3px;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}

.type-person {
  background: rgba(59, 130, 246, 0.15);
  color: var(--color-person);
}

.type-organization {
  background: rgba(16, 185, 129, 0.15);
  color: var(--color-organization);
}

.type-family {
  background: rgba(139, 92, 246, 0.15);
  color: var(--color-family);
}

.type-event {
  background: rgba(245, 158, 11, 0.15);
  color: var(--color-event);
}

.result-name {
  flex: 1;
  font-size: 13px;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.result-meta {
  flex-shrink: 0;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--text-muted);
  text-transform: uppercase;
}

.search-empty {
  padding: 24px 16px;
  text-align: center;
  color: var(--text-muted);
  font-size: 13px;
}

.search-hint {
  padding: 20px 16px;
  color: var(--text-muted);
  font-size: 12px;
}

.search-hint p {
  margin-bottom: 16px;
  line-height: 1.6;
}

.hint-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 11px;
}

.legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.legend-dot.type-person { background: var(--color-person); }
.legend-dot.type-organization { background: var(--color-organization); }
.legend-dot.type-family { background: var(--color-family); }
.legend-dot.type-event { background: var(--color-event); }
</style>
