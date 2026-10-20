# -*- coding: utf-8 -*-
"""Akbar Suffa Welfare Society static site generator (v2 redesign).
Design: logo colours (navy + red), full logo lockup header, expert copy, SEO."""
import os, json

ROOT = os.path.dirname(os.path.abspath(__file__))
V = "v=3"
BASE = "https://akbar-suffa-welfare.vercel.app"

PHONE = "0301-8451152"
PHONE_INTL = "+92 301 8451152"
WA = "https://wa.me/923018451152"
EMAIL = "Akbarsuffawelfaresociety@gmail.com"
ADDRESS = "Shalimar Chowk, Baghban Pura, Lahore, Pakistan"
UBL_ACC = "1342339071519"
FB = "https://www.facebook.com/share/18LEgsfbiw/"
TT = "https://www.tiktok.com/@akbarsuffawelfaresociety"
IG = "https://www.instagram.com/akbar.suffa.welfare.society"

PROJECTS = [
    ("project-funeral.html", "Unclaimed Funeral Support", "assets/img/funeral-work.jpg",
     "When someone dies with no family, no money and no one to claim them, we step in as family, ghusl, kafan, janaza and a dignified burial, completely free."),
    ("project-education.html", "Free Education for Poor Children", "assets/img/education-1.jpg",
     "Free schooling, books and mentorship for children whose parents cannot afford fees, because poverty should never decide a child's future."),
    ("project-elderly.html", "Monthly Support for Elderly Women", "assets/img/elderly.jpg",
     "A fixed monthly stipend, delivered with respect, so widowed and elderly mothers never have to beg for food, medicine or rent."),
    ("project-oldage.html", "Old Age Care & Shelter", "assets/img/oldage.jpg",
     "Food, care and shelter for elderly people left entirely alone, so no elder of our community spends their final years abandoned."),
    ("project-dastarkhwan.html", "Suffa Sasta Dastarkhwan", "assets/img/dastarkhwan.jpg",
     "Fresh, warm meals served daily with dignity. Pay a token amount if you can, eat free if you cannot. Nobody can tell the difference."),
    ("project-dispensary.html", "Suffa Free Dispensary", None,
     "Free check-ups and essential medicines for patients who would otherwise go untreated, because healthcare should not depend on a wallet."),
]

GIVING = [
    ("zakat.html", "Zakat", "Calculate your Zakat in minutes and pay it to verified deserving families, 100% distribution, zero admin deduction."),
    ("sadaqah.html", "Sadaqah & Sadaqah Jariyah", "Give Sadaqah for protection and blessing, or Sadaqah Jariyah that keeps rewarding you and your loved ones, every single day."),
    ("fitrana.html", "Fitrana", "Pay your Fitrana before Eid so every deserving family in Lahore can celebrate with a full table."),
    ("fidya.html", "Fidya & Kaffarah", "Missed fasts due to illness or age? We deliver the prescribed feeding to the poor, faithfully and on your behalf."),
    ("qurbani.html", "Qurbani", "Book your Qurbani share, Shariah-compliant sacrifice with same-day meat distribution to families who rarely eat meat."),
]

SCHEMA = {
    "@context": "https://schema.org",
    "@type": "NGO",
    "name": "Akbar Suffa Welfare Society",
    "url": BASE + "/",
    "logo": BASE + "/assets/img/logo-full.png",
    "description": "Registered welfare society in Lahore providing dignified burials for unclaimed deceased, free education, elderly women support, old age care, a community dastarkhwan and a free dispensary.",
    "email": EMAIL,
    "telephone": "+92-301-8451152",
    "address": {"@type": "PostalAddress", "streetAddress": "Shalimar Chowk, Baghban Pura",
                "addressLocality": "Lahore", "addressCountry": "PK"},
    "sameAs": [FB, TT, IG],
    "nonprofitStatus": "NonprofitType",
}


def head(title, desc, slug=""):
    url = BASE + "/" + slug
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Akbar Suffa Welfare Society Lahore</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow">
<meta property="og:site_name" content="Akbar Suffa Welfare Society">
<meta property="og:title" content="{title} | Akbar Suffa Welfare Society">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/assets/img/hero-janaza.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?{V}">
<script type="application/ld+json">{json.dumps(SCHEMA)}</script>
</head>
<body>"""


def header():
    proj_items = "\n".join(f'<li><a href="{u}">{n}</a></li>' for u, n, *_ in PROJECTS)
    give_items = "\n".join(f'<li><a href="{u}">{n}</a></li>' for u, n, d in GIVING)
    return f"""
<div class="topbar"><div class="wrap">
  <div class="tcontact">
    <a href="tel:+923018451152"><svg class="tic" viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.13.96.36 1.9.7 2.8a2 2 0 0 1-.45 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.25a2 2 0 0 1 2.1-.45c.9.34 1.84.57 2.8.7A2 2 0 0 1 22 16.9z"/></svg>{PHONE}</a>
    <a class="tmail" href="mailto:{EMAIL}"><svg class="tic" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg>{EMAIL}</a>
  </div>
  <div class="tsocial">
    <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook"><svg viewBox="0 0 24 24"><path d="M13.5 21v-7h2.4l.4-3h-2.8V9.1c0-.9.3-1.5 1.6-1.5h1.3V4.9c-.3 0-1.1-.1-2-.1-2 0-3.4 1.2-3.4 3.5V11H8.5v3H11v7h2.5z"/></svg></a>
    <a href="{TT}" target="_blank" rel="noopener" aria-label="TikTok"><svg viewBox="0 0 24 24"><path d="M16.6 3c.4 2.1 1.8 3.8 4 4.1v3c-1.6 0-3-.5-4-1.3v6.4c0 3.5-2.7 5.8-5.9 5.8a5.6 5.6 0 0 1-5.6-5.6c0-3.1 2.5-5.6 5.7-5.6.6 0 1.3.1 1.9.3v3.3c-.5-.3-1-.4-1.6-.4a2.4 2.4 0 0 0-2.4 2.4 2.4 2.4 0 0 0 2.4 2.4c1.4 0 2.5-1.1 2.5-2.6V3h3z"/></svg></a>
    <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="#ffb3b6" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r=".4" fill="#ffb3b6"/></svg></a>
  </div>
