import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build_elsaeed_helpers import (
    BASE_DIR, VIDEOS_DIR, DOMAIN, PHONE, PHONE_FORMATTED, PHONE_DISPLAY, WHATSAPP_LINK,
    BRAND_NAME, BRAND_FULL, get_head, get_header, get_footer,
    generate_breadcrumbs_html, generate_video_schema
)

VIDEOS_DATA = [
    {
        "filename": "winch-elsaeed-ai-promo.html",
        "video_file": "winch-elsaeed-ai-promo.mp4",
        "poster_file": "poster_elsaeed_ai_promo.webp",
        "title": "الفيديو التعريفي الرسمي: أسطول وإمكانيات ونش السعيد لإنقاذ ونقل السيارات",
        "description": "شاهد الفيديو التعريفي الشامل لخدمات وأسطول ونش السعيد للإنقاذ السريع. أحدث تقنيات السحب والرفع الهيدروليكي، تغطية شاملة للقاهرة والجيزة وكافة الطرق السريعة بمصر 24 ساعة.",
        "upload_date": "2026-11-10T18:00:00+02:00",
        "duration": "PT1M10S",
        "keywords": "فيديو ونش السعيد, إعلان ونش انقاذ سيارات, ونش انقاذ مصر, اقرب ونش انقاذ, فيلم ونش السعيد",
        "details_heading": "رؤية متطورة وأسطول متكامل لخدمات الإنقاذ السريع",
        "details_text": "يقدم هذا الفيديو التعريفي الشامل نظرة متكاملة حول إمكانيات أسطول ونش السعيد لإنقاذ السيارات. نوفر حلول سحب ونقل فورية لجميع أنواع السيارات الملاكي والكهربائية والنقل الخفيف، مع التزام صارم بالوصول خلال 15 دقيقة فقط وأعلى معايير الأمان والسلامة."
    },
    {
        "filename": "winch-elsaeed-towing-action.html",
        "video_file": "202607211016.mp4",
        "poster_file": "poster_elsaeed_action.webp",
        "title": "توثيق بالفيديو: ونش السعيد لإنقاذ السيارات - سحب ورفع احترافي 24 ساعة",
        "description": "شاهد توثيقاً عملياً لعملية رفع وسحب ونقل سيارة بأحدث ونش إنقاذ هيدروليكي مجهز من فريق ونش السعيد لإنقاذ السيارات في مصر. سرعة وأمان واحترافية.",
        "upload_date": "2026-11-08T12:00:00+02:00",
        "duration": "PT39S",
        "keywords": "فيديو ونش انقاذ, توثيق ونش السعيد, سحب سيارات هيدروليك, ونش انقاذ سريع",
        "details_heading": "كفاءة ومعدات هيدروليكية حديثة لرفع وتأمين السيارات",
        "details_text": "يوضح هذا التوثيق الميداني جانباً من العمليات اليومية لأسطول ونش السعيد للإنقاذ السريع. نعتمد على أحدث الرافعات الهيدروليكية المزودة بأحزمة تثبيت خاصة تضمن حماية تامة لنظام التعليق، ممتصات الصدمات، والهيكل الخارجي للسيارة دون خدش واحد."
    },
    {
        "filename": "winch-elsaeed-highway-rescue.html",
        "video_file": "WhatsApp Video 2026-07-21 at 9.56.58 AM.mp4",
        "poster_file": "poster_elsaeed_highway.webp",
        "title": "توثيق ميداني: إنقاذ ونقل سيارة على الطريق السريع - ونش السعيد 24 ساعة",
        "description": "توثيق بالفيديو لإنقاذ سيارة معطلة على الطريق السريع بأعلى معايير السلامة المرورية وسرعة استجابة قياسية من ونش السعيد للإنقاذ السريع.",
        "upload_date": "2026-11-08T12:30:00+02:00",
        "duration": "PT2M8S",
        "keywords": "انقاذ سيارات طريق سريع, ونش طريق سريع, ونش السعيد مصر, انقاذ اعطال الطريق",
        "details_heading": "تأمين الطرق السريعة وسرعة الوصول القياسية",
        "details_text": "عند حدوث عطل مفاجئ على الطرق السريعة كالدائري أو طريق السويس أو الإسكندرية الصحراوي، يكون عامل الوقت والسلامة هو الأهم. في هذا الفيديو، يرصد فريق ونش السعيد إجراءات تأمين محيط العطل بوضع إشارات التحذير وسحب السيارة ونقلها بمرونة وانسيابية تامة تجنباً للازدحام وحفاظاً على أرواح الركاب."
    },
    {
        "filename": "winch-elsaeed-rapid-dispatch.html",
        "video_file": "WhatsApp Video 2026-07-21 at 9.56.58 AM (1).mp4",
        "poster_file": "poster_elsaeed_dispatch.webp",
        "title": "تحرك سريع وفوري لونش إنقاذ السعيد لنجدة سيارة معطلة في دقائق",
        "description": "شاهد سرعة استجابة وانطلاق أوناش السعيد للإنقاذ السريع فور تلقي بلاغ العطل. انتشار واسع لضمان الوصول إليك خلال 15 دقيقة فقط.",
        "upload_date": "2026-11-08T13:00:00+02:00",
        "duration": "PT1M26S",
        "keywords": "سرعة ونش انقاذ, اقرب ونش سريع, نجدة سيارات فورية, ونش السعيد",
        "details_heading": "جاهزية تامة وتوزيع استراتيجي للأوناش",
        "details_text": "يعتمد ونش السعيد على تمركز أوناشه عند المخارج والمطالع الحيوية في القاهرة والجيزة والمحاور الرئيسية، مما يمكننا من الانطلاق الفوري بمجرد اتصال العميل والوصول إليه في مدة تتراوح بين 15 إلى 20 دقيقة كحد أقصى على مدار 24 ساعة طوال أيام الأسبوع."
    }
]

