// Build metadata is added by scripts/build_site.py when the CI job succeeds.
fetch('./build-info.json', { cache: 'no-store' })
  .then(response => {
    if (!response.ok) throw new Error('Build info unavailable');
    return response.json();
  })
  .then(data => {
    document.getElementById('build-sha').textContent = String(data.commit).slice(0, 7);
  })
  .catch(() => {
    document.getElementById('build-sha').textContent = 'Local preview';
  });
