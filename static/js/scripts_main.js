/* Header */
let introH
try {
  introH = document.getElementById("intro").clientHeight + document.getElementById("photos__intro").clientHeight;
} catch (e) {
    introH = window.innerHeight / 2
  }
let scrollOffset = document.documentElement.scrollTop;
let header = document.getElementById("header_main");

chekScroll(scrollOffset);
window.addEventListener('scroll', function (event) {
  scrollOffset = window.pageYOffset
  chekScroll(scrollOffset);
});

function chekScroll(scrollOffset) {
  if ( scrollOffset >= introH ) {
      header.classList.add("fixed");
  } else {
      header.classList.remove("fixed");
  }
};


/* Menu nav toggle */
let nav_toggle = document.querySelector('#nav_toggle'),
    nav = document.querySelector('#nav');

function navToggle() {
  nav.classList.toggle("active");
  nav_toggle.classList.toggle("active");
}



/* Smooth scrol */
const anchors = document.querySelectorAll('a[href*="##"]')

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()

    const blockID = anchor.getAttribute('data-scroll').substr(1)

    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'center'
    })
  })
}
