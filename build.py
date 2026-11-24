#!/usr/bin/env python3
"""Regenerate bilingual portfolio, case studies and articles. No dependencies."""
import json, html, pathlib
from datetime import date

ROOT = pathlib.Path(__file__).parent
DATA = json.loads((ROOT / 'content/projects.json').read_text(encoding='utf-8'))['projects']
ARTICLES = json.loads((ROOT / 'content/articles.json').read_text(encoding='utf-8'))['articles']
PUBLISHED = [a for a in ARTICLES if a.get('published')]
CATEGORIES = {'ecommerce':('eCommerce','eCommerce'),'logistics':('Logistics','Logistika'),'delivery':('Delivery','Isporuka'),'platform':('Platforms','Platforme'),'data':('Data','Podaci'),'loyalty':('Loyalty','Loyalty'),'product':('Product','Produkt'),'process':('Processes','Procesi'),'integration':('Integrations','Integracije'),'insurance':('Insurance','Osiguranje')}


def esc(text): return html.escape(str(text), quote=True)
def t(en, hr, tag='span', attrs=''):
    return f'<{tag}{attrs} data-en="{esc(en)}" data-hr="{esc(hr)}">{esc(en)}</{tag}>'
def abspath(rel, page_root): return page_root + rel


def header(page='',prefix=''):
    labels = [('index.html','About','O meni'),('work.html','Selected work','Projekti'),('articles.html','Articles','Članci'),('index.html#approach','How I work','Kako radim'),('index.html#contact','Contact','Kontakt')]
    nav=''.join(f'<a href="{prefix}{url}" {"aria-current=page" if page==url else ""}>{t(en,hr)}</a>' for url,en,hr in labels)
    return f'''<header class="site-header"><div class="shell header-inner">
      <a class="brand" href="{prefix}index.html" aria-label="Marko Dakić homepage"><span class="brand-symbol">md<span>.</span></span><span class="brand-copy">Marko Dakić<small>Digital Product · Transformation</small></span></a>
      <nav id="site-nav" class="site-nav" aria-label="Main navigation">{nav}</nav>
      <div class="tools"><button class="tool-btn language-btn" type="button" aria-label="Change language" id="langBtn"><span class="lang-current">HR</span><span class="mini-arrow">↗</span></button><button class="tool-btn theme-btn" id="themeBtn" aria-label="Toggle color theme" title="Toggle color theme"><span class="theme-icon">◐</span></button><button class="tool-btn mobile-menu" id="menuBtn" aria-label="Open navigation" aria-expanded="false" aria-controls="site-nav">☰</button></div>
    </div></header>'''


def footer(prefix=''):
    return f'''<footer class="site-footer"><div class="shell footer-inner"><div><span class="footer-brand">md.</span><span>© {date.today().year} Marko Dakić</span></div><p>{t('Made with care. Based in Croatia.','Napravljeno s razlogom. Iz Hrvatske.')}</p><a href="#top">{t('Back to top ↑','Na vrh ↑')}</a></div></footer>'''


def contact():
    return f'''<section class="contact-section shell" id="contact"><div class="contact-panel"><div class="contact-copy"><span class="kicker kicker-on-dark">{t('GOOD THINGS START WITH A CONVERSATION','DOBRE STVARI KREĆU RAZGOVOROM')}</span><h2>{t('Have a complex idea?', 'Imaš složenu ideju?')}<br><em>{t('Let’s make it work.','Pretvorimo je u nešto konkretno.')}</em></h2><p>{t('Open to senior Product, Delivery, eCommerce and Digital Transformation opportunities — where business, technology and people need to work together.','Otvoren sam za senior Product, Delivery, eCommerce i Digital Transformation prilike — tamo gdje treba povezati poslovanje, tehnologiju i ljude.')}</p></div><div class="contact-actions"><a class="button button-cream" href="mailto:marko.dakic@gmail.com?subject=Hello%20Marko">{t('Write me an email','Pošalji e-mail')} <span aria-hidden="true">↗</span></a><a class="contact-text" href="https://www.linkedin.com/in/marko-dakic/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a class="contact-text" href="mailto:marko.dakic@gmail.com?subject=CV%20request%20-%20Marko%20Dakic">{t('Request my CV','Zatraži moj CV')} ↗</a></div></div></section>'''


