"""Generates the static site (index.html, one page per project, 404.html).

Run from anywhere:  python _build/build.py
All content lives in the CONFIG / PROJECTS sections below.
"""
import os
from html import escape as e
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG = os.path.join(ROOT, "img")

# ------------------------------------------------------------------ CONFIG
NAME = "Yelyzaveta Zalizko"
ROLE = "Illustrator / Designer"
OPEN_TO_WORK = "Open to full-time roles"     # set to "" to hide the badge
EMAIL = "zalizkoliza01@gmail.com"
INSTAGRAM = "erizabesuli"
PHONE = ""                  # add a number here and set SHOW_PHONE = True to list it on the contact section
SHOW_PHONE = False
LINKEDIN = ""               # e.g. "https://www.linkedin.com/in/your-name/"  (shown when set)
BEHANCE = ""                # e.g. "https://www.behance.net/your-name"        (shown when set)
RESUME = ""                 # e.g. "Yelyzaveta-Zalizko-CV.pdf" (put the file in the site folder; adds a button)
SITE_DESC = ("Portfolio of Yelyzaveta Zalizko, illustrator and designer: packaging, book covers, "
             "character art, tarot cards and pattern design. Open to full-time roles.")

# ---------------------------------------------------------------- PROJECTS
# layouts: lead | feature | row3 | grid2 | masonry | cards | process
PROJECTS = [
    dict(
        slug="packaging", num="01", title="Packaging illustration", years="2024 – 2025",
        card=dict(img="soap-trio", fit="contain", tint="#f8f9fa", pos="center"),
        lede=("Illustrated packaging with a story: a gentle floral soap range and a playful craft-beer "
              "label series, each designed as a cohesive set."),
        groups=[
            dict(title="Botaniqué", years="2024 – 2025", layout="lead",
                 text=("“Botaniqué – Vegan Floral Soap Collection”: a gentle, eco-conscious collection inspired by "
                       "nature’s most loved flowers. Each soap highlights a unique floral scent and is free from "
                       "animal products, palm oil, and artificial colors."),
                 items=[("soap-trio", "Three Botaniqué soap boxes stacked together, each with an illustrated woman among flowers")]),
            dict(title="Tanuki Tap", years="2024", layout="row3", tint="#f6f8f9",
                 text=("“Tanuki Tap”: a playful and modern craft beer label series inspired by Japanese folklore and "
                       "the whimsical spirit of the tanuki. The goal was a cohesive identity across three unique ale "
                       "flavors, blending traditional Japanese folklore with a modern look."),
                 items=[("can-golden", "Tanuki Tap “Golden Paws” beer can with hop illustrations"),
                        ("can-moonlit", "Tanuki Tap “Moonlit Berry” beer can with blueberry illustrations"),
                        ("can-ruby", "Tanuki Tap “Ruby Trickster” beer can with cherry illustrations")]),
        ],
    ),
    dict(
        slug="book-covers", num="02", title="Book covers", years="2023 – 2025",
        card=dict(img="moon-closed", fit="cover", tint="#dfe1e6", pos="center"),
        lede="Cover and interior illustration for a bedtime story and a hand-drawn recipe book.",
        groups=[
            dict(title="The Moon Who Lost Her Light", years="2023 – 2025", layout="feature",
                 text=("A gentle story about the moon who loses her light and sets off on a journey to find it. Along "
                       "the way, she meets night creatures who help her discover the strength within. Soft, dreamlike "
                       "illustrations and poetic narration make it perfect for children, and soothing for adults, too. "
                       "It’s a story about healing, hope, and finding light in unexpected places."),
                 items=[("moon-open", "Open hardcover of The Moon Who Lost Her Light showing the front cover, spine and back cover"),
                        ("moon-closed", "Closed hardcover with a sleepy moon surrounded by an owl, fox, rabbit and raccoon"),
                        ("moon-spreads", "Interior spreads of the picture book: the moon, an owl, a fox and a raccoon in a night forest")]),
            dict(title="The Witch’s Pantry", years="2024", layout="feature",
                 text=("“The Witch’s Pantry”: a hand-drawn recipe book filled with potions, elixirs, and edible spells. "
                       "Each page blends cozy kitchen magic with a touch of folklore and whimsy. Thematic chapters guide "
                       "readers through charming, enchanted recipes inspired by herbs, nature, and old-world witchcraft. "
                       "Part cookbook, part spellbook, perfect for anyone who loves a little magic in their meals."),
                 items=[("witch-cover", "Cover of The Witch’s Pantry: a witch stirring a cauldron surrounded by potion bottles"),
                        ("witch-popcorn", "Recipe spread for Dragon’s Breath Popcorn with an illustrated cauldron"),
                        ("witch-focaccia", "Recipe spread for Lunar Herb Focaccia with an illustrated loaf"),
                        ("witch-cake", "Recipe spread for Black Forest Familiar Cake with an illustrated cake")]),
        ],
    ),
    dict(
        slug="tattoo-art", num="03", title="Tattoo art", years="2020 – 2025",
        card=dict(img="tattoo-dragon", fit="contain", tint="#ffffff", pos="center"),
        lede=("Unique, personalized tattoo designs that tell a story and resonate with each client."),
        groups=[
            dict(title="", years="", layout="lead",
                 text=("I’m passionate about creating unique and personalized tattoo designs that tell a story and "
                       "resonate with my clients. Since 2021, I’ve been working on Fiverr, collaborating with "
                       "individuals from around the world to bring their tattoo ideas to life. Each design in my "
                       "portfolio is a testament to my dedication to creating meaningful and visually stunning "
                       "tattoos tailored to my clients’ preferences."),
                 items=[("tattoo-dragon", "Black and grey tattoo design of a dragon and a serpent among stylised clouds")]),
            dict(title="More designs", years="", layout="masonry",
                 items=[("tattoo-samurai", "Line-art design of a samurai helmet and peony flowers"),
                        ("tattoo-dragon2", "Vertical tattoo design of a slender Eastern dragon"),
                        ("tattoo-mecha", "Line-art design of a mechanical penguin against geometric shapes"),
                        ("tattoo-skeleton", "Line-art skeleton in a boxing stance"),
                        ("tattoo-owl", "Mechanical owl with clockwork and gears"),
                        ("tattoo-trex", "Stippled illustration of a T. rex skull")]),
        ],
    ),
    dict(
        slug="portraits", num="04", title="Hand-drawn portraits", years="2018 – 2022",
        card=dict(img="portrait-rm", fit="cover", tint="#e8e1d8", pos="center 35%"),
        lede=("While I adore digital art, there’s something special about returning to traditional drawing with "
              "pencil and paper. It’s a nostalgic experience that allows me to reconnect with the raw essence of "
              "creating art."),
        groups=[
            dict(title="", years="", layout="grid2",
                 items=[("portrait-jin", "Pencil portrait of a man in a suit and tie in a sketchbook"),
                        ("portrait-jk", "Pencil portrait of a young man in a collared jacket"),
                        ("portrait-suga", "Pencil sketch of a man in traditional dress with a dragon behind him"),
                        ("portrait-rm", "Graphite portrait of a man resting his chin on his hand")]),
        ],
    ),
    dict(
        slug="personal-art", num="05", title="Personal art", years="2020 – 2025",
        card=dict(img="art-couple", fit="cover", tint="#1a1a1f", pos="center 30%"),
        lede=("A collection of self-initiated works that reflect my creative exploration and personal interests. "
              "These pieces allow me to experiment with style, technique, and storytelling beyond client work. "
              "They represent moments of inspiration, curiosity, and growth."),
        groups=[
            dict(title="", years="", layout="masonry",
                 items=[("art-couple", "Digital illustration of a blonde woman embraced by a hooded figure"),
                        ("art-beacon", "Three kids standing under a “Beacon Pines” sign", "Beacon Pines"),
                        ("art-jinx", "Digital illustration of a laughing blue-haired character among paint splatters"),
                        ("art-rabbit", "A boy and a rabbit-headed man in a suit exchanging a book in a dark alley"),
                        ("art-ninja", "Character illustration of a masked ninja with a katana")]),
        ],
    ),
    dict(
        slug="pattern-design", num="06", title="Pattern design", years="Process",
        card=dict(img="pat-hat", fit="contain", tint="#f7f1ec", pos="center"),
        lede=("From a single hand-drawn floral motif to a seamless repeat, then applied to products."),
        groups=[
            dict(title="From motif to repeat", years="", layout="process",
                 items=[("pat-motif", "Hand-drawn pink and gold floral motif", "Motif"),
                        ("pat-tile", "Pattern tile built from the motif", "Tile"),
                        ("pat-repeat", "Seamless floral repeat pattern", "Repeat")]),
            dict(title="On products", years="", layout="grid2",
                 items=[("pat-hat", "Bucket hat with the pink and gold floral pattern"),
                        ("pat-tote", "Tote bag with the pink and gold floral pattern")]),
        ],
    ),
    dict(
        slug="tarot", num="07", title="Tarot cards", years="2023 – 2025", dark=True,
        card=dict(img="tarot-stack", fit="cover", tint="#161616", pos="center 45%"),
        lede=("Welcome to my tarot card collection, where dark tones meet mysticism. Each card delves into the "
              "subconscious, offering insights found in shadows. Perfect for meditation, divination, or art, "
              "these cards reveal the mysteries of the soul."),
        groups=[
            dict(title="The Hollow Arcana", years="Stories told in shadow and line", layout="feature",
                 items=[("tarot-stack", "A stack of tarot cards with the Judgement card on top"),
                        ("tarot-box", "The Hollow Arcana tarot box with a hooded figure holding a glowing star"),
                        ("tarot-flat", "Tarot cards laid out in a grid")]),
            dict(title="The cards", years="", layout="cards",
                 items=[("card-star", "The Star tarot card"), ("card-moon", "The Moon tarot card"),
                        ("card-judgement", "Judgement tarot card"), ("card-lovers", "The Lovers tarot card"),
                        ("card-world", "The World tarot card"), ("card-sun", "The Sun tarot card"),
                        ("card-magician", "The Magician tarot card")]),
        ],
    ),
]

