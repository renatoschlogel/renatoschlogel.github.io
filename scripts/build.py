#!/usr/bin/env python3
"""Generate the public bilingual resume using only Python's standard library."""

import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "content/resume.json").read_text(encoding="utf-8"))


def esc(value):
    return escape(str(value), quote=True)


def items(values):
    return "<ul>" + "".join(f"<li>{esc(value)}</li>" for value in values) + "</ul>"


def role(value):
    return f'<div class="role-row"><h4>{esc(value["title"])}</h4><p>{esc(value["period"])}</p></div>'


def page(locale):
    ui = locale["ui"]
    prefix = "../" if locale["path"] else "./"
    canonical = DATA["url"] + "/" + locale["path"]
    languages = []
    for code, label in (("en", "English"), ("pt-br", "Português")):
        other = DATA["locales"][code]
        current = ' aria-current="page"' if other["lang"] == locale["lang"] else ""
        languages.append(f'<a href="{prefix}{other["path"]}" lang="{other["lang"]}" hreflang="{other["lang"]}"{current}>{label}</a>')

    jobs = []
    for job in locale["experience"]:
        earlier = ""
        if "earlierRole" in job:
            earlier = '<div class="earlier-role">' + role(job["earlierRole"]) + items(job["earlierBullets"]) + "</div>"
        jobs.append(f'''<article class="job">
          <div class="company-row"><h3>{esc(job["company"])}</h3><p class="company-period">{esc(job["period"])}</p></div>
          <p class="job-context">{esc(job["context"])}</p>
          <div class="roles">{"".join(role(value) for value in job["roles"])}</div>
          {items(job["bullets"])}{earlier}
        </article>''')

    skills = "".join(f'<div class="skill-group"><h3>{esc(value["title"])}</h3><p>{esc(value["text"])}</p></div>' for value in locale["skills"])
    education = "".join(f'<article class="degree"><h3>{esc(value["degree"])}</h3><p>{esc(value["school"])}</p><p class="degree-period">{esc(value["period"])}</p></article>' for value in locale["education"])
    metrics = "".join(f'<div><dt>{esc(value["label"])}</dt><dd>{esc(value["value"])}</dd></div>' for value in locale["metrics"])
    navigation = "".join(f'<a href="#{key}">{esc(label)}</a>' for key, label in locale["nav"].items())
    schema = {
        "@context": "https://schema.org", "@type": "ProfilePage", "inLanguage": locale["lang"],
        "url": canonical, "mainEntity": {
            "@type": "Person", "name": DATA["name"], "jobTitle": locale["title"],
            "url": DATA["url"] + "/", "sameAs": [DATA["linkedin"], DATA["github"]]
        }
    }
    schema_text = json.dumps(schema, ensure_ascii=False).replace("<", "\\u003c")
    return f'''<!doctype html>
<html lang="{locale["lang"]}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light">
  <meta name="theme-color" content="#f5f4ef">
  <title>{esc(DATA["name"])} | {esc(locale["title"])}</title>
  <meta name="description" content="{esc(locale["description"])}">
  <meta property="og:type" content="profile">
  <meta property="og:title" content="{esc(DATA["name"])} | {esc(locale["title"])}">
  <meta property="og:description" content="{esc(locale["description"])}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:locale" content="{"pt_BR" if locale["lang"] == "pt-BR" else "en_US"}">
  <meta name="twitter:card" content="summary">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{DATA["url"]}/">
  <link rel="alternate" hreflang="pt-BR" href="{DATA["url"]}/pt-br/">
  <link rel="alternate" hreflang="x-default" href="{DATA["url"]}/">
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}assets/style.css">
  <script src="{prefix}assets/site.js" defer></script>
  <script type="application/ld+json">{schema_text}</script>
</head>
<body>
  <a class="skip-link" href="#main">{esc(ui["skip"])}</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{prefix}{locale["path"]}" aria-label="{esc(DATA["name"])}"><span class="monogram" aria-hidden="true">rs</span><span>Renato Schlogel</span></a>
      <nav class="section-nav" aria-label="{esc(ui["navigation"])}">{navigation}</nav>
      <nav class="language-nav" aria-label="{esc(ui["language"])}">{"".join(languages)}</nav>
    </div>
  </header>

  <main id="main" class="container" tabindex="-1">
    <section class="hero" aria-labelledby="name">
      <div class="hero-main">
        <p class="eyebrow">{esc(locale["title"])}</p>
        <h1 id="name">{esc(DATA["firstNames"])} <br><span>{esc(DATA["surname"])}</span></h1>
        <p class="specialty">{esc(locale["specialty"])}</p>
        <p class="intro">{esc(locale["summary"])}</p>
        <p class="print-contact">{esc(DATA["email"])} · renatoschlogel.github.io<br>linkedin.com/in/renato-welinton-schlogel · github.com/renatoschlogel</p>
        <div class="hero-actions">
          <a class="button button-primary" href="mailto:{esc(DATA["email"])}">{esc(ui["contact"])}<span aria-hidden="true">↗</span></a>
          <button class="button button-secondary" type="button" data-print hidden>{esc(ui["print"])}</button>
        </div>
      </div>
      <aside class="profile-panel" aria-labelledby="profile-title">
        <p id="profile-title" class="eyebrow">{esc(ui["quick"])}</p>
        <dl>
          <div><dt>{esc(ui["locationLabel"])}</dt><dd>{esc(ui["location"])}</dd></div>
          <div><dt>{esc(ui["focusLabel"])}</dt><dd>{esc(ui["focus"])}</dd></div>
          <div><dt>{esc(ui["domainsLabel"])}</dt><dd>{esc(ui["domains"])}</dd></div>
        </dl>
        <div class="profile-links"><a href="{esc(DATA["linkedin"])}">LinkedIn <span aria-hidden="true">↗</span></a><a href="{esc(DATA["github"])}">GitHub <span aria-hidden="true">↗</span></a><a class="email-link" href="mailto:{esc(DATA["email"])}">{esc(DATA["email"])}</a></div>
      </aside>
    </section>

    <dl class="metrics" aria-label="{esc(ui["profile"])}">{metrics}</dl>

    <div class="resume-grid">
      <section id="experience" class="experience" aria-labelledby="experience-title">
        <div class="section-heading"><p class="eyebrow">{esc(ui["selected"])}</p><h2 id="experience-title">{esc(locale["nav"]["experience"])}</h2></div>
        {"".join(jobs)}
      </section>

      <aside class="sidebar">
        <section id="expertise" aria-labelledby="expertise-title"><h2 id="expertise-title">{esc(ui["skills"])}</h2>{skills}</section>
        <section id="education" aria-labelledby="education-title"><h2 id="education-title">{esc(locale["nav"]["education"])}</h2>{education}</section>
        <section aria-labelledby="certification-title"><h2 id="certification-title">{esc(ui["certification"])}</h2><p class="certification">Scrum Foundation Professional Certificate (SFPC)</p></section>
      </aside>
    </div>
  </main>

  <footer class="site-footer container"><p>{esc(ui["footer"])}</p><p><time datetime="{DATA["updated"]}">{esc(ui["updated"])}</time></p></footer>
</body>
</html>
'''


def build():
    for locale in DATA["locales"].values():
        target = ROOT / locale["path"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(locale), encoding="utf-8")
        print(f"Generated {target.relative_to(ROOT)}")
    entries = []
    for locale in DATA["locales"].values():
        alternates = "".join(f'<xhtml:link rel="alternate" hreflang="{other["lang"]}" href="{DATA["url"]}/{other["path"]}"/>' for other in DATA["locales"].values())
        entries.append(f'<url><loc>{DATA["url"]}/{locale["path"]}</loc>{alternates}</url>')
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">' + "".join(entries) + '</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f'User-agent: *\nAllow: /\nSitemap: {DATA["url"]}/sitemap.xml\n', encoding="utf-8")
    (ROOT / ".nojekyll").touch()


if __name__ == "__main__":
    build()