# Shared Cloudflare Web Analytics beacon for every generated page.
CLOUDFLARE_BEACON = """<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "6962ff0825304bbfbfc6558345bbcf2a"}'></script><!-- End Cloudflare Web Analytics -->"""

def head(title, description, prefix='', canonical_path=None):
    canonical = f'https://markodakic.github.io/{canonical_path}' if canonical_path is not None else None
    seo = f'<link rel="canonical" href="{esc(canonical)}"><meta property="og:url" content="{esc(canonical)}">' if canonical else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#ffffff"><meta name="description" content="{esc(description)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:image" content="https://markodakic.github.io/assets/og-md-logo.png"><meta property="og:image:secure_url" content="https://markodakic.github.io/assets/og-md-logo.png"><meta property="og:image:type" content="image/png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Marko Dakić — md logo"><meta name="twitter:image" content="https://markodakic.github.io/assets/og-md-logo.png">{seo}<meta name="twitter:card" content="summary_large_image"><meta name="color-scheme" content="light dark"><link rel="icon" type="image/svg+xml" href="{prefix}assets/favicon.svg?v=6"><link rel="stylesheet" href="{prefix}style.css?v=12"><script src="{prefix}script.js" defer></script><title>{esc(title)}</title>{CLOUDFLARE_BEACON}</head><body id="top"><a class="skip-link" href="#main">Skip to content</a>'''



COMPANY_DOMAINS = {'eKupi':'ekupi.hr','mStart':'mstart.hr','Konzum':'konzum.hr','Croatia osiguranje':'crosig.hr'}
COMPANY_LOGOS = {'eKupi':'assets/logos/ekupi.svg','Croatia osiguranje':'assets/logos/croatia-osiguranje.svg'}

def company_lockup(company):
    domain = COMPANY_DOMAINS.get(company)
    if not domain:
        return esc(company)
    src = COMPANY_LOGOS.get(company) or 'https://www.google.com/s2/favicons?domain='+domain+'&sz=64'
    return '<span class="company-lockup"><img src="'+esc(src)+'" alt="" loading="lazy"><span>'+esc(company)+'</span></span>'


def project_visual(p, prefix='', detail=False):
    """Render project images with an overlay, plus a caption on detail pages only."""
    path = str(p.get('image') or '').strip()
    if not path.startswith('assets/') or not (ROOT / path).is_file():
        return ''
    alt = str(p.get('image_alt') or f"Project visual: {p['company']}")
    css = 'project-real-visual project-real-visual-detail' if detail else 'project-real-visual project-card-visual'
    disclosure = 'Project photo' if p.get('id') == 'ekupi-outdoor-parcel-lockers' else 'AI-generated image'
    caption = f'<figcaption class="concept-caption">{disclosure}</figcaption>' if detail else ''
    overlay = "" if detail and p.get("id") == "konzum-pampers-club" else f'<span class="project-image-overlay" aria-hidden="true">{disclosure}</span>'
    return f'<figure class="{css}"><div class="project-image-media"><img src="{prefix}{esc(path)}" alt="{esc(alt)}" loading="lazy" decoding="async">{overlay}</div>{caption}</figure>'

def project_card(p,prefix='',i=0):
    d=p['en'];h=p['hr']; tags=' '.join(p['category']);
    link = f'{prefix}cases/{p["id"]}.html'
    chips=''.join(f'<span class="tag">{t(*CATEGORIES[k])}</span>' for k in p['category'][:2])
    return f'''<article class="work-card" data-tags="{tags}" data-name="{esc(d['title'])}" style="--card-n:{i}"><a href="{link}" class="work-card-link">{project_visual(p,prefix)}<div class="work-card-body"><div class="card-kicker">{company_lockup(p['company'])}<span aria-hidden="true">↗</span></div><h3>{t(d['title'],h['title'])}</h3><p>{t(d['summary'],h['summary'])}</p><div class="tag-row">{chips}</div></div></a></article>'''


