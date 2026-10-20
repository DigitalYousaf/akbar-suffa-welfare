# -*- coding: utf-8 -*-
"""Static site generator for Akbar Suffa Welfare Society (demo)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
V = "v=1"  # cache-bust version

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
     "Dignified burial and funeral arrangements for those who pass away with no family, no money and no one to claim them."),
    ("project-education.html", "Free Education for Underprivileged Children", "assets/img/education-1.jpg",
     "Free schooling, books and mentorship for children whose families cannot afford education."),
    ("project-elderly.html", "Financial Support for Elderly Women", "assets/img/elderly.jpg",
     "A fixed monthly stipend so elderly and widowed women can meet their basic needs with dignity."),
    ("project-oldage.html", "Old Age Care & Shelter", "assets/img/oldage.jpg",
     "Care, food and shelter for elderly people who have been left alone in their final years."),
    ("project-dastarkhwan.html", "Suffa Sasta Dastarkhwan", "assets/img/dastarkhwan.jpg",
     "Respectful, affordable meals served daily — no one in our neighbourhood should sleep hungry."),
    ("project-dispensary.html", "Suffa Free Dispensary", None,
     "Free basic medical care, check-ups and essential medicines for those who cannot afford treatment."),
]

GIVING = [
    ("zakat.html", "Zakat", "Calculate and pay your Zakat — distributed to verified deserving families."),
    ("sadaqah.html", "Sadaqah & Sadaqah Jariyah", "Give Sadaqah, or ongoing Sadaqah Jariyah for your loved ones."),
    ("fitrana.html", "Fitrana", "Pay your Fitrah before Eid so every family can celebrate."),
    ("fidya.html", "Fidya & Kaffarah", "Compensation for missed fasts and broken oaths, fed to the poor."),
    ("qurbani.html", "Qurbani", "Seasonal Qurbani with meat distributed to deserving families."),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Akbar Suffa Welfare Society, Lahore</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title} | Akbar Suffa Welfare Society">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/img/hero-janaza.jpg">
<link rel="icon" href="assets/img/logo-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?{V}">
</head>
<body>"""


def header(active=""):
    proj_items = "\n".join(f'<li><a href="{u}">{n}</a></li>' for u, n, *_ in PROJECTS)
    give_items = "\n".join(f'<li><a href="{u}">{n}</a></li>' for u, n, d in GIVING)
    return f"""
<div class="topbar"><div class="wrap">
  <div><a href="tel:+923018451152">📞 {PHONE}</a><a href="mailto:{EMAIL}">✉ {EMAIL}</a></div>
  <div class="social"><a href="{FB}" target="_blank" rel="noopener">Facebook</a><a href="{TT}" target="_blank" rel="noopener">TikTok</a><a href="{IG}" target="_blank" rel="noopener">Instagram</a></div>
</div></div>
<header class="site"><div class="wrap nav">
  <a class="brand" href="index.html"><img src="assets/img/logo-mark.png" alt="Akbar Suffa Welfare Society logo">
    <span class="bt"><b>Akbar Suffa</b><span>Welfare Society · Lahore</span></span></a>
  <button class="burger" aria-label="Open menu"><span></span><span></span><span></span></button>
  <nav class="main"><ul>
    <li><a class="nl" href="index.html">Home</a></li>
    <li><a class="nl" href="about.html">About</a></li>
    <li><a class="nl" href="projects.html">Projects ▾</a><ul class="drop">{proj_items}</ul></li>
    <li><a class="nl" href="zakat.html">Islamic Giving ▾</a><ul class="drop">{give_items}</ul></li>
    <li><a class="nl" href="get-involved.html">Get Involved</a></li>
    <li><a class="nl" href="media.html">Media</a></li>
    <li><a class="nl" href="blog.html">Blog</a></li>
    <li><a class="nl" href="contact.html">Contact</a></li>
  </ul></nav>
  <a class="btn btn-gold nav-cta" href="donate.html">Donate Now</a>
</div></header>"""


def footer():
    proj_links = "\n".join(f'<a href="{u}">{n}</a>' for u, n, *_ in PROJECTS[:4])
    return f"""
<footer class="site"><div class="wrap">
  <div class="cols">
    <div>
      <h4>Akbar Suffa Welfare Society</h4>
      <p>Serving humanity with dignity, compassion and responsibility — from Baghban Pura, Lahore. Dignified burials, free education, elderly care and daily meals for the deserving.</p>
      <p class="urdu" style="color:#ffd97a;font-size:17px;margin-top:10px">خدمتِ خلق ہی ہماری پہچان ہے</p>
    </div>
    <div><h4>Quick Links</h4>
      <a href="about.html">About Us</a><a href="projects.html">Our Projects</a>
      <a href="get-involved.html">Get Involved</a><a href="media.html">Media</a>
      <a href="blog.html">Blog</a><a href="contact.html">Contact</a></div>
    <div><h4>Our Projects</h4>{proj_links}<a href="projects.html">View All Projects</a></div>
    <div><h4>Reach Us</h4>
      <p>📍 {ADDRESS}</p><p>📞 {PHONE_INTL}</p><p>✉ {EMAIL}</p>
      <p style="margin-top:10px">UBL Bank · A/C {UBL_ACC}<br>Title: Akbar Suffa Welfare Society</p></div>
  </div>
  <div class="fbar"><span>© 2026 Akbar Suffa Welfare Society. All rights reserved.</span>
  <span>Registered welfare society · Baghban Pura, Lahore</span></div>
</div></footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
<svg viewBox="0 0 32 32"><path d="M16 3C9.4 3 4 8.3 4 14.9c0 2.6.8 5 2.3 7L4.8 28l6.3-1.4c1.5.8 3.2 1.2 4.9 1.2 6.6 0 12-5.3 12-11.9S22.6 3 16 3zm0 21.7c-1.5 0-3-.4-4.3-1.2l-.3-.2-3.3.7.7-3.2-.2-.3a9.7 9.7 0 0 1-1.5-5.2C7.1 9.9 11.1 5.9 16 5.9S24.9 9.9 24.9 14.9 20.9 24.7 16 24.7zm5.3-6.7c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1l-1 1.2c-.2.2-.4.2-.7.1a11.6 11.6 0 0 1-5.7-5c-.4-.7.5-.7 1.2-2.3.1-.3 0-.5 0-.6l-1-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.9.9-1.1 2.2-.2 3.9a20.6 20.6 0 0 0 4 4.9c1.5 1.4 2.9 2 3.9 2.2.6.1 1.2.1 1.6-.1.5-.2 1.7-.8 1.9-1.6.2-.7.2-1.3.1-1.5 0-.1-.3-.2-.6-.3z"/></svg></a>
<script src="js/main.js?{V}"></script>
</body></html>"""


