// myAge is the years how old I am
const myAge = 47;
// earlyYears has a different factor than the laterYears
let earlyYears = 2;
// the first 2 years has a factor of 10.5 in dog years
earlyYears *= 10.5;
// laterYears are the ones after the first 2 years
laterYears = myAge-2;
// later years count 4 times in dog years
laterYears *= 4
// so my age in dog years is the sum of the early and the later years
let myAgeInDogYears = earlyYears + laterYears
// i have no clue why myName must be lowercase but that's what the code below does
const myName = 'RP'.toLowerCase()

console.log(`My name is: ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years`)
