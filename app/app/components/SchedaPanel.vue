<template>
  <div class="scheda-panel">
    <div v-if="!schedaPath" class="scheda-empty">
      <div class="empty-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M19 3H5a2 2 0 00-2 2v14a2 2 0 002 2h14a2 2 0 002-2V5a2 2 0 00-2-2z"/>
          <path d="M12 8v8M8 12h8"/>
        </svg>
      </div>
      <p>Select a node to view its profile</p>
    </div>

    <div v-else-if="loading" class="scheda-loading">
      <div class="loading-spinner"></div>
      <p>Loading...</p>
    </div>

    <div v-else-if="!scheda?.exists" class="scheda-missing">
      <div class="missing-icon">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M9 12h6M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
        </svg>
      </div>
      <p>No profile available</p>
      <span class="missing-path">{{ schedaPath }}</span>
    </div>

    <div v-else class="scheda-content">
      <div class="scheda-header">
        <span class="scheda-path">{{ schedaPath }}</span>
      </div>
      <div
        class="markdown-body"
        v-html="renderedContent"
        @click="handleContentClick"
      ></div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { marked } from 'marked'

interface Scheda {
  exists: boolean
  content: string | null
  internalLinks: { id: string; type?: string }[]
}

const props = defineProps<{
  schedaPath?: string | null
}>()

const emit = defineEmits<{
  linkClick: [entityId: string]
}>()

const scheda = ref<Scheda | null>(null)
const loading = ref(false)

const renderedContent = computed(() => {
  if (!scheda.value?.content) return ''

  let content = scheda.value.content

  // Convert [[entity-id]] wiki links to clickable spans
  content = content.replace(
    /\[\[([a-z0-9-]+)\]\]/g,
    '<span class="internal-link" data-entity="$1">$1</span>'
  )

  // Convert relative markdown links to clickable spans
  content = content.replace(
    /\[([^\]]+)\]\(\.\.\/([^/]+)\/([^)]+)\.md\)/g,
    '<span class="internal-link" data-entity="$3">$1</span>'
  )

  return marked(content)
})

watch(() => props.schedaPath, async (newPath) => {
  if (!newPath) {
    scheda.value = null
    return
  }

  loading.value = true
  try {
    scheda.value = await $fetch(`/api/scheda/${newPath}`)
  } catch (error) {
    console.error('Error loading scheda:', error)
    scheda.value = { exists: false, content: null, internalLinks: [] }
  } finally {
    loading.value = false
  }
}, { immediate: true })

function handleContentClick(event: MouseEvent) {
  const target = event.target as HTMLElement
  if (target.classList.contains('internal-link')) {
    const entityId = target.dataset.entity
    if (entityId) {
      emit('linkClick', entityId)
    }
  }
}
</script>

<style scoped>
.scheda-panel {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.scheda-empty,
.scheda-loading,
.scheda-missing {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  color: var(--text-muted);
  padding: 24px;
  text-align: center;
}

.empty-icon,
.missing-icon {
  width: 48px;
  height: 48px;
  color: var(--text-muted);
  opacity: 0.5;
}

.empty-icon svg,
.missing-icon svg {
  width: 100%;
  height: 100%;
}

.missing-path {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
  opacity: 0.6;
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

.scheda-content {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
}

.scheda-header {
  padding: 10px 16px;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-tertiary);
}

.scheda-path {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--text-muted);
}

.markdown-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px 16px;
  font-size: 13px;
  line-height: 1.7;
}

/* Markdown styles */
.markdown-body :deep(h1) {
  font-family: var(--font-display);
  font-size: 24px;
  font-weight: 400;
  margin: 0 0 16px 0;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-color);
  letter-spacing: -0.02em;
}

.markdown-body :deep(h2) {
  font-family: var(--font-body);
  font-size: 14px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-secondary);
  margin: 24px 0 12px 0;
}

.markdown-body :deep(h3) {
  font-size: 14px;
  font-weight: 500;
  margin: 16px 0 8px 0;
}

.markdown-body :deep(p) {
  margin: 0 0 12px 0;
}

.markdown-body :deep(ul),
.markdown-body :deep(ol) {
  margin: 0 0 12px 0;
  padding-left: 20px;
}

.markdown-body :deep(li) {
  margin: 4px 0;
}

.markdown-body :deep(strong) {
  color: var(--text-primary);
  font-weight: 500;
}

.markdown-body :deep(a) {
  color: var(--color-person);
  text-decoration: none;
}

.markdown-body :deep(a:hover) {
  text-decoration: underline;
}

.markdown-body :deep(code) {
  font-family: var(--font-mono);
  font-size: 12px;
  padding: 2px 6px;
  background: var(--bg-tertiary);
  border-radius: 3px;
}

.markdown-body :deep(pre) {
  background: var(--bg-tertiary);
  padding: 12px;
  border-radius: 6px;
  overflow-x: auto;
  margin: 0 0 12px 0;
}

.markdown-body :deep(pre code) {
  padding: 0;
  background: none;
}

.markdown-body :deep(blockquote) {
  margin: 0 0 12px 0;
  padding: 8px 16px;
  border-left: 3px solid var(--color-person);
  background: var(--bg-tertiary);
  color: var(--text-secondary);
}

.markdown-body :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 0 0 12px 0;
  font-size: 12px;
}

.markdown-body :deep(th),
.markdown-body :deep(td) {
  padding: 8px;
  border: 1px solid var(--border-color);
  text-align: left;
}

.markdown-body :deep(th) {
  background: var(--bg-tertiary);
  font-weight: 500;
}

.markdown-body :deep(hr) {
  border: none;
  border-top: 1px solid var(--border-color);
  margin: 20px 0;
}

/* Internal links */
.markdown-body :deep(.internal-link) {
  color: var(--color-organization);
  cursor: pointer;
  border-bottom: 1px dotted var(--color-organization);
  transition: all 0.15s;
}

.markdown-body :deep(.internal-link:hover) {
  color: var(--color-person);
  border-bottom-color: var(--color-person);
}
</style>