def pagehero(title, sub, urdu=""):
    u = f'<p class="urdu">{urdu}</p>' if urdu else ""
    return f'<section class="pagehero"><div class="wrap">{u}<h1>{title}</h1><p>{sub}</p></div></section>'


def donate_band():
    return f"""<div class="ctaband">
  <div><h2>Your Donation Can Change a Life Today</h2>
  <p>UBL Bank · Account Title: Akbar Suffa Welfare Society · A/C {UBL_ACC}</p></div>
  <a class="btn btn-navy" href="donate.html">Donate Now</a></div>"""


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


# ============================ HOME ============================
def home():
    cards = []
    for url, name, img, desc in PROJECTS:
        media = f'<img src="{img}" alt="{name}">' if img else '<div class="icon">🩺</div>'
        cards.append(f'<article class="card">{media}<div class="body"><h3>{name}</h3><p>{desc}</p><a class="more" href="{url}">Learn more →</a></div></article>')
    cards = "\n".join(cards)
    give = "\n".join(f'<article class="card"><div class="body"><h3>{n}</h3><p>{d}</p><a class="more" href="{u}">Give now →</a></div></article>' for u, n, d in GIVING[:3])
    body = f"""
<section class="hero">
  <img class="bgimg" src="assets/img/hero-janaza.jpg" alt="Volunteers of Akbar Suffa Welfare Society offering funeral prayer">
  <div class="shade"></div>
  <div class="wrap">
    <p class="dua urdu">اِنّا لِلّٰہِ وَ اِنّا اِلَیْہِ رَاجِعُوْن</p>
    <h1>No One Should Leave This World <em>Alone</em></h1>
    <p>Akbar Suffa Welfare Society gives dignified burials to the unclaimed dead, free education to poor children, monthly support to elderly women, and a warm meal to anyone who comes hungry — in Baghban Pura, Lahore.</p>
    <div class="hero-btns"><a class="btn btn-gold" href="donate.html">Donate Now</a><a class="btn btn-white" href="projects.html">See Our Work</a></div>
  </div>
</section>
<div class="wrap"><div class="impact"><div class="grid">
  <div class="cell"><div class="num" data-count="850">0</div><div class="lbl">Dignified Burials</div></div>
  <div class="cell"><div class="num" data-count="320">0</div><div class="lbl">Students in Free Education</div></div>
  <div class="cell"><div class="num" data-count="150">0</div><div class="lbl">Elderly Women Supported Monthly</div></div>
  <div class="cell"><div class="num" data-count="45000">0</div><div class="lbl">Meals Served at Dastarkhwan</div></div>
</div></div></div>
<section class="section"><div class="wrap"><div class="split">
  <img src="assets/img/funeral-work.jpg" alt="Volunteers performing burial service">
  <div><span class="eyebrow">Who We Are</span>
    <h2>Serving Humanity With Dignity & Responsibility</h2>
    <p style="color:var(--muted);margin-top:12px">We are a community welfare society from Baghban Pura, Lahore. Our volunteers work day and night with local hospitals and police so that every person — rich or unknown — is treated with honour in life and in death.</p>
    <ul class="tick">
      <li>Dignified burial for unclaimed & destitute deceased</li>
      <li>Free education for underprivileged children</li>
      <li>Monthly stipends for elderly & widowed women</li>
      <li>Sasta Dastarkhwan — respectful, affordable daily meals</li>
    </ul>
    <p style="margin-top:20px"><a class="btn btn-outline" href="about.html">More About Us</a></p>
  </div>
</div></div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">What We Do</span><h2>Our Projects</h2>
  <p>Six ongoing projects, one mission: no one in our community should face their hardest day alone.</p></div>
  <div class="cards">{cards}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="story">
    <div><p class="urdu">آخری عزت</p>
      <h2>The Last Honour</h2>
      <p style="margin-top:12px">He had no name in the hospital register. No family came. For three days, no one claimed him. Then our volunteers arrived — they bathed him with the same care as their own father, wrapped him in a clean kafan, carried him on their own shoulders, prayed his janaza with a full congregation, and laid him to rest with a marked grave.</p>
      <p>This is what your Sadaqah does here. Every week, men and women who die unknown in Lahore are given the farewell every human being deserves.</p>
      <p style="margin-top:18px"><a class="btn btn-gold" href="project-funeral.html">About This Project</a></p>
    </div>
    <img src="assets/img/poster-funeral.jpg" alt="Funeral prayer gathering by Akbar Suffa Welfare Society">
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Islamic Giving</span><h2>Give Your Zakat, Sadaqah & Fitrana</h2>
  <p>Shariah-compliant distribution to verified, deserving recipients — with complete transparency.</p></div>
  <div class="cards">{give}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Where We Are Going</span><h2>Our Future Goals</h2></div>
  <div class="cards">
    <article class="card"><div class="body"><h3>🧵 Sewing Training Center</h3><p>A center where women and young girls learn sewing and earn a respectable income from home.</p></div></article>
    <article class="card"><div class="body"><h3>🏠 Orphan Care Center</h3><p>A safe, caring home where orphan children receive shelter, care and guidance.</p></div></article>
    <article class="card"><div class="body"><h3>📚 Primary School</h3><p>A dedicated school for orphan and poor children — quality education with hope for a brighter future.</p></div></article>
  </div>
  <div style="margin-top:44px">{donate_band()}</div>
</div></section>"""
    return head("Home", "Akbar Suffa Welfare Society, Lahore — dignified burials for the unclaimed dead, free education, elderly women support & Sasta Dastarkhwan. Donate your Zakat & Sadaqah.") + header() + body + footer()


