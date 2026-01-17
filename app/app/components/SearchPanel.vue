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
        <span v-if="result.nationality" class="result-flag" :title="result.nationality">{{ countryToFlag(result.nationality) }}</span>
      </div>
    </div>

    <div v-else-if="query && !loading && searched" class="search-empty">
      No results for "{{ query }}"
    </div>

    <div v-else class="search-hint">
      <p>Type to search people, organizations, families, and events.</p>

      <div class="legend-section">
        <div class="legend-title">Main Types</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-person"></span>Person</span>
          <span class="legend-item"><span class="legend-dot type-family"></span>Family</span>
          <span class="legend-item"><span class="legend-dot type-event"></span>Event</span>
        </div>
      </div>

      <div class="legend-section">
        <div class="legend-title">Financial</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-bank"></span>Bank</span>
          <span class="legend-item"><span class="legend-dot type-centralbank"></span>Central Bank</span>
          <span class="legend-item"><span class="legend-dot type-assetmanager"></span>Asset Mgr</span>
          <span class="legend-item"><span class="legend-dot type-privateequity"></span>Private Eq</span>
          <span class="legend-item"><span class="legend-dot type-hedgefund"></span>Hedge Fund</span>
          <span class="legend-item"><span class="legend-dot type-swf"></span>SWF</span>
        </div>
      </div>

      <div class="legend-section">
        <div class="legend-title">Government</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-government"></span>Government</span>
          <span class="legend-item"><span class="legend-dot type-agency"></span>Agency</span>
          <span class="legend-item"><span class="legend-dot type-party"></span>Party</span>
        </div>
      </div>

      <div class="legend-section">
        <div class="legend-title">Knowledge</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-foundation"></span>Foundation</span>
          <span class="legend-item"><span class="legend-dot type-thinktank"></span>Think Tank</span>
          <span class="legend-item"><span class="legend-dot type-university"></span>University</span>
        </div>
      </div>

      <div class="legend-section">
        <div class="legend-title">Business</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-company"></span>Company</span>
          <span class="legend-item"><span class="legend-dot type-defense"></span>Defense</span>
          <span class="legend-item"><span class="legend-dot type-pharma"></span>Pharma</span>
          <span class="legend-item"><span class="legend-dot type-automaker"></span>Automaker</span>
          <span class="legend-item"><span class="legend-dot type-sportsclub"></span>Sports Club</span>
        </div>
      </div>

      <div class="legend-section">
        <div class="legend-title">Other</div>
        <div class="hint-legend">
          <span class="legend-item"><span class="legend-dot type-media"></span>Media</span>
          <span class="legend-item"><span class="legend-dot type-forum"></span>Forum</span>
        </div>
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

// ISO alpha-3 to alpha-2 mapping
const iso3to2: Record<string, string> = {
  AFG: 'AF', ARE: 'AE', ARG: 'AR', AUS: 'AU', AUT: 'AT', BEL: 'BE', BGD: 'BD',
  BGR: 'BG', BHR: 'BH', BOL: 'BO', BRA: 'BR', CAN: 'CA', CHE: 'CH', CHN: 'CN',
  COD: 'CD', CRI: 'CR', CYP: 'CY', CZE: 'CZ', DEU: 'DE', DNK: 'DK', EGY: 'EG',
  ESP: 'ES', EST: 'EE', ETH: 'ET', FIN: 'FI', FRA: 'FR', GBR: 'GB', GEO: 'GE',
  GRC: 'GR', GTM: 'GT', HKG: 'HK', HRV: 'HR', HUN: 'HU', IDN: 'ID', IND: 'IN',
  IRL: 'IE', IRN: 'IR', IRQ: 'IQ', ISR: 'IL', ITA: 'IT', JOR: 'JO', JPN: 'JP',
  KEN: 'KE', KOR: 'KR', LBN: 'LB', LKA: 'LK', LTU: 'LT', LUX: 'LU', MDA: 'MD',
  MEX: 'MX', MLT: 'MT', MNE: 'ME', MYS: 'MY', NGA: 'NG', NLD: 'NL', NOR: 'NO',
  NZL: 'NZ', PAK: 'PK', PHL: 'PH', POL: 'PL', PRT: 'PT', PSE: 'PS', QAT: 'QA',
  ROU: 'RO', RUS: 'RU', SAU: 'SA', SGP: 'SG', SRB: 'RS', SVN: 'SI', SWE: 'SE',
  SYR: 'SY', THA: 'TH', TUR: 'TR', TWN: 'TW', UAE: 'AE', UKR: 'UA', USA: 'US',
  XKX: 'XK', ZAF: 'ZA', ZWE: 'ZW'
}

