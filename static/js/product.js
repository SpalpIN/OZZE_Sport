
/* Slider */
let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block";
}

/* Modal */
let sizeModal = document.getElementById("sizeModal");
let sizeBtn = document.getElementById("sizeBtn");
let span2 = document.getElementsByClassName("img__close")[0];
let span = document.getElementsByClassName("close")[2];
let span3 = document.getElementsByClassName("close")[0];
let span4 = document.getElementsByClassName("close")[1];

let imgModal = document.getElementById("myImgModal");
let img = document.getElementById("productImg1");
let img2 = document.getElementById("productImg2");
let modalImg = document.getElementById("img01");
let captionText = document.getElementById("caption");

let oneClickModal = document.getElementById("oneClickModal");
let oneClickBtn = document.getElementById("oneClickBtn");

let shippingModal = document.getElementById("shippingModal");
let shippingBtn = document.getElementById("shippingBtn");

shippingBtn.onclick = function() {
  shippingModal.style.display = "block";
  document.body.style.overflow = 'hidden'
}

oneClickBtn.onclick = function() {
  oneClickModal.style.display = "block";
  document.body.style.overflow = 'hidden'
}

img.onclick = function() {
  imgModal.style.display = "block";
  document.body.style.overflow = 'hidden'
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

img2.onclick = function() {
  imgModal.style.display = "block";
  document.body.style.overflow = 'hidden'
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

sizeBtn.onclick = function() {
  sizeModal.style.display = "block";
  document.body.style.overflow = 'hidden'
}

span.onclick = function() {
  sizeModal.style.display = "none";
  document.body.style.overflow = 'visible'
}

span2.onclick = function() {
  imgModal.style.display = "none";
    document.body.style.overflow = 'visible'
}

span3.onclick = function() {
  oneClickModal.style.display = "none";
    document.body.style.overflow = 'visible'
}

span4.onclick = function() {
  shippingModal.style.display = "none";
    document.body.style.overflow = 'visible'
}

window.onclick = function(event) {
  if (event.target === shippingModal) {
    shippingModal.style.display = "none";
    document.body.style.overflow = 'visible'
  }
  if (event.target === oneClickModal) {
    oneClickModal.style.display = "none";
    document.body.style.overflow = 'visible'
  }
  if (event.target === sizeModal) {
    sizeModal.style.display = "none";
    document.body.style.overflow = 'visible'
  }
  if (event.target === imgModal) {
    imgModal.style.display = "none";
    document.body.style.overflow = 'visible'
  }
}

function oneClickDone() {
    let oneClickPhone = document.getElementById('oneClickPhone').value;
      if (isNaN(parseInt(oneClickPhone, 10))) {
           alert('Укажите корректный номер');
      } else {
          alert('Заявка оформлена успешно. Мы вам перезвоним!');
      }
}