# ============================ ABOUT ============================
def about():
    body = pagehero("About Us", "A small society with a big promise: dignity for every human being — in life and in death.", "ہمارا تعارف") + f"""
<section class="section"><div class="wrap"><div class="split">
  <img src="assets/img/education-1.jpg" alt="Student receiving an award at Suffa Educators">
  <div class="prose"><span class="eyebrow">Our Story</span>
    <h2>From One Neighbourhood, For All Humanity</h2>
    <p>Akbar Suffa Welfare Society began in Baghban Pura, Lahore, with a painful sight our founders could not unsee: bodies lying unclaimed in hospitals, and funerals that never happened because there was no one to arrange them — and no money to pay for them.</p>
    <p>So the neighbourhood decided: <b>this will not happen here.</b> Volunteers organised a burial service that treats every deceased person — known or unknown, rich or destitute — with the same honour Islam commands.</p>
    <p>From that single act of dignity, the work grew: free education for poor children, monthly stipends for elderly women who have no earner left, shelter and care for the old, a dispensary for the sick, and a Dastarkhwan where anyone can eat with respect.</p>
  </div>
</div></div></section>
<section class="section alt"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Our Mission</span><h2>What We Stand For</h2></div>
  <div class="cards">
    <article class="card"><div class="body"><h3>Dignity</h3><p>Every human being deserves honour — the orphan in class, the widow at our door, and the stranger in his final journey.</p></div></article>
    <article class="card"><div class="body"><h3>Transparency</h3><p>Your Zakat and Sadaqah are a trust (amanah). We distribute to verified deserving recipients and account for every rupee.</p></div></article>
    <article class="card"><div class="body"><h3>Compassion</h3><p>We serve without asking who someone is or where they come from. Need is the only question we ask.</p></div></article>
  </div>
  <div class="notebox" style="margin-top:34px"><b>Registered Society:</b> Akbar Suffa Welfare Society (R), Shalimar Chowk, Baghban Pura, Lahore, Pakistan. President: Malik Akbar Ali · {PHONE_INTL}</div>
</div></section>
<section class="section"><div class="wrap">{donate_band()}</div></section>"""
    return head("About Us", "The story and mission of Akbar Suffa Welfare Society — a registered community welfare society in Baghban Pura, Lahore.") + header() + body + footer()


# ============================ PROJECTS OVERVIEW ============================
def projects_page():
    cards = []
    for url, name, img, desc in PROJECTS:
        media = f'<img src="{img}" alt="{name}">' if img else '<div class="icon">🩺</div>'
        cards.append(f'<article class="card">{media}<div class="body"><h3>{name}</h3><p>{desc}</p><a class="more" href="{url}">Full details →</a></div></article>')
    body = pagehero("Our Projects", "Six projects running today in Lahore — each one answers a real cry for help in our community.", "ہمارے منصوبے") + f"""
<section class="section"><div class="wrap"><div class="cards">{''.join(cards)}</div>
<div style="margin-top:44px">{donate_band()}</div></div></section>"""
    return head("Our Projects", "Explore the six welfare projects of Akbar Suffa Welfare Society: burial support, free education, elderly care, dastarkhwan and free dispensary.") + header() + body + footer()