// Convert country code to flag emoji
function countryToFlag(code: string): string {
  if (!code) return ''
  // Handle dual nationality (e.g., "USA-ITA") - take first
  const primary = code.split('-')[0]
  // Convert alpha-3 to alpha-2 if needed
  let alpha2 = primary.length === 3 ? iso3to2[primary] : primary.toUpperCase()
  // Handle UK -> GB
  if (alpha2 === 'UK') alpha2 = 'GB'
  if (!alpha2 || alpha2.length !== 2) return ''
  const codePoints = alpha2.split('').map(char => 127397 + char.charCodeAt(0))
  return String.fromCodePoint(...codePoints)
}

// Sublabel display config
const sublabelConfig: Record<string, { short: string; class: string }> = {
  // Financial
  Bank: { short: 'BNK', class: 'type-bank' },
  CentralBank: { short: 'CB', class: 'type-centralbank' },
  AssetManager: { short: 'AM', class: 'type-assetmanager' },
  PrivateEquity: { short: 'PE', class: 'type-privateequity' },
  HedgeFund: { short: 'HF', class: 'type-hedgefund' },
  SWF: { short: 'SWF', class: 'type-swf' },
  // Government
  Government: { short: 'GOV', class: 'type-government' },
  Agency: { short: 'AGY', class: 'type-agency' },
  Party: { short: 'PTY', class: 'type-party' },
  // Knowledge
  Foundation: { short: 'FND', class: 'type-foundation' },
  ThinkTank: { short: 'TT', class: 'type-thinktank' },
  University: { short: 'UNI', class: 'type-university' },
  // Business
  Company: { short: 'CO', class: 'type-company' },
  Defense: { short: 'DEF', class: 'type-defense' },
  Pharma: { short: 'PHA', class: 'type-pharma' },
  Automaker: { short: 'CAR', class: 'type-automaker' },
  SportsClub: { short: 'SPT', class: 'type-sportsclub' },
  // Other
  Media: { short: 'MED', class: 'type-media' },
  Forum: { short: 'FRM', class: 'type-forum' }
}

function getTypeLabel(labels: string[]): string {
  if (labels.includes('Person')) return 'P'
  if (labels.includes('Family')) return 'F'
  if (labels.includes('Event')) return 'E'
  // Organization sublabels
  for (const label of labels) {
    if (sublabelConfig[label]) return sublabelConfig[label].short
  }
  return 'ORG'
}

