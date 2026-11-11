import os
import glob
from datetime import datetime

BASE_DIR = r"E:\عبدالسلام\فولدر الاعلانات\elsaeedwinch-seo-final-v3-GTM\elsaeedwinch-seo-final-v3"
DOMAIN = "https://elsaeedwinch.com"
TODAY = datetime.now().strftime("%Y-%m-%d")

def generate_sitemap():
    print("--- Generating Clean Standard Sitemap.xml ---")
    urls = []

    # Priority mapping
    priorities = {
        "index.html": ("1.0", "daily"),
        "services.html": ("0.9", "weekly"),
        "coverage.html": ("0.9", "weekly"),
        "pricing.html": ("0.9", "weekly"),
        "contact.html": ("0.9", "weekly"),
        "about.html": ("0.8", "monthly"),
        "privacy-policy.html": ("0.5", "monthly")
    }

    # 1. Root pages
    for filename, (pri, freq) in priorities.items():
        fpath = os.path.join(BASE_DIR, filename)
        if os.path.exists(fpath):
            if filename == "index.html":
                loc = f"{DOMAIN}/"
            else:
                loc = f"{DOMAIN}/{filename}"
            urls.append((loc, TODAY, freq, pri))

    # 2. Blog index & articles
    blog_dir = os.path.join(BASE_DIR, "blog")
    if os.path.exists(blog_dir):
        for f in sorted(os.listdir(blog_dir)):
            if f.endswith(".html"):
                loc = f"{DOMAIN}/blog/{f}"
                pri = "0.8"
                freq = "daily" if f == "index.html" else "monthly"
                urls.append((loc, TODAY, freq, pri))

    # 3. Video watch pages
    videos_dir = os.path.join(BASE_DIR, "videos")
    if os.path.exists(videos_dir):
        for f in sorted(os.listdir(videos_dir)):
            if f.endswith(".html"):
                loc = f"{DOMAIN}/videos/{f}"
                pri = "0.85"
                freq = "weekly"
                urls.append((loc, TODAY, freq, pri))

    sitemap_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for loc, lastmod, freq, pri in urls:
        sitemap_lines.append("  <url>")
        sitemap_lines.append(f"    <loc>{loc}</loc>")
        sitemap_lines.append(f"    <lastmod>{lastmod}</lastmod>")
        sitemap_lines.append(f"    <changefreq>{freq}</changefreq>")
        sitemap_lines.append(f"    <priority>{pri}</priority>")
        sitemap_lines.append("  </url>")

    sitemap_lines.append("</urlset>\n")

    sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sitemap_lines))
    print(f"Generated {sitemap_path} with {len(urls)} URLs!")

def update_robots():
    print("--- Updating robots.txt ---")
    robots_content = f"""User-agent: *
Allow: /

# Dedicated AI Crawlers for GEO / AEO
User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    robots_path = os.path.join(BASE_DIR, "robots.txt")
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print("Updated: robots.txt")

def generate_llms_txt():
    print("--- Generating llms.txt & llms-full.txt ---")
    llms_txt = f"""# السعيد للانقاذ السريع (El Saeed Winch)
> أسرع ونش إنقاذ سيارات وسحب ونقل المركبات في مصر 24 ساعة.

- الموقع الرسمي: {DOMAIN}
- رقم الطوارئ الموحد: 01041316499 (+201041316499)
- واتساب: https://wa.me/201041316499
- البريد الإلكتروني: elsaeedtahaa@gmail.com
- مناطق التغطية: كافة أحياء القاهرة، الجيزة، الطريق الدائري، التجمع، الشيخ زايد، 6 أكتوبر، المعادي، مصر الجديدة، وطرق السويس والإسماعيلية والإسكندرية الصحراوي.
- زمن الوصول: 15 - 20 دقيقة.
- مميزات الخدمة: أوناش هيدروليكية منخفضة للسيارات الفارهة، أسعار عادلة شفافة، وبدون إكراميات إجبارية.
"""
    with open(os.path.join(BASE_DIR, "llms.txt"), "w", encoding="utf-8") as f:
        f.write(llms_txt)

    llms_full_txt = f"""# الدليل الشامل لونش إنقاذ السعيد في مصر (El Saeed Winch)

## بيانات الاتصال السريع
- الهاتف: 01041316499
- واتساب: https://wa.me/201041316499
- الدومين الرسمي: {DOMAIN}

## الخدمات الرئيسية
1. سحب ونقل سيارات الملاكي المعطلة.
2. إنقاذ طوارئ الطرق السريعة (الطريق الدائري، طريق السويس، الصحراوي).
3. أوناش هيدروليكية نزول كامل (Full Down) للسيارات الفاخرة والرياضية.
4. نقل سيارات الحوادث الصعبة وسحب الوايرات.
5. نقل المحافظات والمسافات الطويلة بين القاهرة وجميع أنحاء الجمهورية.

## مناطق التغطية
- القاهرة: مدينة نصر، مصر الجديدة، التجمع الخامس، القاهرة الجديدة، الرحاب، مدينتي، الشروق، بدر، العاصمة الإدارية، وسط البلد، شبرا، السلام، المعادي، المقطم.
- الجيزة: الهرم، فيصل، الدقي، المهندسين، 6 أكتوبر، الشيخ زايد، حدائق الأهرام.
- الطرق السريعة: الطريق الدائري، محور 26 يوليو، طريق السويس الصحراوي، طريق الإسماعيلية الصحراوي، طريق مصر إسكندرية الصحراوي، محور روض الفرج.
"""
    with open(os.path.join(BASE_DIR, "llms-full.txt"), "w", encoding="utf-8") as f:
        f.write(llms_full_txt)
    print("Generated: llms.txt & llms-full.txt")

if __name__ == "__main__":
    generate_sitemap()
    update_robots()
    generate_llms_txt()