</div></div>
<header class="site"><div class="wrap nav">
  <a class="brand" href="index.html" aria-label="Akbar Suffa Welfare Society home page"><img src="assets/img/logo-full.png" alt="Akbar Suffa Welfare Society logo"></a>
  <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  <nav class="main" aria-label="Main navigation"><ul>
    <li><a class="nl" href="index.html">Home</a></li>
    <li><a class="nl" href="about.html">About</a></li>
    <li class="has-drop"><a class="nl parent-link" href="projects.html">Projects <span class="car">▾</span></a><ul class="drop"><li><a class="overview" href="projects.html">All Projects</a></li>{proj_items}</ul></li>
    <li class="has-drop"><a class="nl parent-link" href="zakat.html">Islamic Giving <span class="car">▾</span></a><ul class="drop">{give_items}</ul></li>
    <li><a class="nl" href="get-involved.html">Get Involved</a></li>
    <li><a class="nl" href="media.html">Media</a></li>
    <li><a class="nl" href="blog.html">Blog</a></li>
    <li><a class="nl" href="contact.html">Contact</a></li>
  </ul><a class="btn btn-red mobile-donate" href="donate.html">Donate Now</a></nav>
  <a class="btn btn-red nav-cta" href="donate.html">Donate Now</a>
</div></header>"""


def footer():
    proj_links = "\n".join(f'<a href="{u}">{n}</a>' for u, n, *_ in PROJECTS[:4])
    give_links = "\n".join(f'<a href="{u}">{n}</a>' for u, n, d in GIVING)
    return f"""
<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <span class="flogo"><img src="assets/img/logo-full.png" alt="Akbar Suffa Welfare Society"></span>
      <p>A registered welfare society serving Lahore with dignity, compassion and responsibility, dignified burials, free education, elderly care and daily meals for the deserving.</p>
    </div>
    <div><h4>Quick Links</h4>
      <a href="about.html">About Us</a><a href="projects.html">Our Projects</a>
      <a href="get-involved.html">Get Involved</a><a href="media.html">Media & Stories</a>
      <a href="blog.html">Blog</a><a href="contact.html">Contact</a></div>
    <div><h4>Islamic Giving</h4>{give_links}</div>
    <div><h4>Reach Us</h4>
      <div class="cinfo">
        <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span><span class="ctext"><span class="clabel">Visit Us</span><span class="cval">{ADDRESS}</span></span></div>
        <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.13.96.36 1.9.7 2.8a2 2 0 0 1-.45 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.25a2 2 0 0 1 2.1-.45c.9.34 1.84.57 2.8.7A2 2 0 0 1 22 16.9z"/></svg></span><span class="ctext"><span class="clabel">Call or WhatsApp</span><a class="cval" href="tel:+923018451152">{PHONE_INTL}</a></span></div>
        <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg></span><span class="ctext"><span class="clabel">Email Us</span><a class="cval" href="mailto:{EMAIL}">{EMAIL}</a></span></div>
      </div>
      <div class="bankcard"><div class="brow"><span class="cicon"><svg viewBox="0 0 24 24"><path d="M3 21h18"/><path d="M5 21v-8"/><path d="M9.5 21v-8"/><path d="M14.5 21v-8"/><path d="M19 21v-8"/><path d="m12 3 9 5H3l9-5z"/></svg></span><div class="blines"><b>Donate: UBL Bank</b><br><span>Account</span> {UBL_ACC}<br><span>Title</span> Akbar Suffa Welfare Society</div></div></div>
    </div>
  </div>
  <div class="fbar"><span>© 2026 Akbar Suffa Welfare Society (R). All rights reserved.</span>
  <span>Baghban Pura · Lahore · Pakistan</span></div>
</div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">
<svg viewBox="0 0 32 32"><path d="M16 3C9.4 3 4 8.3 4 14.9c0 2.6.8 5 2.3 7L4.8 28l6.3-1.4c1.5.8 3.2 1.2 4.9 1.2 6.6 0 12-5.3 12-11.9S22.6 3 16 3zm0 21.7c-1.5 0-3-.4-4.3-1.2l-.3-.2-3.3.7.7-3.2-.2-.3a9.7 9.7 0 0 1-1.5-5.2C7.1 9.9 11.1 5.9 16 5.9S24.9 9.9 24.9 14.9 20.9 24.7 16 24.7zm5.3-6.7c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1l-1 1.2c-.2.2-.4.2-.7.1a11.6 11.6 0 0 1-5.7-5c-.4-.7.5-.7 1.2-2.3.1-.3 0-.5 0-.6l-1-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.9.9-1.1 2.2-.2 3.9a20.6 20.6 0 0 0 4 4.9c1.5 1.4 2.9 2 3.9 2.2.6.1 1.2.1 1.6-.1.5-.2 1.7-.8 1.9-1.6.2-.7.2-1.3.1-1.5 0-.1-.3-.2-.6-.3z"/></svg></a>
<script src="js/main.js?{V}"></script>
</body></html>"""


def pagehero(title, sub):
    return f'<section class="pagehero"><div class="wrap"><h1>{title}</h1><p>{sub}</p></div></section>'


def donate_band():
    return f"""<div class="ctaband">
  <div><h2>Someone in Lahore Needs You <em>Today</em></h2>
  <p>UBL Bank · Account Title: Akbar Suffa Welfare Society · A/C {UBL_ACC}</p></div>
  <a class="btn btn-red" href="donate.html">Donate Now</a></div>"""


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


# ============================ HOME ============================
def home():
    cards = []
    for url, name, img, desc in PROJECTS:
        media = f'<img src="{img}" alt="{name}, Akbar Suffa Welfare Society, Lahore" loading="lazy">' if img else '<div class="icon">🩺</div>'
        cards.append(f'<article class="card">{media}<div class="body"><h3>{name}</h3><p>{desc}</p><a class="more" href="{url}">Learn more →</a></div></article>')
    give = "\n".join(f'<article class="card"><div class="body"><h3>{n}</h3><p>{d}</p><a class="more" href="{u}">Give now →</a></div></article>' for u, n, d in GIVING[:3])
    body = f"""
<main>
<section class="hero">
  <img class="bgimg" src="assets/img/hero-janaza.jpg" alt="Volunteers of Akbar Suffa Welfare Society offering janaza prayer for an unclaimed deceased in Lahore">
  <div class="shade"></div>
  <div class="wrap">
    <span class="kick">Registered Welfare Society · Lahore</span>
    <h1>No One Should Leave This World <em>Alone</em></h1>
    <p>When a person dies in Lahore with no family, no money and no one to claim them, we become their family. And while they live, we feed them, teach their children, and care for their mothers. That is the work your donation makes possible.</p>
    <div class="hero-btns"><a class="btn btn-red" href="donate.html">Donate Now</a><a class="btn btn-ghost-w" href="projects.html">See Our Work</a></div>
    <div class="trustrow"><span>100% Zakat to verified families</span><span>Receipt on WhatsApp</span><span>Serving since Baghban Pura</span></div>
  </div>
</section>
<div class="wrap"><div class="impact"><div class="grid">
  <div class="cell"><div class="num" data-count="850">0</div><div class="lbl">Dignified Burials Arranged</div></div>
  <div class="cell"><div class="num" data-count="320">0</div><div class="lbl">Children in Free Education</div></div>
  <div class="cell"><div class="num" data-count="150">0</div><div class="lbl">Elderly Women Supported Monthly</div></div>
  <div class="cell"><div class="num" data-count="45000">0</div><div class="lbl">Meals Served With Dignity</div></div>