def home():
    featured=[p for p in DATA if p['featured']][:4]
    cards=''.join(project_card(p,'',i) for i,p in enumerate(featured))
    return head('Marko Dakić | Digital Product, Delivery & eCommerce','Digital Product & Transformation | Product Ownership, IT Delivery and eCommerce. Project case studies and articles.',canonical_path='')+header('index.html')+f'''
    <main id="main">
      <section class="hero shell"><div class="hero-copy">
        <div class="hero-roleline">Digital Product &amp; Transformation</div><h1>{t('Digital products.','Digitalni proizvodi.')} <em>{t('Real delivery','Stvarna isporuka')}<span style="color:#e36f4b;">.</span></em></h1>
        <p class="hero-lead">{t('I connect business, people and technology to build digital products that make sense in the real world. From grocery eCommerce and logistics to modern self-service experiences.','Povezujem poslovanje, ljude i tehnologiju kako bih gradio digitalne proizvode koji imaju smisla u stvarnom životu. Od online maloprodaje i logistike do modernih samouslužnih rješenja.')}</p>
        <div class="hero-actions"><a class="button button-dark" href="work.html">{t('See what I’ve built','Pogledaj moje projekte')} <span>↗</span></a><a class="inline-action" href="articles.html">{t('Read my notes','Moji članci i testovi')} <span>↓</span></a></div>
        <div class="hero-proof" aria-label="Experience at a glance"><div class="proof-item"><strong>20<span>+</span></strong><span>{t('years in IT','godina u IT-u')}</span></div><div class="proof-item"><strong>10<span>+</span></strong><span>{t('years in eCommerce','godina u eCommerceu')}</span></div><div class="proof-item"><strong>13</strong><span>{t('documented project stories','obrađenih projekata')}</span></div></div><div class="hero-footnote"><span class="hero-cert-pill"><strong>CSPO®</strong> {t('Certified Scrum Product Owner','Certified Scrum Product Owner')}</span><span class="hero-scope-pill">{t('Retail, digital products & delivery','Maloprodaja, digitalni proizvodi i isporuka')}</span></div>
      </div>
      <div class="hero-showcase" aria-label="Creative illustration of connected digital products"><div class="showcase-glow"></div><div class="showcase-orbit showcase-orbit-1"></div><div class="showcase-orbit showcase-orbit-2"></div><div class="showcase-portrait" aria-label="Professional portrait area"><span class="portrait-fallback" aria-hidden="true">MD</span><img class="portrait-photo" src="assets/profile.jpg" alt="Marko Dakić" loading="eager" onerror="this.style.display='none'"></div><div class="floating-note note-top"><span>◈</span><div>Product<small>from idea to value</small></div></div><div class="floating-note note-left"><div>eCommerce<small>people first</small></div></div></div>
      </section>
      <section class="experience-ribbon"><div class="shell ribbon-inner"><span>{t('I’ve worked with','Moje iskustvo kroz')}</span><div>{company_lockup('Konzum')}{company_lockup('eKupi')}{company_lockup('mStart')}{company_lockup('Croatia osiguranje')}</div></div></section>
      <section class="section shell" id="approach"><div class="section-header"><div><div class="kicker">01 / {t('HOW I WORK','KAKO RADIM')}</div><h2>{t('Less buzzwords.','Manje velikih riječi.')}<br><em>{t('More things that work.','Više stvari koje rade.')}</em></h2></div><p>{t('Good delivery starts with understanding the problem. I help teams define priorities, make trade-offs and connect software with the messy, interesting world of real business.','Dobra isporuka počinje razumijevanjem problema. Pomažem timovima postaviti prioritete, donijeti odluke i povezati softver sa stvarnim poslovanjem — sa svim njegovim zanimljivim komplikacijama.')}</p></div>
      <div class="cap-grid"><article class="cap cap-a"><span class="cap-no">01</span><h3>{t('Product thinking','Produktni način razmišljanja')}</h3><p>{t('User journeys, MVP decisions, backlog priorities and a clear view of the value a feature should create.','Korisnički putovi, MVP odluke, prioriteti backloga i jasno razumijevanje vrijednosti koju funkcionalnost treba donijeti.')}</p></article><article class="cap cap-b"><span class="cap-no">02</span><h3>{t('Delivery leadership','Vođenje isporuke')}</h3><p>{t('Cross-functional teams, partners, integrations, releases and the everyday decisions that keep delivery moving.','Razvojni timovi, partneri, integracije, izdanja i svakodnevne odluke koje pomiču isporuku naprijed.')}</p></article><article class="cap cap-c"><span class="cap-no">03</span><h3>{t('Digital commerce','Digitalna trgovina')}</h3><p>{t('Webshops, omnichannel, loyalty, logistics, platforms and the operational processes behind a great customer experience.','Webshopovi, omnichannel, loyalty, logistika, platforme i procesi iza kvalitetnog korisničkog iskustva.')}</p></article></div></section>
      <section class="section shell section-work"><div class="section-header"><div><div class="kicker">02 / {t('SELECTED WORK','ODABRANI PROJEKTI')}</div><h2>{t('A few things I helped','Nekoliko stvari koje sam')}<br><em>{t('make happen.','pomogao realizirati.')}</em></h2></div><p>{t('Projects with different technologies, but one common thread: connecting decisions to real delivery.','Različite tehnologije i projekti, ali ista nit vodilja: povezati odluke sa stvarnom realizacijom.')}</p></div>
      <div class="work-grid">{cards}</div><div class="center-link"><a class="button button-outline" href="work.html">{t('Explore all 13 projects','Pogledaj svih 13 projekata')} <span>↗</span></a></div></section>
      <section class="section shell journey-section"><div class="section-header"><div><div class="kicker">03 / {t('MY JOURNEY','MOJ PUT')}</div><h2>{t('Built in retail.','Od maloprodaje.')}<br><em>{t('Driven by products.','Do digitalnih proizvoda.')}</em></h2></div><p>{t('I have moved between hands-on systems, development leadership, eCommerce platforms and product ownership — always close to the work that makes business change real.','Radio sam od operativnih sustava do vođenja razvoja, eCommerce platformi i product ownershipa — uvijek blizu konkretnih promjena koje poslovanje koristi.')}</p></div>
      <div class="timeline-grid"><div class="career-timeline"><div><span>2026 —</span><h3>Croatia osiguranje</h3><p>{t('Digital strategy, web & mobile product ownership, process automation','Digitalna strategija, web i mobilni proizvodi, automatizacija procesa')}</p></div><div><span>2021–2025</span><h3>mStart</h3><p>{t('eCommerce Product / Project Manager, Spryker','eCommerce Product / Project Manager, Spryker')}</p></div><div><span>2020–2021</span><h3>eKupi</h3><p>{t('Head of IT Development, commerce & logistics initiatives','Voditelj IT razvoja, eCommerce i logističke inicijative')}</p></div><div><span>2015–2020</span><h3>Konzum</h3><p>{t('Online Platforms → Head of eCommerce IT','Online platforme → Voditelj IT sektora za eCommerce')}</p></div></div>
      <aside class="career-aside"><h3>{t('Business context. Technical fluency. Human approach.','Poslovni kontekst. Tehnička širina. Ljudski pristup.')}</h3><p>{t('CSPO® · Bachelor of Business Informatics. I’m comfortable translating between executives, product teams, engineers and operational teams.','CSPO® · stručni prvostupnik poslovne informatike. Povezujem upravu, product timove, razvoj i operativne odjele.')}</p><div class="aside-tag">CSPO® <span>·</span> bacc. inf.</div></aside></div></section>
      <section class="forward-section shell"><div class="forward-inner"><div class="forward-top"><span>{t('WHAT I’M EXPLORING','ŠTO PRATIM')}</span></div><h2>{t('Commerce is changing.','Trgovina se mijenja.')} <em>{t('That’s the interesting part.','Baš tu postaje zanimljivo.')}</em></h2><p>{t('I follow Agentic Commerce, AI-assisted workflows and the growing importance of structured product data. I’m interested in practical use cases, not technology for its own sake.','Pratim Agentic Commerce, AI automatizaciju i sve veću važnost strukturiranih podataka o proizvodima. Zanimaju me konkretne primjene, ne tehnologija sama sebi svrha.')}</p><div class="forward-decor" aria-hidden="true">↗</div></div></section>
      <section class="section shell lab-home" id="lab"><div class="section-header"><div><div class="kicker">04 / {t('ARTICLES & LAB','ČLANCI I LAB')}</div><h2>{t('Curious by nature.','Znatiželjan po prirodi.')}<br><em>{t('Always experimenting.','Stalno nešto isprobavam.')}</em></h2></div><p>{t('Outside everyday product work, I try things for myself: private cloud computing, local AI, small automations and new ways of working. I document what actually helped, what did not, and what I learned.','Izvan svakodnevnog rada na digitalnim proizvodima volim stvari isprobati sam: privatni cloud, lokalni AI, male automatizacije i nove načine rada. Pišem što je stvarno pomoglo, što nije i što sam naučio.')}</p></div><div class="lab-home-feature"><div class="lab-feature-art"><span class="lab-art-small">DEIMOS / HOME LAB</span><span class="lab-art-icon">⌘</span><span class="lab-art-footer">PRIVATE TECH · REAL EXPERIMENTS</span></div><div class="lab-feature-copy"><div class="kicker">{t('WHAT I’M WRITING ABOUT','O ČEMU PIŠEM')}</div><h3>{t('Technology I actually use.','Tehnologija koju stvarno koristim.')}</h3><p>{t('A personal cloud PC, AI models running locally, connecting devices across platforms, and occasional thoughts about digital products and commerce.','Privatni Cloud PC, lokalni AI modeli, povezivanje uređaja i povremena razmišljanja o digitalnim proizvodima i eCommerceu.')}</p><a class="button button-outline" href="articles.html">{t('Browse Articles & Lab','Otvori Članke i Lab')} <span>↗</span></a></div></div></section>
      {contact()}
    </main>'''+footer()+'''</body></html>'''