PROJECT_DETAILS = {
    "project-funeral.html": dict(
        title="Unclaimed Funeral Support",
        urdu="بے سہارا میتوں کی باعزت تدفین",
        img="assets/img/funeral-work.jpg",
        intro="Our signature project. When a person dies in a Lahore hospital or on its streets with no family, no money and no one to claim the body, our volunteers step in as family.",
        paras=[
            "Every week, hospitals and police stations contact us about unclaimed and destitute deceased. Without a service like ours, these bodies would face delay, indignity — or burial without rites, name or prayer.",
            "Our trained volunteer team completes the full Islamic funeral: ghusl (ritual washing) by trained washers, a clean kafan (shroud), transport, a congregational janaza prayer, and burial in a proper, marked grave — the same honour we would want for our own parents.",
            "We also support poor families who cannot afford a funeral for their own loved ones, quietly and without publicity, so grief is never added to by shame."],
        points=["Full ghusl, kafan & burial arrangements", "Coordination with hospitals & police", "Congregational janaza with our volunteers", "Free for unclaimed & destitute deceased", "Support for poor families' funerals"],
        stat=("850+", "dignified burials arranged so far")),
    "project-education.html": dict(
        title="Free Education for Underprivileged Children",
        urdu="غریب بچوں کی مفت تعلیم",
        img="assets/img/education-2.jpg",
        intro="Education is the only lasting exit from poverty. We provide free schooling and learning support to children whose families cannot afford fees, books or uniforms.",
        paras=[
            "Through Suffa Educators and partner teachers, enrolled children receive regular classes, books, stationery and mentorship — and their progress is celebrated publicly, with awards for top performers, so the whole neighbourhood sees education honoured.",
            "Parents who kept children home for work are counselled personally. Where a family's survival truly depends on it, we pair education support with monthly family assistance."],
        points=["Free classes & learning material", "Books, bags & stationery provided", "Awards & encouragement for students", "Counselling for parents", "Focus on girls' education"],
        stat=("320+", "children currently studying free")),
    "project-elderly.html": dict(
        title="Financial Support for Elderly Women",
        urdu="بزرگ خواتین کی ماہانہ کفالت",
        img="assets/img/elderly.jpg",
        intro="Many elderly and widowed women in our area have outlived their earners. A fixed monthly stipend protects their dignity — so they never have to beg for medicine, food or rent.",
        paras=[
            "Each beneficiary is verified by our local team and receives a monthly amount directly, with respect and privacy. The stipend covers essentials: food, basic medicines and household needs.",
            "Our volunteers also visit regularly — for many of these mothers, the visit matters as much as the money."],
        points=["Verified monthly stipends", "Covers food & basic medicines", "Home visits by volunteers", "Complete privacy & dignity", "Priority to widows with no earner"],
        stat=("150+", "elderly women supported every month")),
    "project-oldage.html": dict(
        title="Old Age Care & Shelter",
        urdu="بزرگوں کی دیکھ بھال اور پناہ",
        img="assets/img/oldage.jpg",
        intro="Some elderly people are left entirely alone — children gone, house empty, health failing. We arrange care, food and shelter so no elder of our community spends their last years abandoned.",
        paras=[
            "We support elderly residents with daily meals, basic medical attention through our dispensary, and safe shelter arrangements with trusted local partners.",
            "This project is the seed of our long-term goal: a dedicated orphan & elderly care home in Baghban Pura."],
        points=["Daily meals & basic care", "Shelter arrangements", "Medical support via our dispensary", "Companionship & visits"],
        stat=("40+", "elders under regular care")),
    "project-dastarkhwan.html": dict(
        title="Suffa Sasta Dastarkhwan",
        urdu="مفت و سستا دسترخوان",
        img="assets/img/dastarkhwan.jpg",
        intro="A dining spread where labourers, travellers, students and the poor sit and eat with respect — fresh, warm food at a token price, and free for anyone who cannot pay.",
        paras=[
            "Hunger removes dignity faster than anything. At Suffa Sasta Dastarkhwan, no one is turned away: those who can pay, pay a small amount; those who cannot, eat free — and nobody can tell the difference.",
            "The Dastarkhwan also serves at funerals, community events and during Ramadan iftars across Baghban Pura."],
        points=["Fresh cooked meals daily", "Free for those who cannot pay", "Open to labourers, travellers & students", "Ramadan iftar arrangements", "Sponsor a full day of meals"],
        stat=("45,000+", "meals served with dignity")),
    "project-dispensary.html": dict(
        title="Suffa Free Dispensary",
        urdu="مفت ڈسپنسری",
        img=None,
        intro="Basic healthcare should not depend on the size of a wallet. Our free dispensary provides check-ups and essential medicines to patients who would otherwise go untreated.",
        paras=[
            "Patients are examined and given essential medicines free of cost. Serious cases are guided and referred to hospitals, with our volunteers helping families navigate the process.",
            "The dispensary works hand-in-hand with our elderly care project, providing regular check-ups for the mothers and elders under our support."],
        points=["Free basic check-ups", "Essential medicines free", "Regular elderly check-ups", "Hospital referral guidance"],
        stat=("300+", "patients treated every month")),
}


def project_detail(url):
    d = PROJECT_DETAILS[url]
    media = f'<img src="{d["img"]}" alt="{d["title"]}">' if d["img"] else ""
    paras = "\n".join(f"<p>{p}</p>" for p in d["paras"])
    points = "\n".join(f"<li>{p}</li>" for p in d["points"])
    body = pagehero(d["title"], d["intro"], d["urdu"]) + f"""
<section class="section"><div class="wrap"><div class="split">
  <div>{media if media else '<div class="icon" style="font-size:110px;text-align:center">🩺</div>'}
    <div class="calc" style="margin-top:20px;text-align:center"><div class="result" style="margin:0"><span class="big">{d['stat'][0]}</span><br>{d['stat'][1]}</div></div>
  </div>
  <div class="prose"><h2>About This Project</h2>{paras}
    <h3 style="margin-top:20px">What Your Support Provides</h3>
    <ul class="tick">{points}</ul>
    <p style="margin-top:22px"><a class="btn btn-gold" href="donate.html">Donate to This Project</a> <a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">Ask on WhatsApp</a></p>
  </div>
</div>
<div style="margin-top:50px">{donate_band()}</div>
</div></section>"""
    return head(d["title"], d["intro"]) + header() + body + footer()


# ============================ ISLAMIC GIVING ============================
def giving_page(slug, title, urdu, intro, paras, points, amounts):
    paras_h = "\n".join(f"<p>{p}</p>" for p in paras)
    points_h = "\n".join(f"<li>{p}</li>" for p in points)
    amt = "\n".join(f'<button type="button" data-amt="{a}">Rs {a:,}</button>' for a in amounts)
    body = pagehero(title, intro, urdu) + f"""
<section class="section"><div class="wrap"><div class="split" style="align-items:start">
  <div class="prose"><h2>About {title}</h2>{paras_h}
    <h3 style="margin-top:18px">How We Distribute</h3>
    <ul class="tick">{points_h}</ul>
    <p style="margin-top:14px">Give through bank transfer (UBL · Akbar Suffa Welfare Society · A/C {UBL_ACC}) or use the form — our team will confirm your donation on WhatsApp.</p>
  </div>
  <form class="form demo-form" action="#" method="post">
    <h3>Give {title} Now</h3>
    <label>Your Name</label><input type="text" name="name" placeholder="Full name" required>
    <label>Mobile / WhatsApp</label><input type="tel" name="phone" placeholder="03XX-XXXXXXX" required>
    <label>Select Amount (PKR)</label>
    <div class="amounts">{amt}</div>
    <label>Or Enter Your Amount</label><input type="number" name="amount" min="10" placeholder="e.g. 5000">
    <input type="hidden" name="fund" value="{title}">
    <p style="margin-top:16px"><button class="btn btn-gold" type="submit" style="width:100%;justify-content:center">Confirm My Donation</button></p>
    <div class="thanks">JazakAllah Khair! Your intention has been noted. Our team will contact you on WhatsApp shortly to confirm the transfer details.</div>
  </form>
</div>
<div style="margin-top:50px">{donate_band()}</div>
</div></section>"""
    return head(title, intro) + header() + body + footer()


