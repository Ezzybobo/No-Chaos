const prompt = require("prompt-sync")();

let number = Number(prompt("Enter your average: "));
let average = 0;

while(number != -1) {
average = number;
number = Number(prompt("Enter your average: "));
}
console.log(average);