def work():
    allcards=''.join(project_card(p,'',i) for i,p in enumerate(DATA))
    options='<button type="button" class="filter-chip active" data-filter="all" aria-pressed="true">'+t('All projects','Svi projekti')+f' <small>{len(DATA)}</small></button>'
    for k,(en,hr) in CATEGORIES.items():
        n=sum(k in p['category'] for p in DATA)
        if n:
            options+=f'<button type="button" class="filter-chip" data-filter="{k}" aria-pressed="false">{t(en,hr)} <small>{n}</small></button>'
    return head('Work | Marko Dakić','Detailed work and case studies across eCommerce, logistics, digital product, retail loyalty, platform integration and insurance.',canonical_path='work.html')+header('work.html')+f'''<main id="main"><section class="page-hero shell"><div class="kicker">{t('THE WORK / FROM IDEAS TO REALITY','PROJEKTI / OD IDEJE DO REALIZACIJE')}</div><h1>{t('Good work leaves','Dobar projekt ostavlja')}<br><em>{t('something useful behind.','nešto korisno iza sebe.')}</em></h1><p>{t('Here are projects I contributed to, led or delivered across retail, eCommerce, logistics and insurance. Open a case study to explore the challenge, my role, the work and the outcome.','Ovdje su projekti na kojima sam radio ili ih vodio u maloprodaji, eCommerceu, logistici i osiguranju. Otvori projekt i pogledaj izazov, moju ulogu, aktivnosti i rezultat.')}</p></section><section class="shell all-work"><div class="filters" role="group" aria-label="Filter project cards">{options}</div><div class="work-grid work-grid-all" id="project-grid">{allcards}</div><p id="filter-empty" hidden>{t('No projects in this category yet.','Za ovu kategoriju nema prikazanih projekata.')}</p></section>{contact()}</main>'''+footer()+'''</body></html>'''