def zakat_page():
    base = giving_page("zakat", "Zakat", "زکاۃ",
        "Your Zakat is a trust. We distribute it to verified, deserving Muslim families — in cash, food and medicine — exactly as Shariah requires.",
        ["Zakat is one of the five pillars of Islam: 2.5% of your zakat-able wealth, given once a year to the poor and needy. It purifies your wealth and restores balance in society.",
         "Akbar Suffa Welfare Society maintains a verified register of deserving families in Baghban Pura and surrounding areas of Lahore — widows, orphans, the sick, and daily-wage earners in genuine need. Your Zakat reaches them directly, never spent on administration.",
         "Not sure how much Zakat you owe? Use our calculator below — it follows the gold nisab standard (7.5 tola / 87.48 grams of gold)."],
        ["100% of Zakat goes to eligible recipients", "Verified local deserving families", "No admin deduction from Zakat funds", "Distribution with dignity & privacy"],
        [2500, 5000, 10000, 25000])
    calc = f"""
<section class="section alt" style="padding-top:0"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Free Tool</span><h2>Zakat Calculator</h2>
  <p>Enter your assets in PKR. Zakat is 2.5% of total zakat-able wealth above the nisab.</p></div>
  <div class="calc" style="max-width:640px;margin:0 auto">
    <div class="form" style="border:0;box-shadow:none;padding:0">
      <label>Today's Gold Price (per tola, PKR)</label><input type="number" id="zk-gold-price" placeholder="e.g. 380000">
      <label>Cash in Hand & Bank</label><input type="number" id="zk-cash" placeholder="0">
      <label>Value of Gold You Own (PKR)</label><input type="number" id="zk-gold-val" placeholder="0">
      <label>Value of Silver You Own (PKR)</label><input type="number" id="zk-silver-val" placeholder="0">
      <label>Business Goods / Trade Assets (PKR)</label><input type="number" id="zk-business" placeholder="0">
      <label>Money You Owe Others (debts, PKR)</label><input type="number" id="zk-debts" placeholder="0">
      <p style="margin-top:18px"><button class="btn btn-navy" id="zk-btn" type="button" style="width:100%;justify-content:center">Calculate My Zakat</button></p>
    </div>
    <div class="result" id="zk-out">Your result will appear here.</div>
    <p class="small" style="margin-top:12px;text-align:center">This calculator is a guide based on the gold nisab. For personal rulings, please consult a scholar.</p>
  </div>
</div></section>"""
    # insert calculator before the closing donate band section of giving page
    return base.replace('<section class="section"><div class="wrap">', '<section class="section"><div class="wrap">', 1).replace(
        '<div style="margin-top:50px">', calc + '<div style="margin-top:50px">', 1)


# ============================ GET INVOLVED ============================
def get_involved():
    body = pagehero("Get Involved", "Money is only one way to serve. Give your time, your skill, or your monthly commitment — and become part of the work.", "شامل ہوں") + f"""
<section class="section"><div class="wrap">
  <div class="cards">
    <article class="card"><div class="body"><h3>🤝 Become a Volunteer</h3><p>Join the burial team, serve at the Dastarkhwan, teach a child, or help with media. Our volunteers are the backbone of every project.</p><a class="more" href="#volunteer">Apply below ↓</a></div></article>
    <article class="card"><div class="body"><h3>🌙 Become a Monthly Saathi</h3><p>Pledge Rs 500 or Rs 1,000 every month. Small, regular giving keeps the Dastarkhwan running and stipends paid — in every season, not only Ramadan.</p><a class="more" href="donate.html">Start monthly giving →</a></div></article>
    <article class="card"><div class="body"><h3>🎁 Sponsor</h3><p>Sponsor a student's full year of education, one complete dignified burial, or a full day of Dastarkhwan meals — in your name or for a loved one's reward.</p><a class="more" href="donate.html">See sponsorship options →</a></div></article>
  </div>
  <div class="split" style="margin-top:60px;align-items:start">
    <div class="prose"><span class="eyebrow">For Businesses & Schools</span>
      <h2>Partner With Us</h2>
      <p>Shops, companies and schools across Lahore partner with the society — placing donation boxes, sponsoring Dastarkhwan days, donating goods in kind, and engaging their students and staff in supervised volunteer work.</p>
      <ul class="tick"><li>Donation box placement at your premises</li><li>Sponsored meals & project days</li><li>CSR & student volunteer programmes</li><li>In-kind donations (food, cloth, medicines)</li></ul>
      <p style="margin-top:14px">Talk to us on <a href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a> to start.</p>
    </div>
    <form class="form demo-form" id="volunteer" action="#" method="post">
      <h3>Volunteer Application</h3>
      <label>Your Name</label><input type="text" name="name" required placeholder="Full name">
      <label>Mobile / WhatsApp</label><input type="tel" name="phone" required placeholder="03XX-XXXXXXX">
      <label>Area / Mohalla</label><input type="text" name="area" placeholder="e.g. Baghban Pura">
      <label>I Want to Help With</label>
      <select name="role"><option>Burial & funeral team</option><option>Dastarkhwan service</option><option>Teaching / education</option><option>Media & social media</option><option>Medical / dispensary</option><option>Fundraising</option><option>Other</option></select>
      <label>Anything We Should Know?</label><textarea name="msg" rows="3" placeholder="Your skills, availability..."></textarea>
      <p style="margin-top:16px"><button class="btn btn-gold" type="submit" style="width:100%;justify-content:center">Submit Application</button></p>
      <div class="thanks">Thank you! Your application has been received. Our volunteer coordinator will contact you on WhatsApp.</div>
    </form>
  </div>
</div></section>"""
    return head("Get Involved", "Volunteer, become a monthly Saathi, sponsor a project or partner with Akbar Suffa Welfare Society, Lahore.") + header() + body + footer()


