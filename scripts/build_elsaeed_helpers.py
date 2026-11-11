import os
import json

BASE_DIR = r"E:\عبدالسلام\فولدر الاعلانات\elsaeedwinch-seo-final-v3-GTM\elsaeedwinch-seo-final-v3"
BLOG_DIR = os.path.join(BASE_DIR, "blog")
VIDEOS_DIR = os.path.join(BASE_DIR, "videos")
os.makedirs(BLOG_DIR, exist_ok=True)
os.makedirs(VIDEOS_DIR, exist_ok=True)

# Core Brand Constants
PHONE = "01041316499"
PHONE_DISPLAY = "01041316499"
PHONE_FORMATTED = "010 4131 6499"
PHONE_TEL = "+201041316499"
WHATSAPP_LINK = "https://wa.me/201041316499?text=%D8%B7%D9%88%D8%A7%D8%B1%D8%A6!%20%D8%A3%D8%AD%D8%AA%D8%A7%D8%AC%20%D9%88%D9%86%D8%B4%20%D8%A5%D9%86%D9%82%D8%A7%D8%B0%20%D8%B3%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA%20%D9%81%D9%88%D8%B1%D8%A7%D9%8B%D8%8C%20%D9%85%D9%88%D9%82%D8%B9%D9%8A%20%D8%A7%D9%84%D8%AD%D8%A7%D9%84%D9%8A:%20"
EMAIL = "elsaeedtahaa@gmail.com"
DOMAIN = "https://elsaeedwinch.com"
BRAND_NAME = "السعيد للانقاذ السريع"
BRAND_FULL = "ونش إنقاذ السعيد — أسرع ونش إنقاذ سيارات في مصر"

# GTM Container ID
GTM_ID = "GTM-N6QSL634"

def get_head(title, description, canonical_url, is_subfolder=False, preload_lcp=False, keywords=None):
    p = "../" if is_subfolder else ""
    if not keywords:
        keywords = "ونش انقاذ, ونش انقاذ سيارات, ونش سيارات, ونش السعيد, اقرب ونش, ارخص ونش, ونش انقاذ القاهرة, ونش انقاذ الجيزة"

    preload_lcp_tags = ""
    if preload_lcp:
        preload_lcp_tags = f'''  <!-- Responsive LCP Image Preload (Sub-2s Speed) -->
  <link rel="preload" as="image" href="{p}assets/images/hero-bg-mobile.webp" media="(max-width: 640px)" fetchpriority="high" type="image/webp">
  <link rel="preload" as="image" href="{p}assets/images/hero-bg-pro.webp" media="(min-width: 641px)" fetchpriority="high" type="image/webp">\n'''

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','{GTM_ID}');</script>
  <!-- End Google Tag Manager -->

  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="{DOMAIN}/assets/images/winch-og-banner.webp">
  <meta property="og:locale" content="ar_EG">
  <meta property="og:site_name" content="{BRAND_NAME}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{canonical_url}">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{DOMAIN}/assets/images/winch-og-banner.webp">

  <!-- Theme Color & Mobile Chrome Header -->
  <meta name="theme-color" content="#0a1628">
  <meta name="msapplication-navbutton-color" content="#0a1628">
  <meta name="apple-mobile-web-app-status-bar-style" content="#0a1628">

{preload_lcp_tags}  <!-- Preconnect Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap" rel="stylesheet">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="{p}assets/css/style.css?v=3.5">
"""

def get_header(active_page="home", is_subfolder=False):
    p = "../" if is_subfolder else ""
    nav_links = [
        ("home", "الرئيسية", f"{p}index.html"),
        ("services", "الخدمات", f"{p}services.html"),
        ("coverage", "مناطق التغطية", f"{p}coverage.html"),
        ("pricing", "دليل الأسعار", f"{p}pricing.html"),
        ("blog", "مقالات الإنقاذ", f"{p}blog/index.html"),
        ("about", "من نحن", f"{p}about.html"),
        ("contact", "اتصل بنا", f"{p}contact.html")
    ]

    links_html = ""
    for page_id, label, url in nav_links:
        active_cls = "active" if active_page == page_id else ""
        links_html += f'        <a class="nav-link {active_cls}" href="{url}">{label}</a>\n'

    return f"""
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<!-- Unified Sticky Site Header (Zero Collision / Zero Overlap) -->
<header class="site-header" id="siteHeader">
  <!-- Top Notification Bar -->
  <div class="top-announcement-bar">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 10px;">
      <span>⚡ أسرع ونش إنقاذ سيارات في مصر — نصلك خلال 15 دقيقة</span>
      <span style="color: #00b4d8;">|</span>
      <span>خدمة 24 ساعة طوال أيام الأسبوع</span>
      <span style="color: #00b4d8;">|</span>
      <span>طوارئ: <a href="tel:{PHONE}" style="color: #f0b429; text-decoration: none; font-weight: 800;"><span dir="ltr">{PHONE}</span></a></span>
    </div>
  </div>

  <!-- Main Navbar -->
  <nav class="navbar" id="navbar">
    <div class="nav-container">
      <a class="nav-logo" href="{p}index.html">
        <span class="logo-icon">🛻</span>
        <span class="logo-text">{BRAND_NAME}</span>
      </a>
      <div class="nav-menu" id="navMenu">
{links_html}      </div>
      <a class="nav-cta" href="tel:{PHONE}">
        <span>📞</span> <span dir="ltr">{PHONE}</span>
      </a>
      <button aria-label="القائمة" class="nav-toggle" id="navToggle">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>