def bullet_list(items_en,items_hr):
    return '<ul class="detail-list">'+''.join(f'<li><span aria-hidden="true">↗</span>{t(e,h)}</li>' for e,h in zip(items_en,items_hr))+'</ul>'


def case(p, idx):
    en=p['en'];hr=p['hr']; prefix='../'
    section=lambda no,title_en,title_hr,body: f'<section class="case-block"><div class="case-number">{no}</div><div><h2>{t(title_en,title_hr)}</h2>{body}</div></section>'
    blocks=section('01','The challenge','Izazov',f'<p>{t(en["challenge"],hr["challenge"])}</p>')+section('02','Why it mattered','Zašto je bilo važno',f'<p>{t(en["why"],hr["why"])}</p>')+section('03','My role','Moja uloga',bullet_list(en['role'],hr['role']))+section('04','What I did','Što sam radio',bullet_list(en['work'],hr['work']))+section('05','What came out of it','Što je ostvareno',bullet_list(en['results'],hr['results']))+section('06','My takeaway','Što mi je važno iz ovog projekta',f'<p class="lesson-copy">{t(en["lesson"],hr["lesson"])}</p>')
    tags=''.join(f'<span class="tag">{t(*CATEGORIES[c])}</span>' for c in p['category'])
    prev=DATA[(idx-1)%len(DATA)];nxt=DATA[(idx+1)%len(DATA)]
    return head(en['title']+' | Marko Dakić',en['summary'],prefix,canonical_path=f"cases/{p['id']}.html")+header('',prefix)+f'''<main id="main"><section class="shell case-intro"><a class="back-link" href="../work.html">← {t('All projects','Svi projekti')}</a><div class="case-meta">{esc(p['company'])} <span>·</span> {esc(p['period'])}</div><h1>{t(en['title'],hr['title'])}</h1><p class="case-deck">{t(en['summary'],hr['summary'])}</p><div class="tag-row">{tags}</div>{project_visual(p,prefix,True)}</section><section class="shell case-content"><div class="case-sections">{blocks}</div><aside class="case-aside"><div class="aside-card"><span>{t('PROJECT CONTEXT','KONTEKST PROJEKTA')}</span><strong>{esc(p['company'])}</strong><div>{esc(p['period'])}</div><hr><span>{t('AREAS','PODRUČJA')}</span><div class="tag-row">{tags}</div></div><p class="aside-note">{t('This public write-up focuses on my role and known project scope. Internal details and unverified business metrics are intentionally excluded.','Javni prikaz fokusiran je na moju ulogu i poznati opseg projekta. Interni detalji i neprovjereni poslovni rezultati namjerno su izostavljeni.')}</p></aside></section><div class="shell case-pager"><a href="{prev['id']}.html">← <span>{t('Previous project','Prethodni projekt')}</span><strong>{t(prev['en']['title'],prev['hr']['title'])}</strong></a><a href="{nxt['id']}.html"><span>{t('Next project','Sljedeći projekt')}</span><strong>{t(nxt['en']['title'],nxt['hr']['title'])}</strong> →</a></div>{contact()}</main>'''+footer()+'''</body></html>'''




