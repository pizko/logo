/* Медленный параллакс декоративных пластилиновых объектов (data-depth). Только мышь и широкий экран. */
(function () {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches || innerWidth < 960) return;
  var objs = [].slice.call(document.querySelectorAll('[data-depth]'));
  if (!objs.length) return;
  var mx = 0, my = 0, pending = false;
  function apply() {
    pending = false;
    objs.forEach(function (o) {
      var k = parseFloat(o.dataset.depth) || 0;
      o.style.transform = 'translate(' + (mx * k * 18).toFixed(1) + 'px,' + (my * k * 14).toFixed(1) + 'px)';
    });
  }
  addEventListener('pointermove', function (e) {
    mx = e.clientX / innerWidth - 0.5; my = e.clientY / innerHeight - 0.5;
    if (!pending) { pending = true; requestAnimationFrame(apply); }
  }, { passive: true });
})();
