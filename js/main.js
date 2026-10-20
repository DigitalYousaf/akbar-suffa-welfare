// ---------- Navigation ----------
(function () {
  var burger = document.querySelector('.burger');
  var mainNav = document.querySelector('nav.main');
  if (!burger || !mainNav) return;

  burger.addEventListener('click', function () {
    var open = mainNav.classList.toggle('open');
    burger.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Mobile: tapping a parent item expands its submenu (accordion).
  // Desktop: submenus open on hover via CSS; clicks navigate normally.
  mainNav.querySelectorAll('li.has-drop > a.nl').forEach(function (link) {
    link.addEventListener('click', function (e) {
      if (window.innerWidth <= 1080) {
        e.preventDefault();
        var li = link.parentElement;
        var wasOpen = li.classList.contains('expanded');
        mainNav.querySelectorAll('li.expanded').forEach(function (x) { x.classList.remove('expanded'); });
        if (!wasOpen) li.classList.add('expanded');
      }
    });
  });

  // Tapping any real link inside the mobile panel closes the panel.
  mainNav.querySelectorAll('.drop a, a.nl:not(.parent-link)').forEach(function (a) {
    a.addEventListener('click', function () {
      if (window.innerWidth <= 1080) {
        mainNav.classList.remove('open');
        burger.classList.remove('open');
      }
    });
  });
})();

// ---------- Count-up impact numbers ----------
var counted = false;
function countUp() {
  if (counted) return;
  var el = document.querySelector('.impact');
  if (!el) return;
  if (el.getBoundingClientRect().top > window.innerHeight) return;
  counted = true;
  el.querySelectorAll('.num').forEach(function (n) {
    var target = parseInt(n.getAttribute('data-count'), 10) || 0;
    var start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / 1400, 1);
      n.textContent = Math.floor(target * p).toLocaleString('en-US') + (p === 1 ? '+' : '');
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  });
}
window.addEventListener('scroll', countUp, { passive: true });
countUp();

// ---------- Demo forms ----------
document.querySelectorAll('form.demo-form').forEach(function (f) {
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var t = f.querySelector('.thanks');
    if (t) { t.style.display = 'block'; t.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
    f.reset();
  });
});

// ---------- Donation amount picker ----------
document.querySelectorAll('.amounts').forEach(function (box) {
  var form = box.closest('form');
  var input = form ? form.querySelector('[name=amount]') : null;
  box.querySelectorAll('button').forEach(function (b) {
    b.addEventListener('click', function () {
      box.querySelectorAll('button').forEach(function (x) { x.classList.remove('sel'); });
      b.classList.add('sel');
      if (input) input.value = b.getAttribute('data-amt');
    });
  });
});

// ---------- Zakat calculator ----------
function calcZakat() {
  function v(id) { var e = document.getElementById(id); return e ? (parseFloat(e.value) || 0) : 0; }
  var goldPrice = v('zk-gold-price');
  var out = document.getElementById('zk-out');
  if (!out) return;
  if (goldPrice <= 0) { out.innerHTML = 'Please enter today\'s gold price per tola to calculate your Zakat.'; return; }
  var nisab = 87.48 * goldPrice;
  var wealth = v('zk-cash') + v('zk-gold-val') + v('zk-silver-val') + v('zk-business') - v('zk-debts');
  if (wealth < nisab) {
    out.innerHTML = 'Your zakat-able wealth is <b>Rs ' + Math.round(wealth).toLocaleString('en-US') + '</b> — below the nisab of <b>Rs ' + Math.round(nisab).toLocaleString('en-US') + '</b>. Zakat is not obligatory on this amount, though any Sadaqah you give still carries great reward.';
    return;
  }
  var zakat = wealth * 0.025;
  out.innerHTML = 'Your Zakat is <span class="big">Rs ' + Math.round(zakat).toLocaleString('en-US') + '</span><br>Total zakat-able wealth: Rs ' + Math.round(wealth).toLocaleString('en-US') + ' · Nisab: Rs ' + Math.round(nisab).toLocaleString('en-US');
}
var zkBtn = document.getElementById('zk-btn');
if (zkBtn) zkBtn.addEventListener('click', calcZakat);
