/**
 * Family Wedding Centre — Main JavaScript
 * Vanilla JS only. No frameworks.
 */

'use strict';

/* ─── Utility Helpers ────────────────────────────────────────── */
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

/* ─── DOM Ready ──────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileMenu();
  initHeroCarousel();
  initStatCounters();
  initEnquiryForm();
  initLazyImages();
  initSmoothScroll();
  initScrollReveal();
});

/* ═══════════════════════════════════════════════════════════════
   1. STICKY HEADER — scroll shadow
═══════════════════════════════════════════════════════════════ */
function initStickyHeader() {
  const header = $('#site-header');
  if (!header) return;

  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 20);
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // run once on load
}

/* ═══════════════════════════════════════════════════════════════
   2. MOBILE MENU — hamburger toggle with accessibility
═══════════════════════════════════════════════════════════════ */
function initMobileMenu() {
  const btn     = $('#hamburger-btn');
  const menu    = $('#mobile-menu');
  const overlay = $('#mobile-overlay');
  if (!btn || !menu) return;

  let isOpen = false;

  function openMenu() {
    isOpen = true;
    btn.classList.add('is-open');
    btn.setAttribute('aria-expanded', 'true');
    menu.classList.add('is-open');
    menu.setAttribute('aria-hidden', 'false');
    if (overlay) { overlay.classList.add('is-visible'); overlay.setAttribute('aria-hidden', 'false'); }
    document.body.style.overflow = 'hidden';
    // Focus first link
    const firstLink = menu.querySelector('.mobile-nav-link');
    if (firstLink) firstLink.focus();
  }

  function closeMenu() {
    isOpen = false;
    btn.classList.remove('is-open');
    btn.setAttribute('aria-expanded', 'false');
    menu.classList.remove('is-open');
    menu.setAttribute('aria-hidden', 'true');
    if (overlay) { overlay.classList.remove('is-visible'); overlay.setAttribute('aria-hidden', 'true'); }
    document.body.style.overflow = '';
    btn.focus();
  }

  btn.addEventListener('click', () => isOpen ? closeMenu() : openMenu());
  if (overlay) overlay.addEventListener('click', closeMenu);

  // Close on Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen) closeMenu();
  });

  // Close when a mobile nav link is clicked
  $$('.mobile-nav-link', menu).forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}

/* ═══════════════════════════════════════════════════════════════
   3. HERO CAROUSEL — auto-advance with arrow & dot controls
═══════════════════════════════════════════════════════════════ */
function initHeroCarousel() {
  const slidesWrap = $('#heroSlides');
  if (!slidesWrap) return;

  const slides   = $$('.hero-slide', slidesWrap);
  const dots     = $$('.hero-dot');
  const prevBtn  = $('#heroPrev');
  const nextBtn  = $('#heroNext');

  if (slides.length < 2) {
    if (prevBtn) prevBtn.style.display = 'none';
    if (nextBtn) nextBtn.style.display = 'none';
    return;
  }

  let current  = 0;
  let autoPlay = null;
  const INTERVAL = 5500;

  function goTo(index) {
    slides[current].classList.remove('active');
    if (dots[current]) { dots[current].classList.remove('active'); dots[current].setAttribute('aria-selected', 'false'); }

    current = (index + slides.length) % slides.length;

    slides[current].classList.add('active');
    if (dots[current]) { dots[current].classList.add('active'); dots[current].setAttribute('aria-selected', 'true'); }
  }

  function startAuto() {
    clearInterval(autoPlay);
    autoPlay = setInterval(() => goTo(current + 1), INTERVAL);
  }

  function stopAuto() { clearInterval(autoPlay); }

  if (prevBtn) prevBtn.addEventListener('click', () => { goTo(current - 1); stopAuto(); startAuto(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { goTo(current + 1); stopAuto(); startAuto(); });

  dots.forEach((dot, i) => {
    dot.addEventListener('click', () => { goTo(i); stopAuto(); startAuto(); });
  });

  // Pause on hover / touch
  slidesWrap.addEventListener('mouseenter', stopAuto);
  slidesWrap.addEventListener('mouseleave', startAuto);

  // Swipe support
  let touchStartX = 0;
  slidesWrap.addEventListener('touchstart', (e) => { touchStartX = e.changedTouches[0].clientX; }, { passive: true });
  slidesWrap.addEventListener('touchend', (e) => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) { goTo(diff > 0 ? current + 1 : current - 1); stopAuto(); startAuto(); }
  });

  startAuto();
}

