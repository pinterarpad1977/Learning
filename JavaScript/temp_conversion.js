// this is a constant
const kelvin = 297;
// celsius ia the same scale but 273 degrees colder
const celsius = kelvin-273;
// Fahrenheit = Celsius * (9/5) + 32 - we will round it that is why it is created by let
let fahrenheit = celsius *(9 / 5) + 32;
fahrenheit = Math.floor(fahrenheit);
// the newton scale is Newton = Celsius * (33/100)
let newton = celsius * (33 / 100);
console.log(`The temperature is ${fahrenheit} fahrenheit`);
console.log(`The temperature is ${newton} on the newton scale`)