# Display order (change this list to reorder the site). Numbers 01-07 follow it automatically.
ORDER = ["packaging", "pattern-design", "book-covers", "tattoo-art", "tarot", "personal-art", "portraits"]
PROJECTS.sort(key=lambda p: ORDER.index(p["slug"]))
for _i, _p in enumerate(PROJECTS, 1):
    _p["num"] = f"{_i:02d}"

SERVICES = ["Packaging illustration", "Book covers", "Tattoo design", "Character art",
            "Pattern design", "Hand-drawn portraits"]

# ---------------------------------------------------------------- HELPERS
_size_cache = {}


def size(name):
    if name not in _size_cache:
        with Image.open(os.path.join(IMG, f"{name}-t.webp")) as im:
            _size_cache[name] = im.size
    return _size_cache[name]


def img_tag(name, alt, lazy=True, cls=""):
    w, h = size(name)
    return (f'<img src="img/{name}-t.webp" width="{w}" height="{h}" alt="{e(alt)}"'
            f'{" loading=\"lazy\" decoding=\"async\"" if lazy else ""}{f" class=\"{cls}\"" if cls else ""}>')


def fig(item, plain=False, show_caption=True):
    name, alt = item[0], item[1]
    cap = item[2] if len(item) > 2 else ""
    figcap = f"<figcaption>{e(cap)}</figcaption>" if cap and show_caption and not plain else ""
    return (f'<figure class="fig reveal{" plain" if plain else ""}">'
            f'<a href="img/{name}-f.webp" data-full="img/{name}-f.webp" data-caption="{e(cap or alt)}">'
            f'{img_tag(name, alt)}</a>{figcap}</figure>')