</div></div></div>
<section class="section"><div class="wrap"><div class="split">
  <img src="assets/img/funeral-work.jpg" alt="Volunteer team of Akbar Suffa Welfare Society performing a burial service" loading="lazy">
  <div><span class="eyebrow">Who We Are</span>
    <h2>A Small Team With One Big Promise: Dignity for Every Human Being</h2>
    <p style="color:var(--muted);margin-top:14px">From one neighbourhood in Lahore, our volunteers work with hospitals, police and local families so that nobody faces their hardest day alone, not in hunger, not in illness, and not in death.</p>
    <ul class="tick">
      <li><b>Dignified burials</b> for unclaimed and destitute deceased</li>
      <li><b>Free education</b> for children poverty would leave behind</li>
      <li><b>Monthly stipends</b> for elderly and widowed mothers</li>
      <li><b>A dastarkhwan</b> where everyone eats with respect</li>
    </ul>
    <p style="margin-top:22px"><a class="btn btn-outline" href="about.html">Our Story</a></p>
  </div>
</div></div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">What We Do</span><h2>Six Projects. One Mission.</h2>
  <p>Every project answers a real cry for help in our community, and every one of them runs on your generosity.</p></div>
  <div class="cards">{''.join(cards)}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="story">
    <div><span class="kick">Our Signature Work</span>
      <h2>Aakhri Izzat: <em>The Last Honour</em></h2>
      <p style="margin-top:14px">He had no name in the hospital register. No family came forward. For three days, nobody claimed him. Then our volunteers arrived. They washed him with the care they would give their own father, wrapped him in a clean kafan, carried him on their own shoulders, gathered a congregation for his janaza, and buried him in a proper, marked grave.</p>
      <p>Every week, men and women who die unknown in this city receive the farewell every human being deserves. This is what your Sadaqah does here.</p>
      <p style="margin-top:20px"><a class="btn btn-red" href="project-funeral.html">About This Project</a></p>
    </div>
    <img src="assets/img/poster-funeral.jpg" alt="Funeral prayer gathering arranged by Akbar Suffa Welfare Society" loading="lazy">
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Islamic Giving</span><h2>Your Zakat & Sadaqah, Delivered Right</h2>
  <p>Shariah-compliant distribution to verified, deserving recipients, with complete transparency and a receipt for every donation.</p></div>
  <div class="cards">{give}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Where We Are Going</span><h2>Help Us Build What Comes Next</h2></div>
  <div class="cards">
    <article class="card"><div class="body"><h3>Sewing Training Center</h3><p>A center where women and young girls learn a skill and earn a respectable income from home, independence with dignity.</p></div></article>
    <article class="card"><div class="body"><h3>Orphan Care Center</h3><p>A safe, caring home where orphaned children receive shelter, education and guidance, and a real chance at life.</p></div></article>
    <article class="card"><div class="body"><h3>Primary School</h3><p>A dedicated school for orphan and poor children: quality education, character building, and hope for a brighter future.</p></div></article>
  </div>
  <div style="margin-top:46px">{donate_band()}</div>
</div></section>
</main>"""
    return head("Dignified Burials, Free Education & Elderly Care in Lahore",
                "Akbar Suffa Welfare Society (Baghban Pura, Lahore) arranges dignified burials for unclaimed deceased, free education for poor children, monthly support for elderly women and daily community meals. Donate Zakat & Sadaqah online.",
                "index.html") + header() + body + footer()


# ============================ ABOUT ============================
def about():
    body = pagehero("About Us", "A neighbourhood that refused to look away, and built a promise instead.") + f"""
<main><section class="section"><div class="wrap"><div class="split">
  <img src="assets/img/education-1.jpg" alt="A student receiving an achievement award at Suffa Educators, Lahore" loading="lazy">
  <div class="prose"><span class="eyebrow">Our Story</span>
    <h2>It Began With a Sight We Could Not Unsee</h2>
    <p>Akbar Suffa Welfare Society began in Baghban Pura, Lahore, with a painful reality: bodies lying unclaimed in hospital mortuaries, and funerals that never happened, because there was no family to arrange them, and no money to pay for them.</p>
    <p>So the neighbourhood made a decision: <b>not here. Not on our watch.</b> Volunteers organised a burial service that treats every deceased person, known or unknown, rich or destitute, with the same honour Islam commands.</p>
    <p>From that single act of dignity, the work kept growing: free education for poor children, monthly stipends for elderly mothers with no earner left, care and shelter for the abandoned old, a dispensary for the sick, and a dastarkhwan where anyone can sit down and eat with respect.</p>
  </div>
</div></div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Mission</span><h2>Three Values Run Everything We Do</h2></div>
  <div class="cards">
    <article class="card"><div class="body"><h3>Dignity</h3><p>Every human being deserves honour, the orphan in the classroom, the widow at our door, and the stranger on his final journey.</p></div></article>
    <article class="card"><div class="body"><h3>Transparency</h3><p>Your Zakat and Sadaqah are an amanah, a sacred trust. We distribute to verified deserving recipients and account for every rupee.</p></div></article>
    <article class="card"><div class="body"><h3>Compassion</h3><p>We never ask who someone is or where they come from. Need is the only question we ask.</p></div></article>
  </div>
  <div class="notebox" style="margin-top:36px"><b>Registered Society:</b> Akbar Suffa Welfare Society (R) · Shalimar Chowk, Baghban Pura, Lahore, Pakistan · President: Malik Akbar Ali · {PHONE_INTL}</div>
</div></section>
<section class="section"><div class="wrap">{donate_band()}</div></section></main>"""
    return head("About Us: Our Story & Mission",
                "The story of Akbar Suffa Welfare Society: how a Baghban Pura neighbourhood built Lahore's dignified burial service for the unclaimed dead, and grew into education, elderly care and community meals.",
                "about.html") + header() + body + footer()


# ============================ PROJECTS ============================
def projects_page():
    cards = []
    for url, name, img, desc in PROJECTS:
        media = f'<img src="{img}" alt="{name}, Akbar Suffa Welfare Society" loading="lazy">' if img else '<div class="icon">🩺</div>'
        cards.append(f'<article class="card">{media}<div class="body"><h3>{name}</h3><p>{desc}</p><a class="more" href="{url}">Full details →</a></div></article>')
    body = pagehero("Our Projects", "Six projects running today in Lahore. Each one answers a real cry for help in our community.") + f"""
