"""Generate crawlable PL/EN pages with Python's standard library."""

import json
import hashlib
from html import escape
from pathlib import Path
from string import Template
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://nut-software.pl"


def build():
    translations = json.loads((ROOT / "content/translations.json").read_text())
    template = Template((ROOT / "templates/page.html.tmpl").read_text())
    organization = {
        "@type": "Organization", "@id": BASE + "/#organization",
        "name": "Nut Software", "legalName": "Nut Software Sebastian Orzechowski",
        "url": BASE + "/", "logo": BASE + "/assets/brand/nut-logo.svg",
        "email": "info@nut-software.pl", "taxID": "8741681486",
        "identifier": {"@type": "PropertyValue", "propertyID": "REGON", "value": "386776684"},
        # Publish only the city, including in machine-readable metadata.
        "address": {"@type": "PostalAddress", "addressLocality": "Bydgoszcz", "addressCountry": "PL"},
        "sameAs": ["https://github.com/Nut-Software"],
    }
    html_keys = {"heroTitle", "heroCta", "heroMore", "approachTitle", "contactTitle"}
    for language, content in translations.items():
        url = BASE + ("/" if language == "pl" else "/en/")
        other_language = "en" if language == "pl" else "pl"
        graph = {
            "@context": "https://schema.org", "@graph": [organization, {
                "@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/",
                "name": "Nut Software", "inLanguage": ["pl", "en"],
                "publisher": {"@id": BASE + "/#organization"},
            }, {
                "@type": "WebPage", "@id": url + "#webpage", "url": url,
                "name": content["title"], "description": content["description"],
                "inLanguage": language, "isPartOf": {"@id": BASE + "/#website"},
                "about": {"@id": BASE + "/#organization"},
            }],
        }
        title, description = escape(content["title"], quote=True), escape(content["description"], quote=True)
        locale, other_locale = ("pl_PL", "en_GB") if language == "pl" else ("en_GB", "pl_PL")
        schema = json.dumps(graph, ensure_ascii=False).replace("<", "\\u003c")
        seo_head = f'''    <link rel="canonical" href="{url}" />
    <link rel="alternate" hreflang="pl" href="{BASE}/" />
    <link rel="alternate" hreflang="en" href="{BASE}/en/" />
    <link rel="alternate" hreflang="x-default" href="{BASE}/" />
    <meta name="robots" content="index, follow, max-image-preview:large" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Nut Software" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:locale" content="{locale}" />
    <meta property="og:locale:alternate" content="{other_locale}" />
    <meta property="og:image" content="{BASE}/assets/brand/social-card.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="Nut Software" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <meta name="twitter:image" content="{BASE}/assets/brand/social-card.png" />
    <meta name="twitter:image:alt" content="Nut Software" />
    <script type="application/ld+json">{schema}</script>'''
        values = {key: value if key in html_keys else escape(value, quote=True) for key, value in content.items()}
        values.update(language=language, seo_head=seo_head, other_language=other_language,
                      styles_url="/styles.css?v=" + hashlib.sha256((ROOT / "styles.css").read_bytes()).hexdigest()[:10],
                      script_url="/site.js?v=" + hashlib.sha256((ROOT / "site.js").read_bytes()).hexdigest()[:10],
                      other_url="/en/" if language == "pl" else "/", other_label=other_language.upper(),
                      contact_href="mailto:info@nut-software.pl?subject=" + quote(
                          "Nut Software — kontakt" if language == "pl" else "Nut Software — enquiry"))
        destination = ROOT / ("index.html" if language == "pl" else "en/index.html")
        destination.parent.mkdir(exist_ok=True)
        destination.write_text(template.substitute(values))
        print(destination.relative_to(ROOT))
    (ROOT / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{BASE}/</loc></url>
  <url><loc>{BASE}/en/</loc></url>
</urlset>
''')


if __name__ == "__main__":
    build()
