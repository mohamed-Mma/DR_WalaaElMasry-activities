/* Share + Feedback system — Dr. Walaa El-Masry Activities */
(function () {
  const WA_NUMBER = '201157566942';

  function activityMeta() {
    const title =
      document.querySelector('.game-title')?.textContent?.trim() ||
      document.title.split('|')[0].trim() ||
      'Activity';
    const url = window.location.href.split('#')[0];
    return { title, url };
  }

  function ensureModal() {
    if (document.getElementById('share-modal')) return;

    const modal = document.createElement('div');
    modal.id = 'share-modal';
    modal.className = 'modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.innerHTML = `
      <div class="modal-content share-card">
        <button class="close-modal" id="share-close" type="button" aria-label="Close">&times;</button>
        <p class="eyebrow" id="share-sub" style="animation:none">SHARE ACTIVITY</p>
        <h3 id="share-title" class="share-title"></h3>

        <div class="share-row">
          <input id="share-link" readonly aria-label="Link">
          <button class="view-btn solid" id="share-copy" type="button">COPY</button>
        </div>

        <div class="share-targets">
          <a class="view-btn" id="share-wa" target="_blank" rel="noopener">WhatsApp</a>
          <a class="view-btn" id="share-tg" target="_blank" rel="noopener">Telegram</a>
          <a class="view-btn" id="share-fb" target="_blank" rel="noopener">Facebook</a>
          <button class="view-btn" id="share-native" type="button">More…</button>
        </div>

        <div class="share-divider"><span>أو اكتب رأيك للميس</span></div>

        <form id="feedback-form" class="feedback-form" autocomplete="on">
          <label class="fb-label">الاسم</label>
          <input type="text" id="fb-name" name="name" required placeholder="اكتب اسمك" dir="rtl">

          <label class="fb-label">رأيك في الأكتيفيتي</label>
          <textarea id="fb-opinion" name="opinion" required rows="3" placeholder="إيه رأيك؟ سهلة؟ مفيدة؟ محتاجة تعديل؟" dir="rtl"></textarea>

          <label class="fb-label">هل أنت من طلابنا؟</label>
          <div class="fb-radio-group" dir="rtl">
            <label class="fb-radio">
              <input type="radio" name="student" value="طالب من طلابنا" required>
              <span>طالب من طلابنا</span>
            </label>
            <label class="fb-radio">
              <input type="radio" name="student" value="مش من طلابنا">
              <span>مش من طلابنا</span>
            </label>
          </div>

          <button type="submit" class="btn fb-submit" id="fb-send">
            ابعت واتس للميس
          </button>
        </form>
      </div>
    `;
    document.body.appendChild(modal);

    document.getElementById('share-close').addEventListener('click', closeShare);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeShare();
    });
    document.getElementById('share-copy').addEventListener('click', () => {
      const input = document.getElementById('share-link');
      input.select();
      navigator.clipboard?.writeText(input.value).catch(() => {
        try { document.execCommand('copy'); } catch (_) {}
      });
      toast('تم نسخ اللينك ✓');
    });
    document.getElementById('share-native').addEventListener('click', () => {
      const { title, url } = activityMeta();
      if (navigator.share) {
        navigator.share({ title, text: title + ' — Dr. Walaa El-Masry', url }).catch(() => {});
      }
    });
    document.getElementById('feedback-form').addEventListener('submit', onFeedbackSubmit);

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('active')) closeShare();
    });
  }

  function openShare() {
    ensureModal();
    const { title, url } = activityMeta();
    const text = `${title} — Interactive Activity | Dr. Walaa El-Masry · Programming & AI`;

    document.getElementById('share-title').textContent = title;
    document.getElementById('share-link').value = url;
    document.getElementById('share-wa').href =
      'https://wa.me/?text=' + encodeURIComponent(text + '\n' + url);
    document.getElementById('share-tg').href =
      'https://t.me/share/url?url=' + encodeURIComponent(url) + '&text=' + encodeURIComponent(text);
    document.getElementById('share-fb').href =
      'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url);
    document.getElementById('share-native').hidden = !navigator.share;

    // reset form
    const form = document.getElementById('feedback-form');
    form.reset();

    document.getElementById('share-modal').classList.add('active');
  }

  function closeShare() {
    document.getElementById('share-modal')?.classList.remove('active');
  }

  function onFeedbackSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('fb-name').value.trim();
    const opinion = document.getElementById('fb-opinion').value.trim();
    const student = document.querySelector('input[name="student"]:checked')?.value;
    const { title, url } = activityMeta();

    if (!name || !opinion || !student) {
      toast('من فضلك املأ كل الحقول');
      return;
    }

    const message =
`السلام عليكم مس ولاء 👋

📌 الاسم: ${name}
👤 الحالة: ${student}

📝 رأيي في أكتيفيتي «${title}»:
${opinion}

🔗 لينك الأكتيفيتي:
${url}

— مرسل من موقع الأنشطة`;

    const waUrl = 'https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(message);
    window.open(waUrl, '_blank', 'noopener');
    toast('هيتفتح واتساب… ابعت الرسالة للميس');
    closeShare();
  }

  function toast(msg) {
    let el = document.getElementById('toast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'toast';
      el.className = 'toast';
      el.setAttribute('role', 'status');
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.classList.add('show');
    clearTimeout(el._t);
    el._t = setTimeout(() => el.classList.remove('show'), 2800);
  }

  // Expose
  window.openActivityShare = openShare;
  window.closeActivityShare = closeShare;

  // Auto-bind share buttons
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('[data-share], #share-btn, .share-trigger').forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openShare();
      });
    });
  });
})();