<main><section class="section"><div class="wrap"><div class="cards">{''.join(cards)}</div>
<div style="margin-top:46px">{donate_band()}</div></div></section></main>"""
    return head("Our Projects: Burials, Education, Elderly Care and More",
                "Explore the six welfare projects of Akbar Suffa Welfare Society, Lahore: unclaimed funeral support, free education, elderly women stipends, old age care, Sasta Dastarkhwan and a free dispensary.",
                "projects.html") + header() + body + footer()


PROJECT_DETAILS = {
    "project-funeral.html": dict(
        title="Unclaimed Funeral Support",
        img="assets/img/funeral-work.jpg",
        intro="Our signature project. When a person dies in a Lahore hospital or on its streets with no family, no money and no one to claim the body, our volunteers step in as family.",
        paras=[
            "Every week, hospitals and police stations across Lahore call us about unclaimed and destitute deceased. Without a service like ours, these bodies face delay, indignity, or burial without rites, without a name, without a single prayer.",
            "Our trained volunteer team completes the full Islamic funeral: ghusl (ritual washing), a clean kafan (shroud), respectful transport, a congregational janaza prayer, and burial in a proper, marked grave, the same honour we would demand for our own parents.",
            "We also quietly support poor families who cannot afford a funeral for their own loved ones, so grief is never added to by shame."],
        points=["Full ghusl, kafan & burial arrangements", "Coordination with hospitals & police", "Congregational janaza with our volunteers", "Completely free for unclaimed & destitute deceased", "Quiet support for poor families' funerals"],
        stat=("850+", "dignified burials arranged so far")),
    "project-education.html": dict(
        title="Free Education for Poor Children",
        img="assets/img/education-2.jpg",
        intro="Education is the only lasting exit from poverty. We give free schooling, books and mentorship to children whose families cannot afford any of it.",
        paras=[
            "Through Suffa Educators and partner teachers, enrolled children receive regular classes, books, stationery and mentorship. Their progress is celebrated publicly, with awards for top performers, so the whole neighbourhood learns to honour learning.",
            "Parents who keep children home for work are counselled personally, with patience. And where a family's survival truly depends on it, education support is paired with monthly family assistance."],
        points=["Free classes & learning material", "Books, bags & stationery provided", "Awards & recognition for students", "Personal counselling for parents", "Special focus on girls' education"],
        stat=("320+", "children currently studying free")),
    "project-elderly.html": dict(
        title="Monthly Support for Elderly Women",
        img="assets/img/elderly.jpg",
        intro="Many elderly and widowed mothers in our area have outlived everyone who earned for them. A fixed monthly stipend protects what matters most to them: their dignity.",
        paras=[
            "Every beneficiary is verified by our local team and receives her monthly amount directly, privately and with respect. It covers the essentials: food, basic medicines and household needs.",
            "Our volunteers visit regularly too, because for many of these mothers, being remembered matters as much as the money."],
        points=["Verified monthly stipends", "Covers food & basic medicines", "Regular home visits by volunteers", "Complete privacy & dignity", "Priority to widows with no earner"],
        stat=("150+", "elderly women supported every month")),
    "project-oldage.html": dict(
        title="Old Age Care & Shelter",
        img="assets/img/oldage.jpg",
        intro="Some elderly people are left entirely alone, children gone, house empty, health failing. We arrange the care, food and shelter that make their final years safe.",
        paras=[
            "Residents under our care receive daily meals, basic medical attention through our dispensary, and safe shelter arrangements with trusted local partners.",
            "This project is the seed of our long-term dream: a dedicated care home in Baghban Pura for the elderly and for orphans."],
        points=["Daily meals & basic care", "Safe shelter arrangements", "Medical support via our dispensary", "Companionship & regular visits"],
        stat=("40+", "elders under regular care")),
    "project-dastarkhwan.html": dict(
        title="Suffa Sasta Dastarkhwan",
        img="assets/img/dastarkhwan.jpg",
        intro="A dining spread where labourers, travellers, students and the poor sit down to fresh, warm food, with respect, and never with questions.",
        paras=[
            "Hunger strips dignity faster than anything. At Suffa Sasta Dastarkhwan the rule is simple: pay a token amount if you can, eat completely free if you cannot, and nobody can tell the difference.",
            "The dastarkhwan also serves at funerals, community events and Ramadan iftars across Baghban Pura. Sponsoring one full day of meals is one of the most beloved forms of Sadaqah Jariyah among our donors."],
        points=["Fresh cooked meals, served daily", "Free for anyone who cannot pay", "Open to labourers, travellers & students", "Ramadan iftar arrangements", "Sponsor a full day of meals"],
        stat=("45,000+", "meals served with dignity")),
    "project-dispensary.html": dict(
        title="Suffa Free Dispensary",
        img=None,
        intro="Basic healthcare should never depend on the size of a wallet. Our free dispensary treats patients who would otherwise simply go untreated.",
        paras=[
            "Patients receive check-ups and essential medicines completely free. Serious cases are guided and referred to hospitals, with our volunteers helping families through the process.",
            "The dispensary works hand-in-hand with our elderly projects, providing regular check-ups for the mothers and elders under our care."],
        points=["Free basic check-ups", "Essential medicines, free", "Regular check-ups for our elderly beneficiaries", "Hospital referral guidance"],
        stat=("300+", "patients treated every month")),
}


def project_detail(url):
    d = PROJECT_DETAILS[url]
    media = f'<img src="{d["img"]}" alt="{d["title"]}, Akbar Suffa Welfare Society, Lahore" loading="lazy">' if d["img"] else '<div class="icon" style="font-size:110px;text-align:center;padding:60px 0">🩺</div>'
    paras = "\n".join(f"<p>{p}</p>" for p in d["paras"])
    points = "\n".join(f"<li>{p}</li>" for p in d["points"])
    body = pagehero(d["title"], d["intro"]) + f"""
<main><section class="section"><div class="wrap"><div class="split" style="align-items:start">
  <div>{media}
    <div class="calc" style="margin-top:22px;padding:22px"><div class="result" style="margin:0"><span class="big">{d['stat'][0]}</span><br>{d['stat'][1]}</div></div>
  </div>
  <div class="prose"><span class="eyebrow">Project Detail</span><h2>About This Project</h2>{paras}
    <h3 style="margin-top:22px">What Your Support Provides</h3>
    <ul class="tick">{points}</ul>
    <p style="margin-top:24px"><a class="btn btn-red" href="donate.html">Donate to This Project</a> <a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">Ask on WhatsApp</a></p>
  </div>
</div>
<div style="margin-top:54px">{donate_band()}</div>
</div></section></main>"""
    return head(d["title"], d["intro"], url) + header() + body + footer()


# ============================ ISLAMIC GIVING ============================
def giving_page(slug, title, intro, paras, points, amounts, extra=""):
    paras_h = "\n".join(f"<p>{p}</p>" for p in paras)
    points_h = "\n".join(f"<li>{p}</li>" for p in points)
    amt = "\n".join(f'<button type="button" data-amt="{a}">Rs {a:,}</button>' for a in amounts)
    body = pagehero(title, intro) + f"""