/* ═══════════════════════════════════════════════════════════════
   4. STAT COUNTERS — Intersection Observer animated counters
═══════════════════════════════════════════════════════════════ */
function initStatCounters() {
  const statNums = $$('.stat-number[data-target]');
  if (!statNums.length || !window.IntersectionObserver) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      observer.unobserve(entry.target);

      const el     = entry.target;
      const target = parseInt(el.dataset.target, 10);
      const suffix = el.textContent.replace(/[\d,]+/, '');
      const start  = Date.now();
      const dur    = 1800;

      function easeOut(t) { return 1 - Math.pow(1 - t, 3); }

      function tick() {
        const elapsed = Date.now() - start;
        const progress = Math.min(elapsed / dur, 1);
        const val = Math.round(easeOut(progress) * target);

        if (target >= 1000000) {
          el.textContent = (val / 1000000).toFixed(0) + 'M+';
        } else if (target >= 1000) {
          el.textContent = (val / 1000).toFixed(0) + 'K+';
        } else {
          el.textContent = val + suffix;
        }

        if (progress < 1) requestAnimationFrame(tick);
      }

      requestAnimationFrame(tick);
    });
  }, { threshold: 0.5 });

  statNums.forEach(el => observer.observe(el));
}

/* ═══════════════════════════════════════════════════════════════
   5. ENQUIRY FORM — AJAX submit + success state
═══════════════════════════════════════════════════════════════ */
function initEnquiryForm() {
  const form = $('#enquiry-form');
  if (!form) return;

  const submitBtn  = $('#enquiry-submit');
  const btnText    = submitBtn ? $('.btn-text', submitBtn) : null;
  const btnLoading = submitBtn ? $('.btn-loading', submitBtn) : null;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Clear previous errors
    $$('.form-error', form).forEach(el => el.remove());
    $$('.form-input', form).forEach(el => el.classList.remove('has-error'));

    // Client-side validation
    if (!clientValidate(form)) return;

    // Show loading state
    if (submitBtn) submitBtn.disabled = true;
    if (btnText)    btnText.hidden    = true;
    if (btnLoading) btnLoading.hidden = false;

    try {
      const formData = new FormData(form);
      const resp = await fetch(form.action || window.location.href, {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        body: formData,
      });

      const data = await resp.json();

      if (data.success) {
        showFormSuccess(form, data.message || 'Thank you! We will contact you shortly.');
      } else if (data.errors) {
        showFormErrors(form, data.errors);
      }
    } catch {
      showInlineError(form, 'Something went wrong. Please try again or call us directly.');
    } finally {
      if (submitBtn) submitBtn.disabled = false;
      if (btnText)    btnText.hidden    = false;
      if (btnLoading) btnLoading.hidden = true;
    }
  });
}

function clientValidate(form) {
  let valid = true;

  const name  = form.querySelector('input[name="name"]');
  const phone = form.querySelector('input[name="phone"]');
  const msg   = form.querySelector('textarea[name="message"]');

  if (name && name.value.trim().length < 2) {
    addFieldError(name, 'Please enter your full name.'); valid = false;
  }
  if (phone && phone.value.trim().replace(/\D/g, '').length < 7) {
    addFieldError(phone, 'Please enter a valid phone number.'); valid = false;
  }
  if (msg && msg.value.trim().length < 3) {
    addFieldError(msg, 'Please enter a message.'); valid = false;
  }

  return valid;
}