# ============================ DONATE ============================
def donate():
    body = pagehero("Donate", "Every rupee is an amanah (trust). Choose your fund, pick an amount, and know exactly what it does.", "عطیہ دیں") + f"""
<section class="section"><div class="wrap">
  <div class="split" style="align-items:start">
    <div>
      <div class="bankbox"><h3>🏦 Bank Transfer</h3>
        <div class="row"><span>Bank</span><b>UBL Bank</b></div>
        <div class="row"><span>Account Title</span><b>Akbar Suffa Welfare Society</b></div>
        <div class="row"><span>Account Number</span><b>{UBL_ACC}</b></div>
        <div class="row"><span>IBAN</span><b>To be added</b></div>
        <p class="copyhint" style="margin-top:12px">After transferring, send your receipt on WhatsApp ({PHONE}) so we can issue your donation receipt.</p>
      </div>
      <div class="form" style="margin-top:22px"><h3>📱 Mobile Accounts</h3>
        <p style="color:var(--muted);font-size:15px;margin-top:8px">JazzCash and EasyPaisa account details will be added here. For now, please donate via bank transfer or contact us on WhatsApp for guidance.</p>
        <p style="margin-top:12px"><a class="btn btn-navy" href="{WA}" target="_blank" rel="noopener">WhatsApp {PHONE}</a></p>
      </div>
      <div class="notebox" style="margin-top:22px"><b>What your money does:</b><br>
      Rs 1,000 — one day of Dastarkhwan meals for the poor<br>
      Rs 3,500 — monthly stipend of one elderly mother<br>
      Rs 5,000 — one complete dignified burial (ghusl, kafan, grave)<br>
      Rs 12,000 — one child's full year of education support</div>
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
      <label style="display:flex;gap:10px;align-items:center;font-weight:600"><input type="checkbox" name="monthly" style="width:auto"> Make this a monthly donation (Monthly Saathi)</label>
      <p style="margin-top:16px"><button class="btn btn-gold" type="submit" style="width:100%;justify-content:center">Confirm My Donation</button></p>
      <div class="thanks">JazakAllah Khair! Your donation intention is noted. Our team will WhatsApp you the transfer confirmation and your receipt.</div>
    </form>
  </div>
</div></section>"""
    return head("Donate", "Donate your Zakat, Sadaqah or general charity to Akbar Suffa Welfare Society — UBL account, verified projects, complete transparency.") + header() + body + footer()


# ============================ MEDIA ============================
def media_page():
    tt_videos = [
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7593776403967905045", "Field Work in the Community"),
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7646679219174427911", "Serving the Deserving"),
        ("https://www.tiktok.com/@akbarsuffawelfaresociety/video/7625693484179131666", "Our Volunteers in Action"),
    ]
    vids = "\n".join(f'<article class="vcard"><div class="vbody"><h3>{t}</h3><p>Watch this video from our field work on TikTok.</p><p style="margin-top:10px"><a class="btn btn-outline" href="{u}" target="_blank" rel="noopener">▶ Watch Video</a></p></div></article>' for u, t in tt_videos)
    body = pagehero("Media & Stories", "Real work, real people, real change — from the streets and mohallas of Lahore.", "میڈیا") + f"""
<section class="section"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Gallery</span><h2>From the Field</h2></div>
  <div class="gallery">
    <img src="assets/img/hero-janaza.jpg" alt="Janaza prayer gathering">
    <img src="assets/img/funeral-work.jpg" alt="Volunteers at burial service">
    <img src="assets/img/education-1.jpg" alt="Student award ceremony">
    <img src="assets/img/education-2.jpg" alt="Student receiving trophy">
    <img src="assets/img/dastarkhwan.jpg" alt="Dastarkhwan meal service">
    <img src="assets/img/elderly.jpg" alt="Elderly women support">
  </div>
  <div class="sec-head" style="margin-top:70px"><span class="eyebrow">Videos</span><h2>Watch Our Work</h2>
  <p>Follow our daily work on TikTok, Facebook and Instagram — and share it so the message of dignity reaches further.</p></div>
  <div class="videos">{vids}</div>
  <div class="story" style="margin-top:60px">
    <div><p class="urdu">کہانیاں</p><h2>A Grave With a Name</h2>
      <p style="margin-top:10px">Last winter, an elderly man was found deceased near Shalimar. No ID, no phone, no family traced for days. Our team completed his ghusl and janaza, and — with the help of a neighbour who finally recognised him — his grave was marked with his real name. A name matters. It is the difference between being forgotten and being remembered in people's duas.</p>
      <p>Stories like his are why we exist — and why your support must never stop.</p></div>
    <img src="assets/img/poster-dastarkhwan.jpg" alt="Suffa Sasta Dastarkhwan poster">
  </div>
</div></section>"""
    return head("Media & Stories", "Photos, videos and real stories from the field work of Akbar Suffa Welfare Society, Lahore.") + header() + body + footer()