<main><section class="section"><div class="wrap"><div class="split" style="align-items:start">
  <div class="prose"><span class="eyebrow">Islamic Giving</span><h2>About {title}</h2>{paras_h}
    <h3 style="margin-top:20px">How We Distribute</h3>
    <ul class="tick">{points_h}</ul>
    <p style="margin-top:16px">Give by bank transfer, UBL Bank · Akbar Suffa Welfare Society · A/C {UBL_ACC}, or use the form and our team will confirm your donation on WhatsApp.</p>
  </div>
  <form class="form demo-form" action="#" method="post">
    <h3>Give {title} Now</h3>
    <label>Your Name</label><input type="text" name="name" placeholder="Full name" required>
    <label>Mobile / WhatsApp</label><input type="tel" name="phone" placeholder="03XX-XXXXXXX" required>
    <label>Select Amount (PKR)</label>
    <div class="amounts">{amt}</div>
    <label>Or Enter Your Amount</label><input type="number" name="amount" min="10" placeholder="e.g. 5000">
    <input type="hidden" name="fund" value="{title}">
    <p style="margin-top:18px"><button class="btn btn-red" type="submit" style="width:100%">Confirm My Donation</button></p>
    <div class="thanks">JazakAllah Khair! Your intention has been noted. Our team will contact you on WhatsApp shortly to confirm the transfer and issue your receipt.</div>
  </form>
</div>{extra}
<div style="margin-top:54px">{donate_band()}</div>
</div></section></main>"""
    return head(title, intro, slug) + header() + body + footer()


ZAKAT_CALC = """
<div class="sec-head" style="margin-top:70px"><span class="eyebrow">Free Tool</span><h2>Zakat Calculator</h2>
<p>Enter your assets in PKR. Zakat is 2.5% of zakat-able wealth above the nisab (87.48g gold).</p></div>
<div class="calc" style="max-width:660px;margin:0 auto">
  <div class="form" style="border:0;box-shadow:none;padding:0">
    <label>Today's Gold Price (per tola, PKR)</label><input type="number" id="zk-gold-price" placeholder="e.g. 380000">
    <label>Cash in Hand & Bank Accounts</label><input type="number" id="zk-cash" placeholder="0">
    <label>Value of Gold You Own (PKR)</label><input type="number" id="zk-gold-val" placeholder="0">
    <label>Value of Silver You Own (PKR)</label><input type="number" id="zk-silver-val" placeholder="0">
    <label>Business Goods / Trade Assets (PKR)</label><input type="number" id="zk-business" placeholder="0">
    <label>Money You Owe Others (debts, PKR)</label><input type="number" id="zk-debts" placeholder="0">
    <p style="margin-top:18px"><button class="btn btn-navy" id="zk-btn" type="button" style="width:100%">Calculate My Zakat</button></p>
  </div>
  <div class="result" id="zk-out">Your result will appear here.</div>
  <p class="small" style="margin-top:12px;text-align:center">A guide based on the gold nisab. For personal rulings, please consult a qualified scholar.</p>
</div>"""


# ============================ GET INVOLVED ============================
def get_involved():
    body = pagehero("Get Involved", "Money is only one way to serve. Give your time, your skill, or a small monthly commitment, and become part of the work itself.") + f"""
<main><section class="section"><div class="wrap">
  <div class="cards">
    <article class="card"><div class="body"><h3>Become a Volunteer</h3><p>Join the burial team, serve at the dastarkhwan, teach a child, or run our media. Our volunteers are not helpers, they are the backbone of every project.</p><a class="more" href="#volunteer">Apply below ↓</a></div></article>
    <article class="card"><div class="body"><h3>Become a Monthly Saathi</h3><p>Pledge Rs 500 or Rs 1,000 every month. Small, regular giving keeps meals cooking and stipends paid in every season, not only in Ramadan.</p><a class="more" href="donate.html">Start monthly giving →</a></div></article>
    <article class="card"><div class="body"><h3>Sponsor Something Specific</h3><p>A student's full year of education. One complete dignified burial. A full day of dastarkhwan meals. Give it in your name, or in a loved one's.</p><a class="more" href="donate.html">See sponsorship options →</a></div></article>
  </div>
  <div class="split" style="margin-top:64px;align-items:start">
    <div class="prose"><span class="eyebrow">For Businesses & Schools</span>
      <h2>Partner With Us</h2>
      <p>Shops, companies and schools across Lahore already partner with the Society, placing donation boxes, sponsoring dastarkhwan days, donating goods in kind, and sending students and staff for supervised volunteer work.</p>
      <ul class="tick"><li>Donation box placement at your premises</li><li>Sponsored meals & project days</li><li>CSR & student volunteer programmes</li><li>In-kind donations: food, cloth, medicines</li></ul>
      <p style="margin-top:16px">Start the conversation on <a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a>.</p>
    </div>
    <form class="form demo-form" id="volunteer" action="#" method="post">
      <h3>Volunteer Application</h3>
      <label>Your Name</label><input type="text" name="name" required placeholder="Full name">
      <label>Mobile / WhatsApp</label><input type="tel" name="phone" required placeholder="03XX-XXXXXXX">
      <label>Your Area / Mohalla</label><input type="text" name="area" placeholder="e.g. Baghban Pura">
      <label>I Want to Help With</label>
      <select name="role"><option>Burial & funeral team</option><option>Dastarkhwan service</option><option>Teaching / education</option><option>Media & social media</option><option>Medical / dispensary</option><option>Fundraising</option><option>Other</option></select>
      <label>Anything We Should Know?</label><textarea name="msg" rows="3" placeholder="Your skills, availability..."></textarea>
      <p style="margin-top:18px"><button class="btn btn-red" type="submit" style="width:100%">Submit Application</button></p>
      <div class="thanks">Thank you for stepping forward! Our volunteer coordinator will contact you on WhatsApp.</div>
    </form>
  </div>
</div></section></main>"""
    return head("Get Involved: Volunteer, Monthly Giving and Sponsorship",
                "Volunteer with Akbar Suffa Welfare Society, become a Monthly Saathi, sponsor a burial, a student or a dastarkhwan day, or partner your business or school with us in Lahore.",
                "get-involved.html") + header() + body + footer()


# ============================ DONATE ============================
def donate():
    body = pagehero("Donate", "Every rupee you give is an amanah, a sacred trust. Choose your fund, pick an amount, and know exactly what it will do.") + f"""