def article_card(a, prefix=''):
    return f'''<article class="lab-entry"><div class="lab-entry-label">{esc(a['category'])} <span>·</span> {esc(a.get('year',''))}</div><h3><a href="{prefix}articles/{esc(a['id'])}.html">{t(a['en']['title'],a['hr']['title'])} <span aria-hidden="true">↗</span></a></h3><p>{t(a['en']['summary'],a['hr']['summary'])}</p><div class="lab-read">{t('Read the article','Pročitaj članak')} · {esc(a.get('read_minutes',6))} min</div></article>'''


def articles_index():
    cards = ''.join(article_card(a) for a in PUBLISHED)
    intro = f'''<div class="lab-intro-copy"><span class="kicker">{t('A PERSONAL NOTEBOOK','MOJE OSOBNE BILJEŠKE')}</span><h2>{t('Ideas from practice.','Ideje iz prakse.')}<br><em>{t('Projects, people, technology.','Projekti, ljudi, tehnologija.')}</em></h2><p>{t('I spend time trying technology for myself, then write about what I discovered — in plain language, without pretending every experiment is a breakthrough.','Volim osobno isprobati tehnologiju, pa onda jednostavno napisati što sam otkrio — bez pretvaranja svakog eksperimenta u veliku revoluciju.')}</p></div>'''
    upcoming = [
      ('01','My private Cloud PC','Moj privatni Cloud PC','Remote access, everyday computing and keeping more control over my setup.','Udaljeni pristup, svakodnevni rad i veća kontrola nad vlastitim sustavom.'),
      ('02','Local AI on a mini-PC','Lokalni AI na mini-PC računalu','Ollama, Open WebUI and practical tests on DEIMOS.','Ollama, Open WebUI i praktični testovi na DEIMOS-u.'),
      ('03','A portable workspace with Samsung DeX','Prijenosno radno mjesto uz Samsung DeX','What works when a phone becomes a desktop.','Što funkcionira kada mobitel postane radna površina.'),
      ('04','Digital commerce & AI','Digitalna trgovina i AI','Product thinking, agentic commerce and the real customer journey.','Produktni način razmišljanja, agentic commerce i stvarni korisnički put.'),
    ]
    future = ''.join(f'''<div class="lab-topic"><span>{no}</span><div><h3>{t(en,hr)}</h3><p>{t(d_en,d_hr)}</p></div><span class="topic-state">{t('On my radar','U bilješkama')}</span></div>''' for no,en,hr,d_en,d_hr in upcoming)
    published_section = f'''<section class="shell lab-published"><div class="kicker">{t('ARTICLES','ČLANCI')}</div><div class="lab-entry-grid">{cards}</div></section>'''
    return head('Articles & Lab | Marko Dakić','Personal experiments, home lab, local AI, digital commerce and practical technology notes.',canonical_path='articles.html')+header('articles.html')+f'''<main id="main"><section class="shell page-hero lab-page-hero"><div class="kicker">ARTICLES / LAB / IDEAS</div><h1>{t('Ideas worth','Ideje koje vrijedi')} <em>{t('sharing.','podijeliti.')}</em></h1><p>{t('Notes from my personal experiments in technology, small automations, local AI and digital products. The longer version lives here; LinkedIn is where I share a short introduction.','Bilješke iz mojih osobnih tehnoloških eksperimenata, malih automatizacija, lokalnog AI-ja i digitalnih proizvoda. Ovdje ostaje cijela priča, a na LinkedInu dijelim kratki uvod.')}</p></section><section class="shell lab-intro">{intro}<div class="lab-intro-accent"><div class="lab-intro-terminal"><span class="terminal-top">● ● ● &nbsp; MARKO / LAB</span><strong>learn → test → write<span>_</span></strong><small>No hype. Just things worth sharing.</small></div></div></section>{published_section}<section class="shell lab-upcoming"><div class="kicker">{t('TOPICS I’M EXPLORING','TEME KOJE ISTRAŽUJEM')}</div><h2>{t('On my desk','Na mom stolu')} <em>{t('right now.','trenutačno.')}</em></h2><div class="lab-topic-list">{future}</div></section>{contact()}</main>'''+footer()+'</body></html>'


