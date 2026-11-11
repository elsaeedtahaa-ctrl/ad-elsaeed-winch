import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_elsaeed_helpers import (
    BASE_DIR, DOMAIN, PHONE, PHONE_FORMATTED, PHONE_DISPLAY, WHATSAPP_LINK, EMAIL,
    BRAND_NAME, BRAND_FULL, get_head, get_header, get_footer,
    generate_breadcrumbs_html, generate_local_business_schema, generate_faq_schema
)

def build_coverage_page():
    canonical_url = f"{DOMAIN}/coverage.html"
    head = get_head(
        title=f"مناطق تغطية ونش إنقاذ السعيد في القاهرة والجيزة والمحافظات | {BRAND_NAME}",
        description="تعرف على خريطة وتغطية أوناش إنقاذ السعيد على مدار 24 ساعة في القاهرة الكبرى، الجيزة، التجمع، زايد، أكتوبر، والطرق والمحاور السريعة.",
        canonical_url=canonical_url,
        is_subfolder=False,
        preload_lcp=False,
        keywords="مناطق تغطية ونش انقاذ, ونش القاهرة, ونش الجيزة, ونش التجمع, ونش 6 اكتوبر, ونش الطرق السريعة"
    )
    breadcrumbs = generate_breadcrumbs_html([
        ("الرئيسية", "index.html"),
        ("مناطق التغطية", None)
    ], is_subfolder=False)
    header = get_header(active_page="coverage", is_subfolder=False)
    footer = get_footer(is_subfolder=False)
    local_schema = generate_local_business_schema("مناطق تغطية أوناش السعيد", canonical_url)

    areas_data = [
        ("الطريق الدائري ومحور 26 يوليو", "تغطية شاملة لكافة مطالع ومنازل الدائري، دائري المعادي، المنيب، المريوطية، والوراق.", "blog/winch-daeri-cairo.html", "winch-highway-patrol.webp"),
        ("التجمع الخامس والقاهرة الجديدة", "تغطية شارع التسعين، اللوتس، المستثمرين، والنرجس وسرعة وصول في دقائق.", "blog/winch-tagamoa-new-cairo.html", "winch-luxury-car-flatbed.webp"),
        ("الشيخ زايد ومدينة 6 أكتوبر", "تغطية وصلة دهشور، طريق الواحات، المحور المركزي، وكافة أحياء زايد وأكتوبر.", "blog/winch-sheikh-zayed-6-october.html", "winch-porsche-towing.webp"),
        ("مدينة نصر ومصر الجديدة", "تغطية عباس العقاد، مكرم عبيد، النزهة، روكسي، طريق النصر، وصلاح سالم.", "blog/winch-nasr-city.html", "winch-red-truck-patrol.webp"),
        ("المعادي وأوتوستراد المعادي", "تغطية دجلة، ثكنات المعادي، الكورنيش، والأوتوستراد السريع لنقل وتأمين سيارتك.", "blog/winch-maadi.html", "winch-night-pickup.webp"),
        ("المقطم والهضبة الوسطى", "أوناش مجهزة للتعامل مع المنحدرات والمطالع الجبلية بشارع 9 ومحيط الأوتوستراد.", "blog/winch-mokattam.html", "winch-red-truck-heavy.webp"),
        ("الجيزة والهرم وفيصل والدقي", "تغطية شوارع الهرم، فيصل، ميدان الجيزة، الدقي، والمهندسين على مدار 24 ساعة.", "blog/winch-giza-haram.html", "winch-rescue-cairo-1.webp"),
        ("وسط البلد والزمالك والعجوزة", "أوناش مرنة للمناورة في الشوارع المزدحمة وكباري 6 أكتوبر و15 مايو.", "blog/winch-downtown-cairo.html", "winch-cupra-safe-loading.webp"),
        ("شبرا ومصر وشبرا الخيمة", "تغطية شارع شبرا، ميدان المؤسسة، مسطرد، وبداية طريق مصر إسكندرية الزراعي.", "blog/winch-shobra.html", "winch-rescue-cairo-2.webp"),
        ("مدينة العبور وسوق العبور", "تمركز دائم عند كارفور العبور وجولف سيتي ومحور خط 10 وطريق الإسماعيلية.", "blog/winch-obour-city.html", "winch-caterpillar-loader.webp"),
        ("الشروق وبدر وهليوبوليس الجديدة", "خدمة سريعة على بوابات طريق السويس والروبيكي ومدن شرق القاهرة.", "blog/winch-shorouk-badr.html", "winch-porsche-highway.webp"),
        ("مدينتي والرحاب والمستقبل سيتي", "أوناش هيدروليك نزول كامل مخصصة للسيارات الفارهة والحديثة 24 ساعة.", "blog/winch-rehab-madinaty.html", "winch-night-supercar.webp"),
        ("العاصمة الإدارية الجديدة", "تغطية الحي الحكومي، محور بن زايد، والدائري الأوسطي بسرعة قياسية.", "blog/winch-new-capital.html", "winch-hero-fleet.webp"),
        ("طريق السويس الصحراوي", "تأمين الطرق السريعة وسحب فوري للسيارات المعطلة حتى بوابات الرسوم.", "blog/winch-suez-road.html", "winch-highway-patrol.webp"),
        ("طريق مصر إسكندرية الصحراوي", "إنقاذ سريع وموثوق من بوابات القاهرة حتى وادي النطرون والإسكندرية.", "blog/winch-alex-desert-road.html", "winch-red-truck-heavy.webp")
    ]

    cards_html = ""
    for title, desc, link, img in areas_data:
        cards_html += f"""
      <div class="service-card" style="display: flex; flex-direction: column; overflow: hidden; padding: 0; background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius);">
        <div style="height: 190px; overflow: hidden; background: #000;">
          <img src="assets/images/{img}" alt="{title}" class="coverage-card-img" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;">
        </div>
        <div style="padding: 24px; display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
          <div>
            <h3 style="font-size: 20px; font-weight: 700; color: #ffffff; margin-bottom: 10px;">📍 {title}</h3>
            <p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin-bottom: 18px;">{desc}</p>
          </div>
          <a href="{link}" style="color: #f0b429; font-weight: 700; font-size: 14px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
            دليل ونقاط التمركز بالتفصيل ←
          </a>
        </div>
      </div>
"""

    content = f"""{head}
{local_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container" style="padding-top: 20px; padding-bottom: 70px;">
  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <span class="section-label">🗺️ انتشار استراتيجي وسرعة وصول</span>
    <h1 class="section-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 900; margin: 12px 0;">مناطق تغطية ونش إنقاذ السعيد في مصر</h1>
    <p class="section-desc" style="max-width: 750px; margin: 0 auto; color: #94a3b8; font-size: 16px;">نغطي كافة أحياء ومحاور القاهرة الكبرى والجيزة والطرق السريعة الرابطة بين المحافظات. أينما كنت، نصلك في زمن قياسي لا يتجاوز 15 - 20 دقيقة.</p>
  </div>

  <div class="services-grid" style="grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));">
    {cards_html}
  </div>

  <!-- Action CTA -->
  <div class="article-cta-box" style="margin-top: 60px;">
    <h3>هل تحتاج ونش إنقاذ سيارات الآن في منطقتك؟</h3>
    <p>فريق ونش السعيد متأهب بالقرب منك على مدار 24 ساعة. اتصل بنا أو راسلنا وسنصلك فوراً بأفضل سعر.</p>
    <div class="cta-btns">
      <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        📞 اتصل الآن: <span dir="ltr">{PHONE}</span>
      </a>
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        💬 طلب ونش عبر واتساب
      </a>
    </div>
  </div>
</main>

{footer}
"""
    with open(os.path.join(BASE_DIR, "coverage.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated: coverage.html with vivid area photos")

def update_services_page():
    canonical_url = f"{DOMAIN}/services.html"
    head = get_head(
        title=f"خدمات ونش إنقاذ وسحب سيارات السعيد في مصر 24 ساعة | {BRAND_NAME}",
        description="تعرف على خدمات ونش السعيد: سحب ونقل سيارات الملاكي، إنقاذ الطرق السريعة، أوناش هيدروليكية منخفضة للسيارات الفارهة، ونقل سيارات الحوادث 24/7.",
        canonical_url=canonical_url,
        is_subfolder=False,
        preload_lcp=False,
        keywords="خدمات ونش انقاذ, سحب سيارات, انقاذ سيارات معطلة, ونش هيدروليك, نقل سيارات حوادث"
    )
    breadcrumbs = generate_breadcrumbs_html([
        ("الرئيسية", "index.html"),
        ("الخدمات", None)
    ], is_subfolder=False)
    header = get_header(active_page="services", is_subfolder=False)
    footer = get_footer(is_subfolder=False)
    local_schema = generate_local_business_schema("خدمات ونش إنقاذ السعيد", canonical_url)

    services_list = [
        ("سحب سيارات الملاكي والمعطلة", "سحب ونقل سيارات الركوب الملاكي والسيدان والهاتشباك بأمان تام وسرعة وصول فائقة لكافة الورش ومراكز الصيانة.", "winch-luxury-car-flatbed.webp"),
        ("إنقاذ الطرق السريعة والمحاور", "خدمة طوارئ متخصصة للطرق السريعة (الدائري، السويس، الإسماعيلية، الصحراوي) لتأمين وسحب السيارة دون تعطيل المرور.", "winch-highway-patrol.webp"),
        ("أوناش هيدروليك للسيارات الفارهة (VIP)", "أوناش هيدروليكية نزول كامل للأرض لحماية سياراتك الفاخرة والرياضية من أي احتكاك في ممتص الصدمات أو الهيكل.", "winch-night-supercar.webp"),
        ("نقل سيارات الحوادث الصعبة", "تجهيزات خاصة بروافع وسلاسل سحب فولاذية قوية لانتشال وسحب السيارات المتضررة من الحوادث أو العالقة في المنحدرات.", "winch-red-truck-patrol.webp"),
        ("نقل المعدات واللودرات الخفيفة", "أوناش ثقيلة متعددة المحاور لنقل اللودرات والمعدات الزراعية والصناعية وسيارات البضائع بأمان تام.", "winch-caterpillar-loader.webp"),
        ("نقل سيارات المسافات الطويلة بين المحافظات", "أسطول جاهز لنقل سيارتك بأمان وسرعة بين كافة محافظات مصر بأسعار مخفضة وخصومات حقيقية.", "winch-porsche-highway.webp")
    ]

    cards_html = ""
    for title, desc, img in services_list:
        cards_html += f"""
      <div class="service-card" style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); overflow: hidden; display: flex; flex-direction: column;">
        <div style="height: 200px; overflow: hidden; background: #000;">
          <img src="assets/images/{img}" alt="{title}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s ease;">
        </div>
        <div style="padding: 24px; display: flex; flex-direction: column; flex: 1; justify-content: space-between;">
          <div>
            <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 10px;">{title}</h3>
            <p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin-bottom: 18px;">{desc}</p>
          </div>
          <a href="tel:{PHONE}" style="color: #f0b429; font-weight: 700; font-size: 14px; text-decoration: none;">اطلب هذه الخدمة الآن ←</a>
        </div>
      </div>
"""

    content = f"""{head}
{local_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container" style="padding-top: 20px; padding-bottom: 70px;">
  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <span class="section-label">🛠️ حلول إنقاذ متكاملة لسيارتك</span>
    <h1 class="section-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 900; margin: 12px 0;">خدمات ونش إنقاذ سيارات السعيد في مصر</h1>
    <p class="section-desc" style="max-width: 750px; margin: 0 auto; color: #94a3b8; font-size: 16px;">نقدم مجموعة شاملة من خدمات سحب ورفع وإنقاذ السيارات على مدار 24 ساعة يومياً بأحدث المعدات وسائقي الإنقاذ المحترفين.</p>
  </div>

  <div class="services-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 24px;">
    {cards_html}
  </div>

  <!-- Video Showcase Box -->
  <div style="margin-top: 60px; background: rgba(15, 31, 53, 0.8); border: 1px solid var(--glass-border); border-radius: var(--radius); padding: 36px 24px; text-align: center;">
    <h2 style="color: #ffffff; font-size: 24px; font-weight: 800; margin-bottom: 12px;">شاهد كفاءة أوناشنا بالفيديو</h2>
    <p style="color: #94a3b8; max-width: 600px; margin: 0 auto 24px; font-size: 15px;">نوثق عمليات الرفع والسحب الميدانية على الطرق السريعة لتتأكد بنفسك من مدى احترافيتنا وأمان سيارتك معنا.</p>
    <a href="videos/winch-elsaeed-towing-action.html" class="btn btn-gold" style="font-weight: 700; padding: 12px 24px; text-decoration: none; border-radius: 8px;">
      ▶️ مشاهدة توثيق الفيديو الميداني
    </a>
  </div>

  <!-- Action CTA -->
  <div class="article-cta-box" style="margin-top: 40px;">
    <h3>هل سيارتك معطلة وتحتاج ونش فوري؟</h3>
    <p>أوناش السعيد جاهزة للتحرك إليك خلال 15 دقيقة فقط. اتصل الآن وسنكون عندك فوراً.</p>
    <div class="cta-btns">
      <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        📞 اتصل فوراً: <span dir="ltr">{PHONE}</span>
      </a>
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        💬 طلب ونش عبر واتساب
      </a>
    </div>
  </div>
</main>

{footer}
"""
    with open(os.path.join(BASE_DIR, "services.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated: services.html with vivid service photos")

def update_about_page():
    canonical_url = f"{DOMAIN}/about.html"
    head = get_head(
        title=f"من نحن — قصة وخبرة ونش إنقاذ السعيد في مصر | {BRAND_NAME}",
        description="تعرف على ونش إنقاذ السعيد: سنوات من الخبرة الميدانية، أسطول أوناش حديث، وسائقون محترفون متاحون 24 ساعة لخدمتك في كافة أنحاء مصر.",
        canonical_url=canonical_url,
        is_subfolder=False,
        preload_lcp=False,
        keywords="من نحن ونش السعيد, خبرة ونش سيارات, فريق ونش السعيد, اسطول اوناش السعيد"
    )
    breadcrumbs = generate_breadcrumbs_html([
        ("الرئيسية", "index.html"),
        ("من نحن", None)
    ], is_subfolder=False)
    header = get_header(active_page="about", is_subfolder=False)
    footer = get_footer(is_subfolder=False)
    local_schema = generate_local_business_schema("من نحن - ونش السعيد", canonical_url)

    content = f"""{head}
{local_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container" style="padding-top: 20px; padding-bottom: 70px;">
  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <span class="section-label">🤝 الشريك الموثوق على الطريق</span>
    <h1 class="section-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 900; margin: 12px 0;">من نحن — ونش إنقاذ السعيد للإنقاذ السريع</h1>
    <p class="section-desc" style="max-width: 750px; margin: 0 auto; color: #94a3b8; font-size: 16px;">نحن فريق متخصص في إنقاذ وسحب ونقل السيارات في مصر، نعمل بشغف واحترافية لنكون دائماً صمام الأمان لقائدي السيارات على كافة المحاور والطرق السريعة.</p>
  </div>

  <div style="max-width: 900px; margin: 0 auto; font-size: 17px; line-height: 1.85; color: #cbd5e1;">
    <!-- Featured About Banner -->
    <div style="border-radius: 16px; overflow: hidden; margin-bottom: 32px; border: 1px solid var(--glass-border); box-shadow: var(--shadow);">
      <img src="assets/images/winch-hero-fleet.webp" alt="أسطول سيارات وأوناش إنقاذ السعيد" style="width: 100%; height: auto; max-height: 420px; object-fit: cover; display: block;">
      <div style="background: rgba(10, 22, 40, 0.9); padding: 12px 20px; font-size: 14px; color: #94a3b8;">
        🚛 أسطول أوناش حديث ومتطور جاهز على مدار 24 ساعة لخدمتك في جميع أنحاء مصر.
      </div>
    </div>

    <div class="callout-box">
      <h4>رؤيتنا ورسالتنا</h4>
      <p>تقديم أسرع وأأمن خدمة إنقاذ سيارات في مصر بأسعار عادلة وشفافة، والتعامل مع سيارة كل عميل وكأنها سيارتنا الخاصة مع الحفاظ التام على سلامتها وسرعة إيصالها لوجهتها المنشودة.</p>
    </div>

    <h2 style="color: #ffffff; font-size: 24px; font-weight: 800; margin: 36px 0 16px;">لماذا يثق بنا آلاف السائقين؟</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px; margin-bottom: 30px;">
      <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius-sm); padding: 20px;">
        <h3 style="color: #00b4d8; font-size: 18px; margin-bottom: 8px;">⏱️ سرعة وصول قياسية</h3>
        <p style="font-size: 14px; color: #94a3b8; margin: 0;">بفضل انتشار أسطولنا على كافة المطالع والمحاور، نصل للعميل في مدة تتراوح بين 15 إلى 20 دقيقة كحد أقصى.</p>
      </div>

      <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius-sm); padding: 20px;">
        <h3 style="color: #00b4d8; font-size: 18px; margin-bottom: 8px;">🛡️ أمان كامل للسيارة</h3>
        <p style="font-size: 14px; color: #94a3b8; margin: 0;">نستخدم أحدث الرافعات الهيدروليكية المزودة بأحزمة تثبيت خاصة تضمن عدم خدش السيارة أو الإضرار بالشاسيه.</p>
      </div>

      <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius-sm); padding: 20px;">
        <h3 style="color: #00b4d8; font-size: 18px; margin-bottom: 8px;">💰 أسعار شفافة وبدون إكراميات</h3>
        <p style="font-size: 14px; color: #94a3b8; margin: 0;">السعر المتفق عليه عبر الهاتف هو السعر النهائي، بدون أي رسوم خفية أو إكراميات إجبارية للسائقين.</p>
      </div>

      <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius-sm); padding: 20px;">
        <h3 style="color: #00b4d8; font-size: 18px; margin-bottom: 8px;">🕐 متواجدون 24/7</h3>
        <p style="font-size: 14px; color: #94a3b8; margin: 0;">نعمل على مدار الساعة طوال أيام الأسبوع وفي كافة العطلات الرسمية لتقديم الدعم الفوري عند أي طارئ.</p>
      </div>
    </div>

    <!-- Gallery of team and trucks -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin: 30px 0;">
      <img src="assets/images/winch-team-hero.webp" alt="كباتن وفريق عمل ونش السعيد" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; border: 1px solid var(--glass-border);">
      <img src="assets/images/winch-red-truck-patrol.webp" alt="شاحنة ونش إنقاذ حديثة" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; border: 1px solid var(--glass-border);">
      <img src="assets/images/winch-cupra-safe-loading.webp" alt="تحميل سيارة بأمان تام" style="width: 100%; height: 200px; object-fit: cover; border-radius: 12px; border: 1px solid var(--glass-border);">
    </div>

    <!-- Action CTA -->
    <div class="article-cta-box" style="margin-top: 40px;">
      <h3>هل تحتاج لطلب ونش إنقاذ الآن؟</h3>
      <p>فريقنا مستعد لتلبية طلبك فوراً أينما كنت. اتصل بنا على الرقم الموحد.</p>
      <div class="cta-btns">
        <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
          📞 اتصل الآن: <span dir="ltr">{PHONE}</span>
        </a>
        <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
          💬 تواصل عبر واتساب
        </a>
      </div>
    </div>
  </div>
</main>

{footer}
"""
    with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated: about.html with photos")

def update_contact_page():
    canonical_url = f"{DOMAIN}/contact.html"
    head = get_head(
        title=f"اتصل بنا — رقم ونش إنقاذ السعيد 24 ساعة | {BRAND_NAME}",
        description="تواصل فوراً مع ونش إنقاذ سيارات السعيد على الرقم 01041316499 أو عبر الواتساب. نصلك في 15 دقيقة أينما كنت في القاهرة والجيزة والمحافظات.",
        canonical_url=canonical_url,
        is_subfolder=False,
        preload_lcp=False,
        keywords="اتصل بونش السعيد, رقم ونش انقاذ, تليفون ونش سيارات, واتساب ونش انقاذ"
    )
    breadcrumbs = generate_breadcrumbs_html([
        ("الرئيسية", "index.html"),
        ("اتصل بنا", None)
    ], is_subfolder=False)
    header = get_header(active_page="contact", is_subfolder=False)
    footer = get_footer(is_subfolder=False)
    local_schema = generate_local_business_schema("اتصل بنا - ونش السعيد", canonical_url)

    content = f"""{head}
{local_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container" style="padding-top: 20px; padding-bottom: 70px;">
  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <span class="section-label">📞 تواصل فوري مباشر</span>
    <h1 class="section-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 900; margin: 12px 0;">اتصل بونش إنقاذ السعيد للإنقاذ السريع</h1>
    <p class="section-desc" style="max-width: 750px; margin: 0 auto; color: #94a3b8; font-size: 16px;">خدمة العملاء وغرفة عمليات الطوارئ جاهزة لتلقي اتصالاتكم وتوجيه أقرب ونش إليكم على مدار 24 ساعة يومياً.</p>
  </div>

  <div style="max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
    <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); padding: 32px 24px; text-align: center;">
      <span style="font-size: 40px; display: block; margin-bottom: 12px;">📞</span>
      <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 8px;">اتصال هاتفي مباشر</h3>
      <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">خط الطوارئ السريع متاح طوال الـ 24 ساعة للرد الفوري على اتصالاتكم.</p>
      <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block;">
        <span dir="ltr">{PHONE}</span>
      </a>
    </div>

    <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); padding: 32px 24px; text-align: center;">
      <span style="font-size: 40px; display: block; margin-bottom: 12px;">💬</span>
      <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 8px;">إرسال الموقع عبر واتساب</h3>
      <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">أرسل اللوكيشن ونوع سيارتك وسنقوم بالرد وتأكيد السعر وموعد الوصول فوراً.</p>
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 12px 24px; text-decoration: none; border-radius: 8px; display: inline-block;">
        مراسلة واتساب فورية
      </a>
    </div>
  </div>

  <!-- Additional Info Box -->
  <div style="max-width: 800px; margin: 40px auto 0; background: rgba(15, 31, 53, 0.7); border: 1px solid rgba(0, 180, 216, 0.2); border-radius: var(--radius); padding: 24px;">
    <h3 style="color: #f0b429; font-size: 19px; font-weight: 700; margin-bottom: 12px;">معلومات سريعة قبل طلب الونش:</h3>
    <ul style="color: #cbd5e1; font-size: 15px; line-height: 1.8; padding-right: 20px;">
      <li>حدد موقعك بدقة (اسم الشارع، أقرب مخرج أو مطلع، أو علامة مميزة).</li>
      <li>وضح نوع سيارتك وفئتها (ملاكي، دفع رباعي، فان).</li>
      <li>وضح سبب العطل (عطل محرك، إطار، حادث، بطارية).</li>
      <li>احتفظ بهاتفك مفتوحاً للتواصل مع كابتن الونش أثناء تحركه إليك.</li>
    </ul>
  </div>
</main>

{footer}
"""
    with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated: contact.html")

def build_pricing_page():
    canonical_url = f"{DOMAIN}/pricing.html"
    head = get_head(
        title=f"دليل أسعار ونش إنقاذ السيارات في مصر 2026 | {BRAND_NAME}",
        description="دليل أسعار ونش إنقاذ سيارات السعيد في مصر. أسعار عادلة وشفافة بدون أي استغلال لوقت العطل أو إكراميات إضافية. تواصل لمعرفة سعرك بدقة.",
        canonical_url=canonical_url,
        is_subfolder=False,
        preload_lcp=False,
        keywords="اسعار ونش الانقاذ, تكلفة ونش سيارات, ارخص ونش انقاذ مصر, سعر سحب سيارة"
    )
    breadcrumbs = generate_breadcrumbs_html([
        ("الرئيسية", "index.html"),
        ("دليل الأسعار", None)
    ], is_subfolder=False)
    header = get_header(active_page="pricing", is_subfolder=False)
    footer = get_footer(is_subfolder=False)
    local_schema = generate_local_business_schema("دليل أسعار ونش إنقاذ السعيد", canonical_url)

    content = f"""{head}
{local_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container" style="padding-top: 20px; padding-bottom: 70px;">
  <div class="section-header" style="text-align: center; margin-bottom: 40px;">
    <span class="section-label">💰 شفافية كاملة وعدالة في السعر</span>
    <h1 class="section-title" style="font-size: clamp(26px, 4vw, 38px); font-weight: 900; margin: 12px 0;">دليل أسعار ونش إنقاذ السيارات في مصر 2026</h1>
    <p class="section-desc" style="max-width: 750px; margin: 0 auto; color: #94a3b8; font-size: 16px;">في ونش السعيد، نؤمن بأن الشفافية هي أساس الثقة. نقدم أسعاراً عادلة ومدروسة بدون أي استغلال لوقت العطل أو فرض إكراميات إجبارية على العميل.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 40px;">
    <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); overflow: hidden;">
      <img src="assets/images/winch-luxury-car-flatbed.webp" alt="سحب سيارات الملاكي والسيدان" style="width: 100%; height: 180px; object-fit: cover;">
      <div style="padding: 24px;">
        <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">سحب سيارات الملاكي والسيدان</h3>
        <p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">سحب ونقل سيارات الملاكي بكافة أنواعها داخل القاهرة والجيزة بأحدث الأوناش الهيدروليكية وبأفضل الأسعار الاقتصادية العادلة.</p>
        <div style="color: #f0b429; font-weight: 800; font-size: 15px;">✓ تسعير واضح حسب المسافة</div>
      </div>
    </div>

    <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); overflow: hidden;">
      <img src="assets/images/winch-porsche-towing.webp" alt="سيارات الدفع الرباعي والـ SUV" style="width: 100%; height: 180px; object-fit: cover;">
      <div style="padding: 24px;">
        <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">سيارات الدفع الرباعي والـ SUV</h3>
        <p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">أوناش مجهزة لحمل الأوزان الثقيلة وتثبيت آمن للإطارات الأربعة لحماية نظام الدفع الكلي والتعليق بأسعار تنافسية.</p>
        <div style="color: #f0b429; font-weight: 800; font-size: 15px;">✓ حماية كاملة للشاسيه ونظام الدفع</div>
      </div>
    </div>

    <div style="background: var(--glass-card); border: 1px solid var(--glass-border); border-radius: var(--radius); overflow: hidden;">
      <img src="assets/images/winch-porsche-highway.webp" alt="نقل المحافظات والمسافات الطويلة" style="width: 100%; height: 180px; object-fit: cover;">
      <div style="padding: 24px;">
        <h3 style="color: #ffffff; font-size: 20px; font-weight: 700; margin-bottom: 12px;">نقل المحافظات والمسافات الطويلة</h3>
        <p style="color: #94a3b8; font-size: 14px; line-height: 1.6; margin-bottom: 16px;">خصومات خاصة تصل إلى 20% على المشاوير الطويلة بين القاهرة والإسكندرية، السويس، بورسعيد، والصعيد.</p>
        <div style="color: #f0b429; font-weight: 800; font-size: 15px;">✓ خصومات للمشاوير الطويلة</div>
      </div>
    </div>
  </div>

  <!-- How Pricing is Calculated -->
  <div style="background: rgba(15, 31, 53, 0.7); border: 1px solid rgba(0, 180, 216, 0.2); border-radius: 16px; padding: 32px 24px; margin-bottom: 40px;">
    <h2 style="color: #ffffff; font-size: 24px; font-weight: 800; margin-bottom: 20px;">كيف يتم تحديد تكلفة ونش الإنقاذ بدقة؟</h2>
    <ul style="color: #cbd5e1; font-size: 16px; line-height: 1.9; padding-right: 24px;">
      <li><strong>نقطة التحميل ونقطة التوصيل:</strong> يتم حساب المسافة الفعلية بالكيلومتر بين موقع العطل والمكان الذي ترغب في نقل السيارة إليه.</li>
      <li><strong>فئة وحجم السيارة:</strong> تختلف التكلفة باختلاف نوع السيارة (ملاكي صغير، سيدان عائلي، دفع رباعي كبير 4x4، أو سيارة نقل خفيف).</li>
      <li><strong>طبيعة العطل أو الحادث:</strong> هل السيارة تدور وتتحرك على الإطارات أم يوجد كسر في العفشة أو انقلاب يتطلب سحب وايرات إضافي.</li>
      <li><strong>بدون أي مصاريف خفية:</strong> يتم إبلاغك بالسعر الإجمالي عبر الهاتف قبل تحرك الونش مباشرة، ولا يطالبك السائق بأي إكراميات إضافية.</li>
    </ul>
  </div>

  <!-- Direct Quote CTA -->
  <div class="article-cta-box">
    <h3>احصل على عرض سعر فوري لسيارتك الآن</h3>
    <p>اتصل بنا هاتفياً أو أرسل لنا موقعك ونوع سيارتك على الواتساب وسنخبرك بالتكلفة العادلة في ثوانٍ معدودة.</p>
    <div class="cta-btns">
      <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        📞 اتصل لمعرفة السعر: <span dir="ltr">{PHONE}</span>
      </a>
      <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
        💬 استفسر عن السعر عبر واتساب
      </a>
    </div>
  </div>
</main>

{footer}
"""
    with open(os.path.join(BASE_DIR, "pricing.html"), "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated: pricing.html with photos")

if __name__ == "__main__":
    build_coverage_page()
    update_services_page()
    update_about_page()
    update_contact_page()
    build_pricing_page()
    print("Core pages photo enrichment complete!")