function addFieldError(input, message) {
  input.classList.add('has-error');
  const err = document.createElement('span');
  err.className = 'form-error';
  err.setAttribute('role', 'alert');
  err.textContent = message;
  input.parentNode.appendChild(err);
}

function showFormErrors(form, errors) {
  Object.entries(errors).forEach(([field, messages]) => {
    const input = form.querySelector(`[name="${field}"]`);
    if (input) addFieldError(input, Array.isArray(messages) ? messages[0] : messages);
  });
}

function showInlineError(form, message) {
  const err = document.createElement('div');
  err.className = 'form-error form-error--general';
  err.setAttribute('role', 'alert');
  err.textContent = message;
  form.prepend(err);
}

function showFormSuccess(form, message) {
  const card = form.closest('.enquiry-form-card');
  if (card) {
    card.innerHTML = `
      <div class="form-success" role="alert" style="flex-direction:column;align-items:center;text-align:center;padding:3rem 2rem;">
        <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="color:#16a34a;margin-bottom:1rem;">
          <path d="M22 11.08V12a10 10 0 11-5.93-9.14"/>
          <polyline points="22 4 12 14.01 9 11.01"/>
        </svg>
        <strong style="font-size:1.5rem;color:#2D0A4E;font-family:'Cormorant Garamond',serif;">Enquiry Received!</strong>
        <p style="color:#6B5E57;margin-top:0.75rem;">${message}</p>
        <p style="color:#9E8E85;font-size:0.875rem;margin-top:0.5rem;">Our team will get in touch with you within 24 hours.</p>
      </div>`;
  } else {
    showInlineError(form, message);
  }
}

/* ═══════════════════════════════════════════════════════════════
   6. LAZY IMAGES — native + fallback observer
═══════════════════════════════════════════════════════════════ */
function initLazyImages() {
  if ('loading' in HTMLImageElement.prototype) return; // native lazy load handles it

  const imgs = $$('img[loading="lazy"]');
  if (!imgs.length || !window.IntersectionObserver) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const img = entry.target;
      if (img.dataset.src) { img.src = img.dataset.src; delete img.dataset.src; }
      observer.unobserve(img);
    });
  }, { rootMargin: '200px 0px' });

  imgs.forEach(img => observer.observe(img));
}

/* ═══════════════════════════════════════════════════════════════
   7. SMOOTH SCROLL — anchor links
═══════════════════════════════════════════════════════════════ */
function initSmoothScroll() {
  $$('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const target = document.getElementById(link.getAttribute('href').slice(1));
      if (!target) return;
      e.preventDefault();
      const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--header-height') || '80', 10);
      const top = target.getBoundingClientRect().top + window.scrollY - offset - 16;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
}

/* ═══════════════════════════════════════════════════════════════
   8. SCROLL REVEAL — subtle fade-in on scroll
═══════════════════════════════════════════════════════════════ */
function initScrollReveal() {
  if (!window.IntersectionObserver) return;

  // Add reveal class to qualifying sections
  const revealTargets = $$(
    '.collection-card, .store-card, .brand-item, .about-value, .contact-detail-card, .gallery-preview-item'
  );

  revealTargets.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = `opacity 0.5s ease ${(i % 6) * 60}ms, transform 0.5s ease ${(i % 6) * 60}ms`;
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  revealTargets.forEach(el => observer.observe(el));
}

/* ─── CSS helper for has-error ───────────────────────────────── */
(function addHasErrorStyle() {
  const style = document.createElement('style');
  style.textContent = `
    .form-input.has-error {
      border-color: #D63B3B !important;
      box-shadow: 0 0 0 3px rgba(214, 59, 59, 0.1) !important;
    }
  `;
  document.head.appendChild(style);
})();