def article_page(a):
    prefix='../'
    blocks=''
    for i,(se,sh) in enumerate(zip(a['en']['sections'],a['hr']['sections']),1):
        ens=''.join(f'<p>{t(p,ph)}</p>' for p,ph in zip(se['paragraphs'],sh['paragraphs']))
        blocks+=f'''<section class="article-section"><span class="article-sec-no">{i:02d}</span><div><h2>{t(se['heading'],sh['heading'])}</h2>{ens}</div></section>'''
        if a['id']=='private-cloud-pc' and i==1:
            blocks+='''<figure class="article-figure"><img src="../assets/cloud-pc-architecture.svg" width="1100" height="450" loading="lazy" alt="Private Cloud PC schematic"><figcaption>Redrawn architecture diagram; original images remain on LinkedIn.</figcaption></figure>'''
    return head(a['en']['title']+' | Marko Dakić',a['en']['summary'],prefix,canonical_path=f"articles/{a['id']}.html")+header('',prefix)+f'''<main id="main"><section class="shell article-intro"><a class="back-link" href="../articles.html">← {t('Articles & Lab','Članci i Lab')}</a><div class="case-meta">{esc(a['category'])} <span>·</span> {esc(a.get('year','2026'))} <span>·</span> {a.get('read_minutes',6)} MIN</div><h1>{t(a['en']['title'],a['hr']['title'])}</h1><p class="case-deck">{t(a['en']['summary'],a['hr']['summary'])}</p>{('<p class="article-source"><span>'+t('Adapted for this website from an earlier LinkedIn article.','Prilagođeno za ovu stranicu prema ranije objavljenom LinkedIn članku.')+'</span> <a href="'+esc(a['source_url'])+'" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></p>') if a.get('source_url') else ''}</section><section class="shell article-body">{blocks}<aside class="article-notice">{t('This is an edited website edition based on a previously published piece. Refer to the original on LinkedIn for the historical version.','Ovo je uređena web-verzija ranije objavljenog teksta. Izvorna verzija ostaje dostupna na LinkedInu.')}</aside><a class="button button-outline" href="../articles.html">{t('More articles and notes','Ostali članci i bilješke')} ↗</a></section>{contact()}</main>'''+footer()+'</body></html>'