# ============================ BLOG ============================
ARTICLES = [
    ("blog-zakat-guide.html", "Zakat in Pakistan: A Simple Complete Guide", "Who must pay Zakat, what wealth it applies to, the nisab explained simply — and how to make sure your Zakat reaches the truly deserving.", "Zakat Guide"),
    ("blog-akhri-izzat.html", "Aakhri Izzat: Why Every Deceased Person Deserves a Dignified Farewell", "What happens to unclaimed bodies in a big city — and how a small team in Baghban Pura is changing that, one janaza at a time.", "Our Story"),
    ("blog-fitrana-guide.html", "Fitrana 2026: Rates, Rules and Who Receives It", "What Fitrana is, when to pay it, the per-person rate — and how your Fitrah puts an Eid meal on a poor family's table.", "Ramadan Guide"),
]


def blog_page():
    cards = "\n".join(f'<article class="card"><div class="body"><span class="badge">{tag}</span><h3>{t}</h3><p>{d}</p><a class="more" href="{u}">Read article →</a></div></article>' for u, t, d, tag in ARTICLES)
    body = pagehero("Blog", "Guidance on Islamic giving, and stories from our work in Lahore.", "بلاگ") + f"""
<section class="section"><div class="wrap"><div class="cards">{cards}</div></div></section>"""
    return head("Blog", "Zakat guides, Ramadan guidance and real stories from Akbar Suffa Welfare Society, Lahore.") + header() + body + footer()


def article_page(url):
    data = {u: (t, d, tag) for u, t, d, tag in ARTICLES}
    t, d, tag = data[url]
    if "zakat-guide" in url:
        paras = [
            "Zakat is the third pillar of Islam — an obligatory charity of 2.5% on your zakat-able wealth, paid once a lunar year. It is not a favour to the poor; it is their right (haqq) in your wealth.",
            "<b>Who must pay?</b> Every adult Muslim who owns wealth equal to or above the nisab for a full lunar year. The nisab is 87.48 grams of gold (7.5 tola) — or its cash equivalent. Use our free Zakat Calculator on the Zakat page to check your amount in minutes.",
            "<b>What wealth counts?</b> Cash in hand and bank, gold and silver, and goods bought for resale/business. Your home, car and personal items do not count. Debts you owe are deducted first.",
            "<b>Who can receive it?</b> The Quran (Surah At-Tawbah, 9:60) lists the categories — first among them the poor (fuqara) and the needy (masakin). Zakat cannot be given to your parents, spouse or children, and it should not fund buildings or administration.",
            "<b>How we distribute:</b> the Society keeps a verified register of deserving families — widows, orphans, the sick and struggling daily-wage earners. 100% of your Zakat reaches eligible recipients, with no admin deduction."]
        cta = ("zakat.html", "Calculate & Pay Your Zakat")
    elif "akhri-izzat" in url:
        paras = [
            "Every week in Lahore, people die unknown. An accident victim with no ID. An elderly labourer far from his village. A patient in a public hospital whose family cannot be traced. Their bodies wait in mortuaries — and without someone to claim them, their final journey can be delayed, undignified, or completed without the rites every Muslim deserves.",
            "Islam honours the dead as it honours the living. Washing (ghusl), shrouding (kafan), the funeral prayer (janaza) and a proper grave are not optional extras — they are the rights of every deceased Muslim, rich or poor, known or unknown.",
            "This is the work Akbar Suffa Welfare Society was founded for. Our volunteers coordinate with hospitals and police, complete every rite with trained hands, gather a congregation for janaza, and bury each person in a proper grave. For the poor families who simply cannot afford a funeral, we quietly cover the cost — so grief is never mixed with shame.",
            "It costs around Rs 5,000 to give one person a complete, dignified farewell. As Sadaqah Jariyah for your own parents, there are few gifts more meaningful."]
        cta = ("project-funeral.html", "See the Funeral Support Project")
    else:
        paras = [
            "Fitrana (Sadaqat-ul-Fitr) is the charity every Muslim pays before Eid-ul-Fitr prayers, so that the poor can also eat, dress and celebrate on Eid day. It is obligatory on every Muslim who has food beyond one day's need — paid for yourself and your dependents.",
            "<b>How much?</b> Fitrana equals the value of about 2.25 kg of wheat (or its equivalent in dates, barley or raisins) per person. Scholars announce the cash rate every Ramadan according to market prices — for 2026 the commonly announced rate is around Rs 300 per person (wheat basis). Please confirm the current year's rate from your local scholars when Ramadan begins.",
            "<b>When to pay?</b> Any time in Ramadan, but ideally before Eid prayer — the earlier the better, so families can prepare for Eid. The Society distributes Fitrana as food and cash support to verified deserving families before Eid.",
            "<b>Who receives it?</b> The same deserving categories as Zakat — the poor and needy. Pay yours on our Fitrana page and we will deliver it before Eid, in sha Allah."]
        cta = ("fitrana.html", "Pay Your Fitrana")
    paras_h = "\n".join(f"<p>{p}</p>" for p in paras)
    body = pagehero(t, d) + f"""
<section class="section"><div class="wrap" style="max-width:820px">
  <article class="prose">{paras_h}</article>
  <p style="margin-top:26px"><a class="btn btn-gold" href="{cta[0]}">{cta[1]}</a> <a class="btn btn-outline" href="blog.html">← All Articles</a></p>
</div></section>"""
    return head(t, d) + header() + body + footer()


