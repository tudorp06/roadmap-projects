//Base unit: length -> meter = 1
// => mm: 0.001, cm: 0.01, m: 1, km: 1000
// inch: 0.0254, foot: 0.3048, yard: 0.9144, mile: 1609.34



const factors = {
  "length": { "mm": 0.001, "cm": 0.01, "m": 1, "km": 1000, "inch": 0.0254, "foot": 0.3048 },
  "weight": { "mg": 0.001, "g": 1, "kg": 1000, "ounce": 28.349523125, "pound": 453.59237 },
  "temperature": { "C": 1, "K": 1, "F": 1 }
}; // each unit has value in meters

function convert(value, type, from, to) {
  if (type === "temperature") {
    let inC;
    if (from === "C") inC = value;
    else if (from === "F") inC = (value - 32) * 5 / 9;
    else if (from === "K") inC = (value - 273.15);
    if (to === "C") return inC;
    else if (to === "F") return inC * 9 / 5 + 32;
    else if (to === "K") return inC + 273.15;
  }
  else{
    const toBase = value*factors[type][from];
    return toBase / factors[type][to];
  }
}


const convertBtn = document.getElementById("convertBtn");
const type = document.getElementById("type");

type.addEventListener("change", () => {
  const newType = type.value;
  const fromSel = document.getElementById("from");
  const toSel = document.getElementById("to");
  fromSel.innerHTML = "";
  toSel.innerHTML = "";
  Object.keys(factors[newType]).forEach((unit) => {
      const o1 = document.createElement("option");
      o1.value = unit; o1.textContent = unit;
      fromSel.appendChild(o1);
      const o2 = document.createElement("option");
      o2.value = unit; o2.textContent = unit;
      toSel.appendChild(o2);
  })


});

convertBtn.addEventListener("click", () => {
  const resultText = document.getElementById("result");
  const fromValue = document.getElementById("from").value;
  const toValue = document.getElementById("to").value;
  const type = document.getElementById("type").value;
  const input = document.getElementById("value");
  const num = parseFloat(input.value);
  if (isNaN(num)) {
    resultText.innerText = "Enter a valid number";
    return;
  }
  const result = convert(num, type, fromValue, toValue);
  resultText.innerText = result;
});
