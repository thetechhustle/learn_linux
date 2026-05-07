document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a[href^="http"]').forEach((link) => {
    if (!link.hostname || link.hostname === window.location.hostname) return;
    link.rel = 'noopener noreferrer';
  });
});