# ============================ CONTACT ============================
def contact():
    body = pagehero("Contact Us", "Visit us, call us, or message on WhatsApp — we reply personally.", "رابطہ") + f"""
<section class="section"><div class="wrap"><div class="split" style="align-items:start">
  <div class="prose">
    <h2>Reach the Society</h2>
    <p><b>📍 Address:</b> {ADDRESS}</p>
    <p><b>📞 Phone / WhatsApp:</b> {PHONE_INTL}</p>
    <p><b>✉ Email:</b> {EMAIL}</p>
    <p><b>President:</b> Malik Akbar Ali</p>
    <p style="margin-top:14px">For urgent funeral support, call or WhatsApp any time — our volunteer team responds day and night.</p>
    <p style="margin-top:14px"><a class="btn btn-navy" href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></p>
    <div style="margin-top:24px;border-radius:12px;overflow:hidden;border:1px solid var(--line)">
      <iframe title="Map — Baghban Pura, Lahore" src="https://www.google.com/maps?q=Baghbanpura,+Lahore,+Pakistan&output=embed" style="width:100%;height:300px;border:0" loading="lazy"></iframe>
    </div>
  </div>
  <form class="form demo-form" action="#" method="post">
    <h3>Send a Message</h3>
    <label>Your Name</label><input type="text" name="name" required placeholder="Full name">
    <label>Email or Phone</label><input type="text" name="contact" required placeholder="How can we reply?">
    <label>Subject</label>
    <select name="subject"><option>General question</option><option>Donation</option><option>Funeral support (urgent)</option><option>Volunteer</option><option>Help request</option><option>Other</option></select>
    <label>Message</label><textarea name="msg" rows="5" required placeholder="Write your message..."></textarea>
    <p style="margin-top:16px"><button class="btn btn-gold" type="submit" style="width:100%;justify-content:center">Send Message</button></p>
    <div class="thanks">Thank you! Your message has been received. We will reply soon, in sha Allah.</div>
  </form>
</div></div></section>"""
    return head("Contact Us", "Contact Akbar Suffa Welfare Society, Shalimar Chowk, Baghban Pura, Lahore. Phone & WhatsApp 0301-8451152.") + header() + body + footer()


# ============================ BUILD ALL ============================
if __name__ == "__main__":
    write("index.html", home())
    write("about.html", about())
    write("projects.html", projects_page())
    for url, *_ in PROJECTS:
        write(url, project_detail(url))
    write("zakat.html", zakat_page())
    write("sadaqah.html", giving_page("sadaqah", "Sadaqah & Sadaqah Jariyah", "صدقہ",
        "Sadaqah opens doors rizq and protection. Sadaqah Jariyah — ongoing charity — keeps rewarding you and your loved ones even after death.",
        ["The Prophet ﷺ said: 'When a person dies, his deeds end except three: ongoing charity (Sadaqah Jariyah), beneficial knowledge, or a righteous child who prays for him.' (Muslim)",
         "Give Sadaqah for your own protection and blessings — or Sadaqah Jariyah on behalf of your parents and departed loved ones. The most beloved Jariyah projects here: sponsoring a dignified burial, funding a student's education, or feeding people daily at the Dastarkhwan — deeds whose reward repeats every single day."],
        ["Distributed as food, medicine, burials & education", "Can be given for living or deceased loved ones", "Jariyah projects repeat reward daily"], [1000, 3500, 5000, 12000]))
    write("fitrana.html", giving_page("fitrana", "Fitrana (Sadaqat-ul-Fitr)", "فطرانہ",
        "Pay your Fitrana before Eid prayer so that no deserving family in Lahore is left out of Eid's happiness.",
        ["Fitrana is obligatory on every Muslim with food beyond a day's need — for yourself and your dependents. It equals roughly 2.25 kg of wheat per person; the cash rate is announced each Ramadan (around Rs 300 per person on the wheat basis — please confirm the current rate).",
         "The Society collects Fitrana throughout Ramadan and distributes it — as food packages and cash — to verified deserving families before Eid day."],
        ["Distributed before Eid, guaranteed", "Food packages + cash to verified families", "Per-person rate updated every Ramadan"], [300, 900, 1500, 3000]))
    write("fidya.html", giving_page("fidya", "Fidya & Kaffarah", "فدیہ و کفارہ",
        "Missed fasts due to illness or old age? Fidya feeds a poor person for each missed fast. Kaffarah expiates broken oaths and major violations.",
        ["Fidya applies when a person cannot fast in Ramadan and has no hope of making the fasts up (chronic illness, old age): feeding one poor person two meals — or its cash value (commonly Rs 300–350) — for each missed fast.",
         "Kaffarah applies to deliberately broken fasts, broken oaths and certain violations, with its own Shariah-prescribed sequence — feeding ten poor persons for an oath, sixty for a deliberately broken fast. Please consult a scholar for your exact case; we will faithfully deliver the feeding on your behalf."],
        ["Feeding arranged & verified locally", "Two meals per person, as prescribed", "Scholar-guided distribution"], [350, 3500, 10500, 21000]))
    write("qurbani.html", giving_page("qurbani", "Qurbani", "قربانی",
        "Seasonal: book your Qurbani share with the Society — sacrifice performed to Shariah standards, meat distributed to deserving families across Lahore.",
        ["Every Eid-ul-Adha, the Society arranges collective Qurbani: healthy animals, Shariah-compliant slaughter, and hygienic meat packing — distributed the same day to widows, orphans, elderly beneficiaries and poor families who rarely eat meat all year.",
         "Book a full animal or a share (hissa) in a cow. Rates are announced before Eid each year — contact us on WhatsApp for this season's rates and booking."],
        ["Shariah-compliant slaughter", "Same-day distribution to deserving families", "Full animal or single share options"], [25000, 45000, 180000, 250000]))
    write("get-involved.html", get_involved())
    write("donate.html", donate())
    write("media.html", media_page())
    write("blog.html", blog_page())
    for u, *_ in ARTICLES:
        write(u, article_page(u))
    write("contact.html", contact())
    print("BUILD COMPLETE")