function getTypeClass(labels: string[]): string {
  if (labels.includes('Person')) return 'type-person'
  if (labels.includes('Family')) return 'type-family'
  if (labels.includes('Event')) return 'type-event'
  // Organization sublabels
  for (const label of labels) {
    if (sublabelConfig[label]) return sublabelConfig[label].class
  }
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

/* Main types */
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

/* Financial sublabels */
.type-bank {
  background: rgba(5, 150, 105, 0.15);
  color: var(--color-bank);
}

.type-centralbank {
  background: rgba(4, 120, 87, 0.15);
  color: var(--color-centralbank);
}

.type-assetmanager {
  background: rgba(13, 148, 136, 0.15);
  color: var(--color-assetmanager);
}

.type-privateequity {
  background: rgba(8, 145, 178, 0.15);
  color: var(--color-privateequity);
}

.type-hedgefund {
  background: rgba(14, 116, 144, 0.15);
  color: var(--color-hedgefund);
}

.type-swf {
  background: rgba(20, 184, 166, 0.15);
  color: var(--color-swf);
}

/* Government sublabels */
.type-government {
  background: rgba(220, 38, 38, 0.15);
  color: var(--color-government);
}

.type-agency {
  background: rgba(234, 88, 12, 0.15);
  color: var(--color-agency);
}

.type-party {
  background: rgba(225, 29, 72, 0.15);
  color: var(--color-party);
}

/* Knowledge sublabels */
.type-foundation {
  background: rgba(124, 58, 237, 0.15);
  color: var(--color-foundation);
}

.type-thinktank {
  background: rgba(99, 102, 241, 0.15);
  color: var(--color-thinktank);
}

.type-university {
  background: rgba(139, 92, 246, 0.15);
  color: var(--color-university);
}

/* Business sublabels */
.type-company {
  background: rgba(16, 185, 129, 0.15);
  color: var(--color-company);
}

.type-defense {
  background: rgba(100, 116, 139, 0.15);
  color: var(--color-defense);
}

.type-pharma {
  background: rgba(236, 72, 153, 0.15);
  color: var(--color-pharma);
}

.type-automaker {
  background: rgba(120, 113, 108, 0.15);
  color: var(--color-automaker);
}

.type-sportsclub {
  background: rgba(34, 197, 94, 0.15);
  color: var(--color-sportsclub);
}

/* Other sublabels */
.type-media {
  background: rgba(244, 114, 182, 0.15);
  color: var(--color-media);
}

.type-forum {
  background: rgba(251, 191, 36, 0.15);
  color: var(--color-forum);
}

.result-name {
  flex: 1;
  font-size: 13px;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.result-flag {
  flex-shrink: 0;
  font-size: 14px;
  line-height: 1;
}

.search-empty {
  padding: 24px 16px;
  text-align: center;
  color: var(--text-muted);
  font-size: 13px;
}

.search-hint {
  padding: 16px;
  color: var(--text-muted);
  font-size: 12px;
  overflow-y: auto;
}

.search-hint > p {
  margin-bottom: 16px;
  line-height: 1.6;
}

.legend-section {
  margin-bottom: 12px;
}

.legend-title {
  font-size: 9px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 6px;
  opacity: 0.7;
}

.hint-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 12px;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 10px;
}

.legend-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  flex-shrink: 0;
}

/* Main types */
.legend-dot.type-person { background: var(--color-person); }
.legend-dot.type-organization { background: var(--color-organization); }
.legend-dot.type-family { background: var(--color-family); }
.legend-dot.type-event { background: var(--color-event); }

/* Financial */
.legend-dot.type-bank { background: var(--color-bank); }
.legend-dot.type-centralbank { background: var(--color-centralbank); }
.legend-dot.type-assetmanager { background: var(--color-assetmanager); }
.legend-dot.type-privateequity { background: var(--color-privateequity); }
.legend-dot.type-hedgefund { background: var(--color-hedgefund); }
.legend-dot.type-swf { background: var(--color-swf); }

/* Government */
.legend-dot.type-government { background: var(--color-government); }
.legend-dot.type-agency { background: var(--color-agency); }
.legend-dot.type-party { background: var(--color-party); }

/* Knowledge */
.legend-dot.type-foundation { background: var(--color-foundation); }
.legend-dot.type-thinktank { background: var(--color-thinktank); }
.legend-dot.type-university { background: var(--color-university); }

/* Business */
.legend-dot.type-company { background: var(--color-company); }
.legend-dot.type-defense { background: var(--color-defense); }
.legend-dot.type-pharma { background: var(--color-pharma); }
.legend-dot.type-automaker { background: var(--color-automaker); }
.legend-dot.type-sportsclub { background: var(--color-sportsclub); }

/* Other */
.legend-dot.type-media { background: var(--color-media); }
.legend-dot.type-forum { background: var(--color-forum); }
</style>
