/**
 * Main Client Scripts for Mehdi's Digital Legacy
 */

(function () {
  'use strict';

  // 0. Strip temporary cache-buster query param after legacy redirect recovery
  if (window.location.search.includes('_fresh=')) {
    const url = new URL(window.location.href);
    url.searchParams.delete('_fresh');
    window.history.replaceState({}, '', url.pathname + url.search + url.hash);
  }

  // 1. Theme Management
  const themeToggleBtn = document.getElementById('theme-toggle');
  const savedTheme = localStorage.getItem('mehdi_archive_theme') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');

  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('mehdi_archive_theme', next);
      updateThemeIcon(next);
    });
  }

  function updateThemeIcon(theme) {
    if (!themeToggleBtn) return;
    themeToggleBtn.innerHTML = theme === 'dark' ? '☀️ Light' : '🌙 Dark';
    themeToggleBtn.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
  }

  // 2. Responsive Mobile Navigation Menu
  const headerContainer = document.querySelector('.header-container');
  const siteNav = document.querySelector('.site-nav');

  if (headerContainer && siteNav) {
    if (!siteNav.id) {
      siteNav.id = 'site-nav';
    }

    let menuToggleBtn = document.getElementById('mobile-menu-toggle');
    if (!menuToggleBtn) {
      menuToggleBtn = document.createElement('button');
      menuToggleBtn.type = 'button';
      menuToggleBtn.id = 'mobile-menu-toggle';
      menuToggleBtn.className = 'mobile-menu-toggle';
      menuToggleBtn.setAttribute('aria-label', 'Toggle navigation menu');
      menuToggleBtn.setAttribute('aria-expanded', 'false');
      menuToggleBtn.setAttribute('aria-controls', siteNav.id);
      menuToggleBtn.innerHTML =
        '<span class="hamburger-bar"></span>' +
        '<span class="hamburger-bar"></span>' +
        '<span class="hamburger-bar"></span>';
      headerContainer.insertBefore(menuToggleBtn, siteNav);
    }

    const setMenuOpen = (isOpen) => {
      siteNav.classList.toggle('is-open', isOpen);
      menuToggleBtn.setAttribute('aria-expanded', String(isOpen));
    };

    menuToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isCurrentlyOpen = siteNav.classList.contains('is-open');
      setMenuOpen(!isCurrentlyOpen);
    });

    siteNav.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', () => setMenuOpen(false));
    });

    document.addEventListener('click', (e) => {
      if (siteNav.classList.contains('is-open') && !headerContainer.contains(e.target)) {
        setMenuOpen(false);
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && siteNav.classList.contains('is-open')) {
        setMenuOpen(false);
        menuToggleBtn.focus();
      }
    });

    window.addEventListener('resize', () => {
      if (window.innerWidth > 768 && siteNav.classList.contains('is-open')) {
        setMenuOpen(false);
      }
    });
  }

  // 3. Global Archive Helpers
  window.ArchiveUtils = {
    formatDate: function (dateStr) {
      if (!dateStr) return '';
      try {
        const d = new Date(dateStr);
        return d.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'short',
          day: 'numeric'
        });
      } catch (e) {
        return dateStr.substring(0, 10);
      }
    },

    escapeHtml: function (str) {
      if (!str) return '';
      const div = document.createElement('div');
      div.textContent = str;
      return div.innerHTML;
    },

    getQueryParam: function (param) {
      const urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    },

    resolveAssetPath: function (relPath) {
      if (!relPath) return '';
      if (relPath.startsWith('http://') || relPath.startsWith('https://')) return relPath;
      const clean = relPath.replace(/^\/+/, '');
      if (window.location.pathname.includes('/website/')) {
        return '../' + clean;
      }
      return clean;
    },

    fetchAsset: async function (relPath) {
      const primary = window.ArchiveUtils.resolveAssetPath(relPath);
      let resp = await fetch(primary);
      if (!resp.ok && !primary.startsWith('../')) {
        resp = await fetch('../' + relPath.replace(/^\/+/, ''));
      }
      return resp;
    },

    renderArticleCard: function (article) {
      const isRoyal = article.source === 'royaltechbd';
      const badgeClass = isRoyal ? 'badge-royal' : 'badge-shamokal';
      const sourceName = article.source_name || (isRoyal ? 'Royal Technologies' : 'সমকাল দর্পণ');
      const dateFormatted = window.ArchiveUtils.formatDate(article.published_at);
      const excerpt = window.ArchiveUtils.escapeHtml(article.excerpt || '');
      const title = window.ArchiveUtils.escapeHtml(article.title || 'Untitled');
      
      const tagsHtml = (article.categories || []).slice(0, 3).map(cat => 
        `<span class="tag-pill">${window.ArchiveUtils.escapeHtml(cat)}</span>`
      ).join('');

      return `
        <article class="article-card">
          <div class="article-card-meta">
            <span class="source-badge ${badgeClass}">${sourceName}</span>
            <time datetime="${article.published_at}">${dateFormatted}</time>
            <span>•</span>
            <span>${article.language === 'bn' ? 'বাংলা' : 'English'}</span>
          </div>
          <h3 class="article-card-title">
            <a href="article.html?id=${article.archive_id}">${title}</a>
          </h3>
          ${excerpt ? `<p class="article-card-excerpt">${excerpt}</p>` : ''}
          ${tagsHtml ? `<div class="article-card-tags">${tagsHtml}</div>` : ''}
        </article>
      `;
    }
  };
})();
