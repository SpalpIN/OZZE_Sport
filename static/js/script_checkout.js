function shippingRatio() {
  let shippingChoice1 = document.getElementById("shippingChoice1");
  let novP = document.getElementById("novP");

  let shippingChoice2 = document.getElementById("shippingChoice2");
  let avtolux = document.getElementById("avtolux");

  let shippingChoice3 = document.getElementById("shippingChoice3");
  let ukrPoshta = document.getElementById("ukrPoshta");

  // If the checkbox is checked, display the output text
  if (shippingChoice1.checked == true){
    novP.style.display = "block";
  } else {
    novP.style.display = "none";
  }

  if (shippingChoice2.checked == true){
    avtolux.style.display = "block";
  } else {
    avtolux.style.display = "none";
  }

  if (shippingChoice3.checked == true){
    ukrPoshta.style.display = "block";
  } else {
    ukrPoshta.style.display = "none";
  }
}

let totalPrice = document.getElementById("totalPrice");
let prices = document.querySelectorAll('.productPrice');
let quantities = document.querySelectorAll('.productQuantity');
let priceRes = 0;


for (let i of prices) {
  priceRes += parseInt(i.textContent, 10);
}
totalPrice.value = priceRes;

for (let i=0;i<quantities.length; i++) {
    quantities[i].setAttribute('name', 'quan' + i);
}

for (let quantity of quantities) {
    quantity.oninput = function() {
        priceRes = 0;
        for (let i = 0; i < prices.length ; i++) {
          priceRes += parseInt(prices[i].textContent, 10) * quantities[i].value;
        }
        totalPrice.value = priceRes;
    };
}