<main><section class="section"><div class="wrap">
  <div class="split" style="align-items:start">
    <div>
      <div class="bankbox"><h3>Bank <span>Transfer</span></h3>
        <div class="row"><span>Bank</span><b>UBL Bank</b></div>
        <div class="row"><span>Account Title</span><b>Akbar Suffa Welfare Society</b></div>
        <div class="row"><span>Account Number</span><b>{UBL_ACC}</b></div>
        <div class="row"><span>IBAN</span><b>To be added</b></div>
        <p class="copyhint" style="margin-top:12px">After transferring, send your receipt on WhatsApp ({PHONE}) and we will issue your donation receipt.</p>
      </div>
      <div class="form" style="margin-top:24px"><h3>Mobile Accounts</h3>
        <p style="color:var(--muted);font-size:15px;margin-top:8px">JazzCash and EasyPaisa details will be added here soon. For now, please donate by bank transfer, or message us on WhatsApp and we will guide you.</p>
        <p style="margin-top:14px"><a class="btn btn-navy" href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></p>
      </div>
      <div class="notebox" style="margin-top:24px"><b>What your money does:</b><br>
      <b>Rs 1,000</b>, one day of dastarkhwan meals for the poor<br>
      <b>Rs 3,500</b>, one elderly mother's full monthly stipend<br>
      <b>Rs 5,000</b>, one complete dignified burial: ghusl, kafan, janaza, grave<br>
      <b>Rs 12,000</b>, one child's full year of education support</div>
    </div>
    <form class="form demo-form" action="#" method="post">
      <h3>Make a Donation</h3>
      <label>Your Name</label><input type="text" name="name" required placeholder="Full name">
      <label>Mobile / WhatsApp</label><input type="tel" name="phone" required placeholder="03XX-XXXXXXX">
      <label>Fund Type</label>
      <select name="fund"><option>General Donation</option><option>Zakat</option><option>Sadaqah</option><option>Sadaqah Jariyah</option><option>Lillah</option><option>Fitrana</option><option>Fidya / Kaffarah</option></select>
      <label>Project</label>
      <select name="project"><option>Where most needed</option><option>Unclaimed Funeral Support</option><option>Free Education</option><option>Elderly Women Support</option><option>Old Age Care & Shelter</option><option>Sasta Dastarkhwan</option><option>Free Dispensary</option></select>
      <label>Select Amount (PKR)</label>
      <div class="amounts"><button type="button" data-amt="1000">Rs 1,000</button><button type="button" data-amt="3500">Rs 3,500</button><button type="button" data-amt="5000">Rs 5,000</button><button type="button" data-amt="12000">Rs 12,000</button></div>
      <label>Or Enter Your Amount</label><input type="number" name="amount" min="10" placeholder="e.g. 2000">
      <label style="display:flex;gap:10px;align-items:center;font-weight:600"><input type="checkbox" name="monthly" style="width:auto"> Make it monthly (become a Monthly Saathi)</label>
      <p style="margin-top:18px"><button class="btn btn-red" type="submit" style="width:100%">Confirm My Donation</button></p>
      <div class="thanks">JazakAllah Khair! Your donation intention is noted. Our team will WhatsApp you the confirmation and your receipt.</div>
    </form>
  </div>
</div></section></main>"""
    return head("Donate, Zakat, Sadaqah & General Charity",
                "Donate to Akbar Suffa Welfare Society, Lahore: Zakat, Sadaqah, Sadaqah Jariyah, Fitrana & general charity via UBL bank transfer. Rs 5,000 funds one complete dignified burial.",
                "donate.html") + header() + body + footer()


# ============================ MEDIA ============================
def media_page():
    tt_videos = [
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7593776403967905045", "Field Work in the Community", "Our volunteers at work in Baghban Pura, where every project begins."),
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7646679219174427911", "Serving the Deserving", "A glimpse of the people your donations reach, every single week."),
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7625693484179131666", "Our Volunteers in Action", "The hands behind the mission, serving with dignity and without cameras in mind."),
    ]
    vids = "\n".join(f'<article class="vcard"><div class="vbody"><h3>{t}</h3><p>{d}</p><p style="margin-top:12px"><a class="btn btn-outline" href="{u}" target="_blank" rel="noopener">▶ Watch on TikTok</a></p></div></article>' for u, t, d in tt_videos)
    body = pagehero("Media & Stories", "Real work. Real people. Real change, documented from the streets and mohallas of Lahore.") + f"""
<main><section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Gallery</span><h2>From the Field</h2></div>
  <div class="gallery">
    <img src="assets/img/hero-janaza.jpg" alt="Janaza prayer arranged for an unclaimed deceased, Lahore" loading="lazy">
    <img src="assets/img/funeral-work.jpg" alt="Volunteers performing a burial service" loading="lazy">
    <img src="assets/img/education-1.jpg" alt="Student receiving an award at Suffa Educators" loading="lazy">
    <img src="assets/img/education-2.jpg" alt="Student receiving a trophy for academic achievement" loading="lazy">
    <img src="assets/img/dastarkhwan.jpg" alt="Meals being served at Suffa Sasta Dastarkhwan" loading="lazy">
    <img src="assets/img/elderly.jpg" alt="Elderly women receiving monthly financial support" loading="lazy">
  </div>
  <div class="sec-head" style="margin-top:74px"><span class="eyebrow">Videos</span><h2>Watch the Work Happen</h2>
  <p>Follow our daily work on TikTok, Facebook and Instagram, and share it. Every share carries this message of dignity further.</p></div>
  <div class="videos">{vids}</div>
  <div class="story" style="margin-top:64px">
    <div><span class="kick">A True Story</span><h2>A Grave With a <em>Name</em></h2>
      <p style="margin-top:12px">Last winter, an elderly man was found deceased near Shalimar. No ID. No phone. No family traced for days. Our team completed his ghusl and janaza, and then, with the help of a neighbour who finally recognised him, his grave was marked with his real name.</p>
      <p>A name matters. It is the difference between being forgotten, and being remembered in people's prayers. Stories like his are why we exist, and why your support must never stop.</p></div>
    <img src="assets/img/poster-dastarkhwan.jpg" alt="Suffa Sasta Dastarkhwan community meal poster" loading="lazy">
  </div>
</div></section></main>"""
    return head("Media and Stories: Photos and Videos From the Field",
                "Photos, videos and true stories from the field work of Akbar Suffa Welfare Society, Lahore, burials, education, dastarkhwan and elderly care.",
                "media.html") + header() + body + footer()


# ============================ BLOG ============================
ARTICLES = [
    ("blog-zakat-guide.html", "Zakat in Pakistan: A Simple, Complete Guide", "Who must pay Zakat, what wealth it applies to, and the nisab explained in plain words, plus how to be sure your Zakat reaches the truly deserving.", "Zakat Guide"),
    ("blog-akhri-izzat.html", "Aakhri Izzat: Why Every Deceased Person Deserves a Dignified Farewell", "What happens to unclaimed bodies in a city of millions, and how one small team in Baghban Pura is changing it, one janaza at a time.", "Our Story"),
    ("blog-fitrana-guide.html", "Fitrana: Rates, Rules and Who Receives It", "What Fitrana is, when to pay it and the per-person rate, and how your Fitrah puts a full Eid meal on a poor family's table.", "Ramadan Guide"),
]


def blog_page():
    cards = "\n".join(f'<article class="card"><div class="body"><span class="badge">{tag}</span><h3>{t}</h3><p>{d}</p><a class="more" href="{u}">Read article →</a></div></article>' for u, t, d, tag in ARTICLES)
    body = pagehero("Blog", "Clear guidance on Islamic giving, and honest stories from our work in Lahore.") + f"""
