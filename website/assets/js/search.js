/**
 * Client-Side Full-Text Search Engine for Mehdi's Digital Legacy
 * Supports both Bengali (বাংলা) and English queries with filtering & highlights.
 */

(function () {
  'use strict';

  let searchIndex = [];
  let currentFilter = {
    source: 'all',
    language: 'all',
    query: ''
  };

  const searchInput = document.getElementById('search-input');
  const resultsContainer = document.getElementById('search-results');
  const resultsCountElem = document.getElementById('results-count');
  const filterBtns = document.querySelectorAll('.filter-btn');

  // Load search index
  async function initSearch() {
    try {
      const resp = await fetch('data/search-index.json');
      if (!resp.ok) throw new Error('Search index not found');
      searchIndex = await resp.json();
      
      // Check for query in URL param ?q=
      const initialQuery = window.ArchiveUtils.getQueryParam('q');
      const initialSource = window.ArchiveUtils.getQueryParam('source');
      
      if (initialSource) {
        currentFilter.source = initialSource;
        updateActiveFilterUI('source', initialSource);
      }
      
      if (initialQuery && searchInput) {
        searchInput.value = initialQuery;
        currentFilter.query = initialQuery;
        executeSearch();
      } else if (resultsContainer) {
        renderRecentOrInitial();
      }
    } catch (err) {
      console.error('Failed to load search index:', err);
      if (resultsContainer) {
        resultsContainer.innerHTML = '<p class="error-msg">Search index is currently initializing or unavailable.</p>';
      }
    }
  }

  function updateActiveFilterUI(type, value) {
    filterBtns.forEach(btn => {
      if (btn.dataset[type]) {
        btn.classList.toggle('active', btn.dataset[type] === value);
      }
    });
  }

  function normalizeText(str) {
    if (!str) return '';
    return str.normalize('NFC').toLowerCase().trim();
  }

  function highlightMatches(text, queryWords) {
    if (!text || queryWords.length === 0) return window.ArchiveUtils.escapeHtml(text);
    let escaped = window.ArchiveUtils.escapeHtml(text);
    queryWords.forEach(word => {
      if (word.length >= 2) {
        // Safe regex replace avoiding HTML tag corruption
        const regex = new RegExp(`(${word.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&')})`, 'gi');
        escaped = escaped.replace(regex, '<mark>$1</mark>');
      }
    });
    return escaped;
  }

  function executeSearch() {
    if (!resultsContainer) return;

    const rawQuery = (searchInput ? searchInput.value : '').trim();
    currentFilter.query = rawQuery;

    const normalizedQuery = normalizeText(rawQuery);
    const queryWords = normalizedQuery.split(/\s+/).filter(w => w.length > 0);

    let filtered = searchIndex;

    // Filter by source
    if (currentFilter.source !== 'all') {
      filtered = filtered.filter(item => item.src === currentFilter.source);
    }

    // Filter by language
    if (currentFilter.language !== 'all') {
      filtered = filtered.filter(item => item.lang === currentFilter.language);
    }

    // If query words present, rank and match
    if (queryWords.length > 0) {
      filtered = filtered.map(item => {
        let score = 0;
        const titleNorm = normalizeText(item.t);
        const textNorm = item.txt || '';
        
        queryWords.forEach(word => {
          if (titleNorm.includes(word)) score += 10;
          if (textNorm.includes(word)) score += 2;
          if ((item.c || []).some(cat => normalizeText(cat).includes(word))) score += 5;
          if ((item.tg || []).some(t => normalizeText(t).includes(word))) score += 4;
        });

        return { item, score };
      })
      .filter(entry => entry.score > 0)
      .sort((a, b) => b.score - a.score)
      .map(entry => entry.item);
    }

    renderResults(filtered, queryWords);
  }

  function renderRecentOrInitial() {
    if (!resultsContainer) return;
    const initialList = searchIndex.slice(0, 20);
    renderResults(initialList, []);
    if (resultsCountElem) {
      resultsCountElem.textContent = `Showing latest ${initialList.length} articles across all sources`;
    }
  }

  function renderResults(items, queryWords) {
    if (resultsCountElem) {
      if (currentFilter.query) {
        resultsCountElem.textContent = `Found ${items.length} ${items.length === 1 ? 'article' : 'articles'} matching "${currentFilter.query}"`;
      } else {
        resultsCountElem.textContent = `Browsing ${items.length} articles`;
      }
    }

    if (items.length === 0) {
      resultsContainer.innerHTML = `
        <div style="text-align: center; padding: 40px 20px; color: var(--text-muted);">
          <h3>No articles found</h3>
          <p style="margin-top: 8px;">Try refining your search terms in English or Bengali, or clear filters.</p>
        </div>
      `;
      return;
    }

    const html = items.map(item => {
      const isRoyal = item.src === 'royaltechbd';
      const badgeClass = isRoyal ? 'badge-royal' : 'badge-shamokal';
      const titleHighlighted = highlightMatches(item.t, queryWords);
      const excerptHighlighted = highlightMatches(item.ex || '', queryWords);
      const dateFormatted = window.ArchiveUtils.formatDate(item.dt);

      const tagsHtml = (item.c || []).slice(0, 3).map(cat => 
        `<span class="tag-pill">${window.ArchiveUtils.escapeHtml(cat)}</span>`
      ).join('');

      return `
        <article class="article-card">
          <div class="article-card-meta">
            <span class="source-badge ${badgeClass}">${item.src_n}</span>
            <time>${dateFormatted}</time>
            <span>•</span>
            <span>${item.lang === 'bn' ? 'বাংলা' : 'English'}</span>
          </div>
          <h3 class="article-card-title">
            <a href="article.html?id=${item.id}">${titleHighlighted}</a>
          </h3>
          ${item.ex ? `<p class="article-card-excerpt">${excerptHighlighted}</p>` : ''}
          ${tagsHtml ? `<div class="article-card-tags">${tagsHtml}</div>` : ''}
        </article>
      `;
    }).join('');

    resultsContainer.innerHTML = `<div class="articles-list">${html}</div>`;
  }

  // Event Listeners
  if (searchInput) {
    let debounceTimer;
    searchInput.addEventListener('input', () => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(executeSearch, 150);
    });
  }

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const src = btn.dataset.source;
      const lang = btn.dataset.lang;

      if (src) {
        currentFilter.source = src;
        filterBtns.forEach(b => { if (b.dataset.source) b.classList.remove('active'); });
        btn.classList.add('active');
      }

      if (lang) {
        currentFilter.language = lang;
        filterBtns.forEach(b => { if (b.dataset.lang) b.classList.remove('active'); });
        btn.classList.add('active');
      }

      executeSearch();
    });
  });

  // Init on DOM ready
  document.addEventListener('DOMContentLoaded', initSearch);
})();
