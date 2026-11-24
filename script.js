(() => {
  const root = document.documentElement;
  const langBtn = document.querySelector('#langBtn');
  const themeBtn = document.querySelector('#themeBtn');
  const menuBtn = document.querySelector('#menuBtn');
  const nav = document.querySelector('#site-nav');
  const get = (key) => { try { return localStorage.getItem(key); } catch (_) { return null; } };
  const save = (key, value) => { try { localStorage.setItem(key, value); } catch (_) {} };
  function language(lang) {
    const l = lang === 'hr' ? 'hr' : 'en';
    root.lang = l;
    root.dataset.lang = l;
    document.querySelectorAll('[data-en][data-hr]').forEach(el => {
      el.textContent = el.dataset[l];
    });
    if (langBtn) {
      langBtn.querySelector('.lang-current').textContent = l === 'en' ? 'HR' : 'EN';
      langBtn.setAttribute('aria-label',l === 'en' ? 'Switch to Croatian' : 'Prebaci na engleski');
    }
    save('marko-portfolio-lang',l);
  }
  function theme(mode) {
    root.dataset.theme = mode;
    if (themeBtn) themeBtn.setAttribute('aria-label',mode === 'light' ? 'Switch to dark theme':'Switch to light theme');
    save('marko-portfolio-theme',mode);
  }
  language(get('marko-portfolio-lang') || 'en');
  theme(get('marko-portfolio-theme') || 'light');
  langBtn?.addEventListener('click',()=>language(root.lang === 'en' ? 'hr' : 'en'));
  themeBtn?.addEventListener('click',()=>theme(root.dataset.theme === 'light' ? 'dark' : 'light'));
  menuBtn?.addEventListener('click',()=>{ const open=nav.classList.toggle('open');menuBtn.setAttribute('aria-expanded',String(open));});
  nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{nav.classList.remove('open');menuBtn?.setAttribute('aria-expanded','false');}));
  const filterBtns = document.querySelectorAll('.filter-chip');
  const cards = document.querySelectorAll('.work-card[data-tags]');
  filterBtns.forEach(btn=>btn.addEventListener('click',()=>{
    const selected = btn.dataset.filter;
    filterBtns.forEach(b=>{const active=b===btn;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
    let shown = 0;
    cards.forEach(c=>{const visible=selected==='all'||c.dataset.tags.split(' ').includes(selected);c.hidden=!visible;if(visible)shown++;});
    const empty = document.querySelector('#filter-empty'); if(empty) empty.hidden=shown>0;
  }));
})();