STAR = ('<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 2c2.6 16.6 13.4 27.4 30 30-16.6 2.6-27.4 '
        '13.4-30 30C29.4 45.4 18.6 34.6 2 32 18.6 29.4 29.4 18.6 32 2z" fill="#e8b457"/></svg>')


def head(title, desc, body_cls="", extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#fcfbf9">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Cormorant+Garamond:wght@500;600;700&family=Gloock&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{extra}</head>
<body{f' class="{body_cls}"' if body_cls else ""}>
<a class="skip" href="#main">Skip to content</a>
<header class="nav">
  <div class="wrap">
    <a class="brand" href="index.html">{STAR}<span>{e(NAME)}</span></a>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span></button>
    <ul class="menu">
      <li><a href="index.html#work">Work</a></li>
      <li><a href="index.html#about">About</a></li>
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
  </div>
</header>
<main id="main">
"""


def foot():
    return f"""</main>
<footer class="foot">
  <div class="wrap">
    <span>© 2026 {e(NAME)}</span>
    <span><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.instagram.com/{INSTAGRAM}/" rel="noopener">@{INSTAGRAM}</a></span>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""


def contact_block():
    rows = [f'<li><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></li>',
            f'<li><b>Instagram</b><a href="https://www.instagram.com/{INSTAGRAM}/" rel="noopener">@{INSTAGRAM}</a></li>']
    if LINKEDIN:
        rows.append(f'<li><b>LinkedIn</b><a href="{LINKEDIN}" rel="noopener">{LINKEDIN.split("//")[-1].rstrip("/")}</a></li>')
    if BEHANCE:
        rows.append(f'<li><b>Behance</b><a href="{BEHANCE}" rel="noopener">{BEHANCE.split("//")[-1].rstrip("/")}</a></li>')
    cv_btn = f'<a class="btn ghost" href="{RESUME}" download>Download CV</a>' if RESUME else ""
    if SHOW_PHONE and PHONE:
        rows.append(f'<li><b>Phone</b><a href="tel:{PHONE.replace(" ", "").replace("(", "").replace(")", "").replace("-", "")}">{PHONE}</a></li>')
    return f"""<section class="contact" id="contact">
  <img class="swirl" src="img/brush-t.webp" alt="" aria-hidden="true" loading="lazy">
  <div class="wrap reveal">
    <h2>Thank you,<br>let’s work together!</h2>
    <p class="sub">{"I’m looking for a full-time role. If my work fits your team, I’d love to hear from you." if OPEN_TO_WORK else "I’d love to hear about your project."}</p>
    <ul class="contact-list">
      {"".join(rows)}
    </ul>
    <div class="btns"><a class="btn" href="mailto:{EMAIL}?subject=Opportunity%20for%20{NAME.replace(' ', '%20')}">Send an email</a>{cv_btn}</div>
  </div>
</section>
"""


# ------------------------------------------------------------------ PAGES
def build_index():
    cards = []
    for i, p in enumerate(PROJECTS):
        c = p["card"]
        wide = " half" if i in (0, 1, 5, 6) else ""      # layout rows: 2 large, 3 medium, 2 large
        cards.append(f"""    <a class="card reveal{wide}" href="{p['slug']}.html" style="--tint:{c['tint']};--fit:{c['fit']};--pos:{c['pos']}">
      <div class="pic">{img_tag(c['img'], '', lazy=i > 1)}</div>
      <div class="info"><span class="num">{p['num']}</span><div><h3>{e(p['title'])}</h3><span class="yrs">{e(p['years'])}</span></div><span class="arrow" aria-hidden="true">→</span></div>
    </a>""")

    chips = "".join(f"<li>{e(s)}</li>" for s in SERVICES)
    html = head(f"{NAME} · {ROLE}", SITE_DESC)
    html += f"""<section class="hero">
  <img class="swirl" src="img/brush-t.webp" alt="" aria-hidden="true">
  <div class="wrap">
    <div class="hero-art"><img src="img/hero-portrait-t.webp" width="{size('hero-portrait')[0]}" height="{size('hero-portrait')[1]}" alt="Illustrated self-portrait of Yelyzaveta holding a pencil"></div>
    <div>
      <p class="eyebrow">{e(ROLE)}</p>
      <h1>{e(NAME.split()[0])}<br>{e(NAME.split()[1])} <em>2026</em></h1>
      <p class="lede">Illustration for packaging, books, characters and tarot, full of detail, folklore and a little magic.</p>
      {f'<p class="badge"><i aria-hidden="true"></i>{e(OPEN_TO_WORK)}</p>' if OPEN_TO_WORK else ""}
      <div class="btns"><a class="btn" href="#work">View my work</a><a class="btn ghost" href="#contact">Get in touch</a></div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap">
    <div class="sec-head"><h2>Selected work</h2></div>
    <div class="cards">
{chr(10).join(cards)}
    </div>
  </div>
</section>

<section class="about" id="about">
  <div class="wrap">
    <div class="reveal">
      <div class="sec-head"><h2>About</h2></div>
      <p>I’m an illustrator and designer creating packaging, book covers, characters, tarot cards, patterns and custom tattoo designs.</p>
      <p>Since 2021 I’ve collaborated with clients from around the world on Fiverr, bringing their ideas to life. I’m now looking for a full-time role where I can grow with a team, and I still love returning to pencil and paper for the raw essence of creating art.</p>
    </div>
    <div class="reveal">
      <h3>What I do</h3>
      <ul class="chips">{chips}</ul>
    </div>
  </div>
</section>

{contact_block()}"""
    html += foot()
    return html


def build_group(g):
    layout = g["layout"]
    items = g["items"]
    head_html = ""
    if g.get("title") or g.get("text"):
        t = ""
        if g.get("title"):
            y = f'<span class="gy">{e(g["years"])}</span>' if g.get("years") else ""
            t = f"<h2>{e(g['title'])}{y}</h2>"
        txt = f"<p>{e(g['text'])}</p>" if g.get("text") else ""
        head_html = f'<div class="ghead reveal">{t}{txt}</div>'
    style = f' style="--tint:{g["tint"]}"' if g.get("tint") else ""
    if layout == "process":
        parts = []
        for k, it in enumerate(items):
            if k:
                parts.append('<div class="arr" aria-hidden="true">→</div>')
            parts.append(f'<div class="step">{fig(it, show_caption=False)}<span>{e(it[2])}</span></div>')
        body = f'<div class="process">{"".join(parts)}</div>'
    else:
        plain = layout == "cards"
        css_class = "deck" if layout == "cards" else layout   # ".cards" is the home-page grid
        body = f'<div class="{css_class}"{style}>{"".join(fig(it, plain=plain) for it in items)}</div>'
        if layout == "lead":
            body = f'<div class="lead">{"".join(fig(it) for it in items)}</div>'
    return f'<section class="group"><div class="wrap">{head_html}{body}</div></section>'


def build_project(i):
    p = PROJECTS[i]
    prev_p = PROJECTS[i - 1] if i > 0 else None
    next_p = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None
    html = head(f"{p['title']} · {NAME}", f"{p['title']} by {NAME}. {p['lede']}", "dark" if p.get("dark") else "")
    html += f"""<header class="phead">
  <div class="ring" aria-hidden="true"><span>{p['num']}.</span></div>
  <div class="wrap">
    <div>
      <a class="back" href="index.html#work">← All work</a>
      <h1>{e(p['title'])}</h1>
      <p class="years">{e(p['years'])}</p>
      <div class="rule"></div>
      <p class="lede">{e(p['lede'])}</p>
    </div>
  </div>
</header>
"""
    html += "\n".join(build_group(g) for g in p["groups"])
    pager = ""
    if prev_p:
        pager += f'<a href="{prev_p["slug"]}.html"><small>← Previous</small><strong>{e(prev_p["title"])}</strong></a>'
    if next_p:
        pager += f'<a href="{next_p["slug"]}.html"><small>Next →</small><strong>{e(next_p["title"])}</strong></a>'
    html += f'<div class="wrap"><nav class="pager" aria-label="Project navigation">{pager}</nav></div>\n'
    html += contact_block()
    html += foot()
    return html


def build_404():
    html = head(f"Page not found · {NAME}", SITE_DESC)
    html += """<div class="nf"><div><h1>404</h1><p>This page wandered off. Let’s get you back.</p>
<p><a class="btn" href="index.html">Back to the portfolio</a></p></div></div>
"""
    html += foot()
    return html


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("wrote", name)


if __name__ == "__main__":
    write("index.html", build_index())
    for i, p in enumerate(PROJECTS):
        write(f"{p['slug']}.html", build_project(i))
    write("404.html", build_404())