def not_found():
    return head('Not found | Marko Dakić','Page not found')+header()+f'<main class="shell not-found" id="main"><h1>404</h1><p>{t("This page isn’t here. But the projects are.","Ova stranica nije ovdje. Ali projekti jesu.")}</p><a class="button button-dark" href="work.html">{t("Explore work","Pogledaj projekte")} ↗</a></main>'+footer()+'</body></html>'

if __name__=='__main__':
    (ROOT/'index.html').write_text(home(),encoding='utf-8')
    (ROOT/'work.html').write_text(work(),encoding='utf-8')
    (ROOT/'articles.html').write_text(articles_index(),encoding='utf-8')
    (ROOT/'404.html').write_text(not_found(),encoding='utf-8')
    for i,p in enumerate(DATA):
        (ROOT/'cases'/f'{p["id"]}.html').write_text(case(p,i),encoding='utf-8')
    (ROOT/'articles').mkdir(exist_ok=True)
    for a in PUBLISHED:
        (ROOT/'articles'/f"{a['id']}.html").write_text(article_page(a),encoding='utf-8')
    routes = ['', 'work.html', 'articles.html'] + [f"cases/{p['id']}.html" for p in DATA] + [f"articles/{a['id']}.html" for a in PUBLISHED]
    urls=''.join(f'<url><loc>https://markodakic.github.io/{esc(route)}</loc></url>' for route in routes)
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+urls+'</urlset>',encoding='utf-8')
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://markodakic.github.io/sitemap.xml\n',encoding='utf-8')
    print(f'Rebuilt home + work + articles + 404 + {len(DATA)} projects + {len(PUBLISHED)} published articles')