</header>
"""

def get_footer(is_subfolder=False):
    p = "../" if is_subfolder else ""
    return f"""
<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3><span>🛻</span> {BRAND_NAME}</h3>
        <p>أسرع ونش إنقاذ وسحب ونقل سيارات في مصر. متواجدون على مدار 24 ساعة على كافة الطرق والمحاور الرئيسية بأحدث أوناش الإنقاذ الهيدروليكية والمقفلة لضمان سلامة سيارتك وسرعة نجدتك.</p>
        <div class="footer-social" style="display: flex; gap: 10px; margin-top: 16px;">
          <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" title="واتساب" style="font-size: 20px; text-decoration: none;">💬</a>
          <a href="tel:{PHONE}" title="اتصال هاتفي" style="font-size: 20px; text-decoration: none;">📞</a>
        </div>
      </div>

      <div class="footer-links">
        <h4>روابط سريعة</h4>
        <a href="{p}index.html">الرئيسية</a>
        <a href="{p}services.html">خدمات الإنقاذ</a>
        <a href="{p}coverage.html">مناطق التغطية</a>
        <a href="{p}pricing.html">دليل الأسعار الشفاف</a>
        <a href="{p}blog/index.html">مقالات ودليل الإنقاذ</a>
        <a href="{p}about.html">من نحن</a>
        <a href="{p}contact.html">اتصل بنا</a>
      </div>

      <div class="footer-links">
        <h4>أهم مناطق التغطية</h4>
        <a href="{p}blog/winch-daeri-cairo.html">ونش الطريق الدائري</a>
        <a href="{p}blog/winch-tagamoa-new-cairo.html">ونش التجمع الخامس والقاهرة الجديدة</a>
        <a href="{p}blog/winch-sheikh-zayed-6-october.html">ونش الشيخ زايد و6 أكتوبر</a>
        <a href="{p}blog/winch-nasr-city.html">ونش مدينة نصر</a>
        <a href="{p}blog/winch-maadi.html">ونش المعادي والأوتوستراد</a>
        <a href="{p}blog/winch-suez-road.html">ونش طريق السويس الصحراوي</a>
        <a href="{p}blog/winch-alex-desert-road.html">ونش طريق مصر إسكندرية الصحراوي</a>
      </div>

      <div class="footer-contact">
        <h4>تواصل مباشر 24 ساعة</h4>
        <div class="footer-contact-item">
          <span>📞</span> <a href="tel:{PHONE}" style="color: #f0b429; font-weight: 800; text-decoration: none;"><span dir="ltr">{PHONE}</span></a>
        </div>
        <div class="footer-contact-item">
          <span>💬</span> <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" style="color: #25d366; font-weight: 700; text-decoration: none;">مراسلة واتساب فورية</a>
        </div>
        <div class="footer-contact-item">
          <span>📧</span> <span>{EMAIL}</span>
        </div>
        <div class="footer-contact-item">
          <span>🕐</span> <span>خدمة متواصلة 24/7 طوال أيام السنة</span>
        </div>
        <div class="footer-contact-item">
          <span>⚡</span> <span>سرعة وصول قياسية: 15 - 20 دقيقة</span>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <p>© 2026 {BRAND_NAME} — أسرع وأوثق ونش إنقاذ سيارات في مصر — جميع الحقوق محفوظة.</p>
      <div style="display: flex; gap: 16px;">
        <a href="{p}privacy-policy.html">سياسة الخصوصية</a>
        <a href="{p}sitemap.xml">خريطة الموقع</a>
      </div>
    </div>
  </div>
</footer>

<!-- Desktop Floating Buttons -->
<div class="floating-btns">
  <a class="float-btn whatsapp" href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" title="راسلنا عبر واتساب">
    <svg viewBox="0 0 24 24" width="28" height="28" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.654-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>
  <a class="float-btn phone" href="tel:{PHONE}" title="اتصل فوراً">
    <svg viewBox="0 0 24 24" width="28" height="28" fill="white"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
  </a>
