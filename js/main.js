(function () {
  document.documentElement.classList.add("js");

  // mobile menu
  var nav = document.querySelector(".nav");
  var burger = document.querySelector(".burger");
  if (nav && burger) {
    burger.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      burger.setAttribute("aria-expanded", open);
    });
    nav.querySelectorAll(".menu a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("open");
        burger.setAttribute("aria-expanded", "false");
      });
    });
  }

  // reveal on scroll
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // lightbox
  var links = Array.prototype.slice.call(document.querySelectorAll("a[data-full]"));
  if (!links.length) return;

  var lb = document.createElement("div");
  lb.className = "lb";
  lb.setAttribute("role", "dialog");
  lb.setAttribute("aria-modal", "true");
  lb.setAttribute("aria-label", "Image viewer");
  lb.innerHTML =
    '<span class="count"></span>' +
    '<button class="x" aria-label="Close">&times;</button>' +
    '<button class="p" aria-label="Previous image">&#8249;</button>' +
    '<img alt="">' +
    '<button class="n" aria-label="Next image">&#8250;</button>' +
    '<div class="cap"></div>';
  document.body.appendChild(lb);

  var img = lb.querySelector("img");
  var cap = lb.querySelector(".cap");
  var count = lb.querySelector(".count");
  var idx = 0, last = null;

  function show(i) {
    idx = (i + links.length) % links.length;
    var a = links[idx];
    var thumb = a.querySelector("img");
    img.src = thumb.currentSrc || thumb.src;      // show the already-loaded thumbnail instantly
    img.alt = thumb.alt;
    var full = new Image();
    full.onload = function () { if (links[idx] === a) img.src = a.dataset.full; };
    full.src = a.dataset.full;
    cap.textContent = a.dataset.caption || thumb.alt;
    count.textContent = links.length > 1 ? (idx + 1) + " / " + links.length : "";
  }
  function open(i) {
    last = document.activeElement;
    show(i);
    lb.classList.add("on");
    document.body.style.overflow = "hidden";
    lb.querySelector(".x").focus();
  }
  function close() {
    lb.classList.remove("on");
    document.body.style.overflow = "";
    img.removeAttribute("src");
    if (last) last.focus();
  }

  links.forEach(function (a, i) {
    a.addEventListener("click", function (e) { e.preventDefault(); open(i); });
  });
  lb.querySelector(".x").addEventListener("click", close);
  lb.querySelector(".p").addEventListener("click", function () { show(idx - 1); });
  lb.querySelector(".n").addEventListener("click", function () { show(idx + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
  document.addEventListener("keydown", function (e) {
    if (!lb.classList.contains("on")) return;
    if (e.key === "Escape") close();
    else if (e.key === "ArrowLeft") show(idx - 1);
    else if (e.key === "ArrowRight") show(idx + 1);
  });

  // swipe
  var sx = null;
  lb.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (sx === null) return;
    var dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    sx = null;
  });
})();