<main><section class="section"><div class="wrap"><div class="cards">{cards}</div></div></section></main>"""
    return head("Blog: Zakat Guides, Ramadan Guidance and True Stories",
                "Read the Akbar Suffa Welfare Society blog: a simple Zakat guide for Pakistan, Fitrana rules and rates, and true stories from our welfare work in Lahore.",
                "blog.html") + header() + body + footer()


def article_page(url):
    data = {u: (t, d, tag) for u, t, d, tag in ARTICLES}
    t, d, tag = data[url]
    if "zakat-guide" in url:
        paras = [
            "Zakat is the third pillar of Islam, an obligatory charity of 2.5% on your zakat-able wealth, paid once every lunar year. It is not a favour to the poor; in the Quran's words, it is their established right in your wealth.",
            "<b>Who must pay?</b> Every adult Muslim whose wealth reaches the nisab and stays above it for a full lunar year. The nisab equals 87.48 grams of gold (7.5 tola), or its cash equivalent. Our free Zakat Calculator on the Zakat page works your exact amount out in minutes.",
            "<b>What wealth counts?</b> Cash in hand and in bank accounts, gold and silver, and goods held for trade. Your home, your car and your personal belongings do not count. Money you owe others is deducted first.",
            "<b>Who can receive it?</b> Surah At-Tawbah (9:60) defines the categories, headed by the poor (fuqara) and the needy (masakin). Zakat cannot be given to your parents, spouse or children, and it must not be spent on buildings or administration.",
            "<b>How we distribute it:</b> the Society maintains a verified register of deserving families, widows, orphans, the sick, and daily-wage earners in genuine hardship. One hundred percent of your Zakat reaches eligible recipients. No admin deduction. Ever."]
        cta = ("zakat.html", "Calculate & Pay Your Zakat")
    elif "akhri-izzat" in url:
        paras = [
            "Every week in Lahore, people die unknown. An accident victim carrying no ID. An elderly labourer hundreds of miles from his village. A patient in a public hospital whose family cannot be traced. Their bodies wait in mortuaries, and without someone to claim them, their final journey can be delayed, stripped of dignity, or completed without the rites every Muslim deserves.",
            "Islam honours the dead exactly as it honours the living. Ghusl (washing), kafan (shrouding), janaza (the funeral prayer) and a proper grave are not optional extras. They are rights, of the poorest stranger exactly as much as of the richest citizen.",
            "This is the work Akbar Suffa Welfare Society was founded to do. Our volunteers coordinate with hospitals and police, perform every rite with trained hands, gather a congregation for the janaza, and bury each person in a proper, marked grave. And for poor families who simply cannot afford a funeral, we quietly cover the cost, so grief is never mixed with shame.",
            "One complete, dignified farewell costs around Rs 5,000. Given as Sadaqah Jariyah for your own parents, there are few gifts more meaningful, and few more needed."]
        cta = ("project-funeral.html", "See the Funeral Support Project")
    else:
        paras = [
            "Fitrana (Sadaqat-ul-Fitr) is the charity paid before the Eid-ul-Fitr prayer, so that the poor can eat, dress and celebrate on Eid day too. It is obligatory on every Muslim who has food beyond one day's need, paid for yourself and for your dependents.",
            "<b>How much?</b> Fitrana equals the value of roughly 2.25 kg of wheat per person (or its equivalent in dates, barley or raisins). Scholars announce the official cash rate each Ramadan based on market prices; in recent years the wheat-based rate in Pakistan has been around Rs 300 per person. Please confirm the current year's rate when Ramadan begins.",
            "<b>When to pay?</b> Any time during Ramadan, but the earlier the better, and always before the Eid prayer, so families can prepare. The Society distributes Fitrana as food packages and cash support to verified deserving families ahead of Eid day.",
            "<b>Who receives it?</b> The same deserving categories as Zakat, the poor and the needy. Pay yours on our Fitrana page and we will deliver it before Eid, in sha Allah."]
        cta = ("fitrana.html", "Pay Your Fitrana")
    paras_h = "\n".join(f"<p>{p}</p>" for p in paras)
    body = pagehero(t, d) + f"""
<main><section class="section"><div class="wrap" style="max-width:820px">
  <span class="badge">{tag}</span>
  <article class="prose" style="margin-top:14px">{paras_h}</article>
  <p style="margin-top:28px"><a class="btn btn-red" href="{cta[0]}">{cta[1]}</a> <a class="btn btn-outline" href="blog.html">← All Articles</a></p>
</div></section></main>"""
    return head(t, d, url) + header() + body + footer()


# ============================ CONTACT ============================
def contact():
    body = pagehero("Contact Us", "Visit us, call us, or message on WhatsApp. A real person replies, usually the same day.") + f"""
<main><section class="section"><div class="wrap"><div class="split" style="align-items:start">
  <div class="prose">
    <span class="eyebrow">Get In Touch</span><h2>Reach the Society</h2>
    <div class="cinfo light" style="margin:20px 0 6px">
      <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg></span><span class="ctext"><span class="clabel">Address</span><span class="cval">{ADDRESS}</span></span></div>
      <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.13.96.36 1.9.7 2.8a2 2 0 0 1-.45 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.25a2 2 0 0 1 2.1-.45c.9.34 1.84.57 2.8.7A2 2 0 0 1 22 16.9z"/></svg></span><span class="ctext"><span class="clabel">Phone / WhatsApp</span><a class="cval" href="tel:+923018451152">{PHONE_INTL}</a></span></div>
      <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/></svg></span><span class="ctext"><span class="clabel">Email</span><a class="cval" href="mailto:{EMAIL}">{EMAIL}</a></span></div>
      <div class="crow"><span class="cicon"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 3.6-6.5 8-6.5s8 2.5 8 6.5"/></svg></span><span class="ctext"><span class="clabel">President</span><span class="cval">Malik Akbar Ali</span></span></div>
    </div>
    <p>For urgent funeral support, call or WhatsApp at any hour, our volunteer team responds day and night.</p>
    <p style="margin-top:16px"><a class="btn btn-navy" href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
    <div style="margin-top:26px;border-radius:14px;overflow:hidden;border:1px solid var(--line)">
      <iframe title="Map of Baghban Pura, Lahore" src="https://www.google.com/maps?q=Baghbanpura,+Lahore,+Pakistan&output=embed" style="width:100%;height:300px;border:0" loading="lazy"></iframe>
    </div>
  </div>
  <form class="form demo-form" action="#" method="post">
    <h3>Send a Message</h3>
    <label>Your Name</label><input type="text" name="name" required placeholder="Full name">
    <label>Email or Phone</label><input type="text" name="contact" required placeholder="How can we reply to you?">
    <label>Subject</label>
    <select name="subject"><option>General question</option><option>Donation</option><option>Funeral support (urgent)</option><option>Volunteer</option><option>Request for help</option><option>Other</option></select>
    <label>Message</label><textarea name="msg" rows="5" required placeholder="Write your message..."></textarea>
    <p style="margin-top:18px"><button class="btn btn-red" type="submit" style="width:100%">Send Message</button></p>
    <div class="thanks">Thank you! Your message has been received. We will reply soon, in sha Allah.</div>
  </form>
