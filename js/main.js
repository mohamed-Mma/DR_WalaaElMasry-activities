document.addEventListener('DOMContentLoaded', () => {
  const intro = document.getElementById('intro-screen');
  const activities = document.getElementById('activities-screen');
  const links = document.getElementById('links-screen');

  function show(screen) {
    [intro, activities, links].forEach(s => s && s.classList.remove('active'));
    if (screen) screen.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  document.getElementById('start-btn')?.addEventListener('click', () => show(activities));
  document.getElementById('back-to-welcome')?.addEventListener('click', () => show(intro));
  document.getElementById('open-links')?.addEventListener('click', () => show(links));
  document.getElementById('links-back')?.addEventListener('click', () => show(activities));

  // Theme
  const toggle = document.getElementById('theme-toggle');
  toggle?.addEventListener('click', () => {
    const cur = document.documentElement.getAttribute('data-theme');
    const next = cur === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  // Filters
  const chips = document.querySelectorAll('.chip');
  const cards = document.querySelectorAll('.activity-card');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      chips.forEach(c => c.classList.remove('on'));
      chip.classList.add('on');
      const f = chip.dataset.f;
      cards.forEach(card => {
        card.style.display = (f === 'all' || card.dataset.cat === f) ? '' : 'none';
      });
    });
  });

  // Search
  document.getElementById('search-input')?.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();
    cards.forEach(card => {
      card.style.display = card.innerText.toLowerCase().includes(q) ? '' : 'none';
    });
  });
});