</div>

<!-- Mobile High-Conversion Emergency Bottom Bar -->
<div class="mobile-bottom-bar">
  <div class="bar-inner">
    <a href="tel:{PHONE}" class="bar-btn bar-call">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
      <span>اتصال فوري: <span dir="ltr">{PHONE}</span></span>
    </a>
    <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="bar-btn bar-whatsapp">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.654-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      <span>واتساب</span>
    </a>
  </div>
</div>

<script>
  // Mobile Nav Toggle
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  if (navToggle && navMenu) {{
    navToggle.addEventListener('click', () => {{
      navMenu.classList.toggle('active');
    }});
  }}
</script>
</body>
</html>
"""

def generate_breadcrumbs_html(items, is_subfolder=False):
    p = "../" if is_subfolder else ""
    breadcrumbs_list = []
    html_items = []
    
    for idx, (name, url) in enumerate(items, 1):
        if url:
            full_url = f"{DOMAIN}/{url.lstrip('/')}"
            html_items.append(f'<li><a href="{p}{url}">{name}</a></li>')
            breadcrumbs_list.append({
                "@type": "ListItem",
                "position": idx,
                "name": name,
                "item": full_url
            })
        else:
            html_items.append(f'<li><span aria-current="page">{name}</span></li>')
            breadcrumbs_list.append({
                "@type": "ListItem",
                "position": idx,
                "name": name
            })

    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": breadcrumbs_list
    }

    html = f"""
  <div class="container">
    <nav class="breadcrumbs" aria-label="مسار التنقل">
      <ol>
        {''.join(html_items)}
      </ol>
    </nav>
  </div>
  <script type="application/ld+json">
  {json.dumps(schema, ensure_ascii=False, indent=2)}
  </script>
"""
    return html

def generate_local_business_schema(page_title, page_url, service_name=None, area_name=None):
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{DOMAIN}/#website",
                "url": DOMAIN,
                "name": BRAND_NAME,
                "description": BRAND_FULL,
                "inLanguage": "ar-EG"
            },
            {
                "@type": "AutoTowingService",
                "@id": f"{DOMAIN}/#service",
                "name": BRAND_NAME,
                "url": page_url,
                "telephone": PHONE_TEL,
                "email": EMAIL,
                "priceRange": "$$",
                "image": f"{DOMAIN}/assets/images/winch-og-banner.webp",
                "description": f"{BRAND_NAME} - أسرع ونش إنقاذ وسحب سيارات 24 ساعة في مصر. نصلك أينما كنت خلال 15 دقيقة بأحدث المعدات الهيدروليكية.",
                "openingHoursSpecification": {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                    "opens": "00:00",
                    "closes": "23:59"
                },
                "areaServed": [
                    {"@type": "City", "name": "Cairo"},
                    {"@type": "City", "name": "Giza"},
                    {"@type": "City", "name": "New Cairo"},
                    {"@type": "City", "name": "6th of October"},
                    {"@type": "City", "name": "Sheikh Zayed"},
                    {"@type": "City", "name": "Nasr City"},
                    {"@type": "City", "name": "Heliopolis"},
                    {"@type": "City", "name": "Maadi"},
                    {"@type": "AdministrativeArea", "name": "الطريق الدائري ومحور 26 يوليو"},
                    {"@type": "AdministrativeArea", "name": "طريق السويس وطريق الإسماعيلية"},
                    {"@type": "AdministrativeArea", "name": "طريق مصر إسكندرية الصحراوي"}
                ],
                "serviceType": [
                    "ونش إنقاذ سيارات",
                    "سحب ونقل سيارات معطلة وحوادث",
                    "إنقاذ سيارات الملاكي والـ SUV",
                    "أوناش هيدروليكية متطورة",
                    "خدمة طوارئ وإنقاذ الطرق السريعة 24 ساعة"
                ]
            }
        ]
    }
    return f"""<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>"""

def generate_faq_schema(faq_items):
    entities = []
    for q, a in faq_items:
        entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities
    }
    return f"""<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>"""

def generate_video_schema(title, desc, upload_date, duration, embed_url, content_url, thumbnail_url):
    schema = {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": title,
        "description": desc,
        "thumbnailUrl": thumbnail_url,
        "uploadDate": upload_date,
        "duration": duration,
        "embedUrl": embed_url,
        "contentUrl": content_url
    }
    return f"""<script type="application/ld+json">
{json.dumps(schema, ensure_ascii=False, indent=2)}
</script>"""