</div></div></section></main>"""
    return head("Contact Us: Phone, WhatsApp and Address in Lahore",
                "Contact Akbar Suffa Welfare Society: Shalimar Chowk, Baghban Pura, Lahore. Call or WhatsApp 0301-8451152, urgent funeral support, day and night.",
                "contact.html") + header() + body + footer()


# ============================ BUILD ALL ============================
ALL_PAGES = ["index.html", "about.html", "projects.html"] + [u for u, *_ in PROJECTS] + \
            [u for u, *_ in GIVING] + ["get-involved.html", "donate.html", "media.html", "blog.html"] + \
            [u for u, *_ in ARTICLES] + ["contact.html"]

if __name__ == "__main__":
    write("index.html", home())
    write("about.html", about())
    write("projects.html", projects_page())
    for url, *_ in PROJECTS:
        write(url, project_detail(url))
    write("zakat.html", giving_page("zakat.html", "Zakat",
        "Your Zakat is a trust, and we treat it like one. We distribute it to verified, deserving Muslim families in cash, food and medicine, exactly as Shariah requires.",
        ["Zakat is a pillar of Islam: 2.5% of your zakat-able wealth, given once a year to the poor and needy. It purifies your wealth, and it is the right of the poor, not a favour from the rich.",
         "The Society maintains a verified register of deserving families across Baghban Pura and greater Lahore: widows, orphans, the chronically sick, and daily-wage earners in genuine hardship. Your Zakat reaches them directly, and it is never spent on administration, salaries or buildings.",
         "Not sure what you owe? Use the free calculator below. It follows the gold nisab standard, 7.5 tola (87.48 grams) of gold."],
        ["100% of Zakat reaches eligible recipients", "Verified, local deserving families", "Zero admin deduction from Zakat funds", "Distribution with complete dignity & privacy"],
        [2500, 5000, 10000, 25000], extra=ZAKAT_CALC))
    write("sadaqah.html", giving_page("sadaqah.html", "Sadaqah & Sadaqah Jariyah",
        "Sadaqah brings protection and opens the doors of rizq. Sadaqah Jariyah, ongoing charity, keeps rewarding you and your loved ones long after it is given.",
        ["The Prophet Muhammad ﷺ said: 'When a person dies, his deeds come to an end except three: ongoing charity (Sadaqah Jariyah), beneficial knowledge, or a righteous child who prays for him.' (Muslim)",
         "Give Sadaqah for your family's protection and blessing, or Sadaqah Jariyah on behalf of your parents and departed loved ones. Here, the most powerful Jariyah projects are a sponsored dignified burial, a child's year of education, and a day of dastarkhwan meals: deeds whose reward repeats, every single day."],
        ["Distributed as food, medicine, burials & education", "Give for the living, or for the departed", "Jariyah projects repeat their reward daily"], [1000, 3500, 5000, 12000]))
    write("fitrana.html", giving_page("fitrana.html", "Fitrana (Sadaqat-ul-Fitr)",
        "Pay your Fitrana before the Eid prayer, and put a full Eid table in front of a family that would otherwise go without.",
        ["Fitrana is obligatory on every Muslim who has food beyond one day's need, paid for yourself and your dependents. It equals roughly 2.25 kg of wheat per person; the official cash rate is announced every Ramadan (in recent years around Rs 300 per person on the wheat basis, please confirm the current rate).",
         "We collect Fitrana throughout Ramadan and distribute it, as food packages and cash, to verified deserving families before Eid day. Pay early: it lets families prepare with dignity instead of panic."],
        ["Distributed before Eid, guaranteed", "Food packages + cash to verified families", "Per-person rate updated every Ramadan"], [300, 900, 1500, 3000]))
    write("fidya.html", giving_page("fidya.html", "Fidya & Kaffarah",
        "Fasts missed through illness or old age are compensated by feeding the poor. We arrange that feeding faithfully, on your behalf.",
        ["Fidya applies when a Muslim cannot fast in Ramadan and has no realistic hope of making the fasts up, chronic illness or advanced age. The compensation: feeding one poor person two meals, or its cash value (commonly Rs 300 to 350), for every missed fast.",
         "Kaffarah applies to deliberately broken fasts and broken oaths, each with its own Shariah-prescribed sequence, feeding ten poor persons for an oath; sixty for a deliberately broken fast. Please confirm your exact case with a scholar; we will deliver the feeding precisely as prescribed."],
        ["Feeding arranged & verified locally", "Two full meals per person, as prescribed", "Scholar-guided distribution"], [350, 3500, 10500, 21000]))
    write("qurbani.html", giving_page("qurbani.html", "Qurbani",
        "Seasonal service: book your Qurbani with the Society, a Shariah-compliant sacrifice, with the meat reaching families who rarely taste it all year.",
        ["Every Eid-ul-Adha, the Society arranges collective Qurbani: healthy animals, Shariah-compliant slaughter, hygienic packing, and same-day distribution to widows, orphans, our elderly beneficiaries and poor families across Lahore.",
         "Book a full animal or a single share (hissa) in a cow. Seasonal rates are announced before Eid, message us on WhatsApp for this year's rates and booking."],
        ["Shariah-compliant slaughter", "Same-day distribution to deserving families", "Full animal or single-share options"], [25000, 45000, 180000, 250000]))
    write("get-involved.html", get_involved())
    write("donate.html", donate())
    write("media.html", media_page())
    write("blog.html", blog_page())
    for u, *_ in ARTICLES:
        write(u, article_page(u))
    write("contact.html", contact())
    # sitemap + robots
    urls = "\n".join(f"  <url><loc>{BASE}/{p}</loc><changefreq>weekly</changefreq></url>" for p in ALL_PAGES)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "\n</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    print("BUILD COMPLETE ,", len(ALL_PAGES), "pages + sitemap + robots")