def build_video_pages():
    print("--- Generating Google Video Watch Pages with Existing Videos ---")
    for v in VIDEOS_DATA:
        file_path = os.path.join(VIDEOS_DIR, v["filename"])
        canonical_url = f"{DOMAIN}/videos/{v['filename']}"
        video_url = f"{DOMAIN}/assets/videos/{v['video_file'].replace(' ', '%20')}"
        poster_url = f"{DOMAIN}/assets/images/{v['poster_file']}"

        head = get_head(
            title=f"{v['title']} | {BRAND_NAME}",
            description=v['description'],
            canonical_url=canonical_url,
            is_subfolder=True,
            preload_lcp=False,
            keywords=v['keywords']
        )

        video_schema = generate_video_schema(
            title=v['title'],
            desc=v['description'],
            upload_date=v['upload_date'],
            duration=v['duration'],
            embed_url=canonical_url,
            content_url=video_url,
            thumbnail_url=poster_url
        )

        breadcrumbs = generate_breadcrumbs_html([
            ("الرئيسية", "index.html"),
            ("معرض الفيديوهات والتوثيق", None),
            (v['title'], None)
        ], is_subfolder=True)

        header = get_header(active_page="services", is_subfolder=True)
        footer = get_footer(is_subfolder=True)

        content = f"""{head}
{video_schema}
</head>
<body>
{header}

{breadcrumbs}

<main class="container">
  <div class="video-watch-container">
    <div class="video-player-card">
      <video controls preload="metadata" poster="../assets/images/{v['poster_file']}" style="width: 100%; max-height: 540px; background: #000; border-radius: 16px 16px 0 0;">
        <source src="../assets/videos/{v['video_file']}" type="video/mp4">
        متصفحك لا يدعم تشغيل الفيديو المباشر.
      </video>

      <div class="video-player-info">
        <h1>{v['title']}</h1>
        <div class="video-meta-row">
          <span>📅 تاريخ النشر: 2026/11/08</span>
          <span>⏱️ المدة: {v['duration'].replace('PT', '').replace('M', ' دقيقة و ').replace('S', ' ثانية')}</span>
          <span>📍 التغطية: كافة طرق ومحاور القاهرة والجيزة والمحافظات</span>
          <span>✅ المصدر: توثيق رسمي — أسطول {BRAND_NAME}</span>
        </div>

        <div class="video-desc">
          <p>{v['description']}</p>
        </div>

        <div class="callout-box">
          <h4>{v['details_heading']}</h4>
          <p>{v['details_text']}</p>
        </div>

        <!-- Emergency Action Box -->
        <div class="article-cta-box">
          <h3>هل تعطلت سيارتك وتحتاج ونش إنقاذ فوري؟</h3>
          <p>أوناش السعيد متمركزة الآن بالقرب منك على كافة الطرق. اتصل بنا وسنصلك خلال دقائق معدودة بأفضل سعر وسلامة تامة لسيارتك.</p>
          <div class="cta-btns">
            <a href="tel:{PHONE}" class="btn btn-gold" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
              📞 اتصل فوراً: <span dir="ltr">{PHONE}</span>
            </a>
            <a href="{WHATSAPP_LINK}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="font-weight: 800; font-size: 17px; padding: 14px 28px; text-decoration: none; border-radius: 8px;">
              💬 طلب ونش عبر واتساب
            </a>
          </div>
        </div>

        <!-- Related Videos Nav -->
        <div style="margin-top: 40px; padding-top: 24px; border-top: 1px solid rgba(0, 180, 216, 0.2);">
          <h3 style="color: #00b4d8; font-size: 20px; margin-bottom: 16px;">فيديوهات وتوثيقات أخرى من أرض الواقع:</h3>
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
"""
        for other in VIDEOS_DATA:
            if other["filename"] != v["filename"]:
                content += f"""            <div style="background: rgba(15, 31, 53, 0.6); padding: 16px; border-radius: 12px; border: 1px solid rgba(0, 180, 216, 0.15);">
              <h4 style="font-size: 15px; margin-bottom: 8px;"><a href="{other['filename']}" style="color: #ffffff; text-decoration: none;">{other['title']}</a></h4>
              <p style="font-size: 13px; color: #94a3b8; margin-bottom: 12px;">{other['description'][:110]}...</p>
              <a href="{other['filename']}" style="color: #f0b429; font-size: 13px; font-weight: 700; text-decoration: none;">مشاهدة التوثيق ←</a>
            </div>\n"""

        content += f"""          </div>
        </div>
      </div>
    </div>
  </div>
</main>

{footer}
"""
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated Video Watch Page: {v['filename']}")

if __name__ == "__main__":
    build_video_pages()
