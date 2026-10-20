// Mobile nav
var burger = document.querySelector('.burger');
var mainNav = document.querySelector('nav.main');
if (burger && mainNav) {
  burger.addEventListener('click', function () {
    mainNav.classList.toggle('open');
  });
}

// Count-up impact numbers
var counted = false;
function countUp() {
  if (counted) return;
  var el = document.querySelector('.impact');
  if (!el) return;
  var r = el.getBoundingClientRect();
  if (r.top > window.innerHeight) return;
  counted = true;
  document.querySelectorAll('.impact .num').forEach(function (n) {
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

// Donation / volunteer forms (demo: front-end only)
document.querySelectorAll('form.demo-form').forEach(function (f) {
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    var t = f.querySelector('.thanks');
    if (t) { t.style.display = 'block'; t.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
    f.querySelectorAll('input,select,textarea').forEach(function (i) { i.value = ''; });
  });
});

// Donation amount picker
document.querySelectorAll('.amounts').forEach(function (box) {
  var input = box.closest('form') ? box.closest('form').querySelector('[name=amount]') : null;
  box.querySelectorAll('button').forEach(function (b) {
    b.addEventListener('click', function () {
      box.querySelectorAll('button').forEach(function (x) { x.classList.remove('sel'); });
      b.classList.add('sel');
      if (input) input.value = b.getAttribute('data-amt');
    });
  });
});

// Zakat calculator
function calcZakat() {
  function v(id) { var e = document.getElementById(id); return e ? (parseFloat(e.value) || 0) : 0; }
  var goldPrice = v('zk-gold-price');
  var nisab = 87.48 * goldPrice; // 7.5 tola gold
  var wealth = v('zk-cash') + v('zk-gold-val') + v('zk-silver-val') + v('zk-business') - v('zk-debts');
  var out = document.getElementById('zk-out');
  if (!out) return;
  if (goldPrice <= 0) { out.innerHTML = 'Please enter today\'s gold price per tola to calculate.'; return; }
  if (wealth < nisab) {
    out.innerHTML = 'Your total zakat-able wealth is <b>Rs ' + wealth.toLocaleString('en-US') + '</b>, which is below the nisab of <b>Rs ' + Math.round(nisab).toLocaleString('en-US') + '</b>. Zakat is not obligatory on this amount — but any Sadaqah you give is still a great reward.';
    return;
  }
  var zakat = wealth * 0.025;
  out.innerHTML = 'Your Zakat is <span class="big">Rs ' + Math.round(zakat).toLocaleString('en-US') + '</span><br>Total zakat-able wealth: Rs ' + Math.round(wealth).toLocaleString('en-US') + ' · Nisab: Rs ' + Math.round(nisab).toLocaleString('en-US');
}
var zkBtn = document.getElementById('zk-btn');
if (zkBtn) zkBtn.addEventListener('click', calcZakat);
