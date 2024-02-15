/*Take a phrase like ‘turpentine and turtles’ and translate it into its “whale talk” equivalent: ‘UUEEIEEAUUEE’.

There are a few simple rules for translating text to whale language:

    There are no consonants. Only vowels excluding “y”.
    The u‘s and e‘s are extra long, so we must double them in our program.

Once we have converted text to the whale language, the result is sung slowly, as is a custom in the ocean. */

const input = 'good morning neighbour';
const vowels = ['a', 'e', 'i', 'o', 'u'];
const resultArray = [];

for (let i = 0; i  < input.length; i++){
  for ( let j = 0; j < vowels.length; j++){
    if (input[i] === vowels[j]){
      console.log(`match found: ${vowels[j]}`);
      resultArray.push(vowels[j]);
      if (vowels[j] === 'e'){
        resultArray.push('e');
      } else if (vowels[j] === 'u'){
        resultArray.push('u');
      }
    }
  }
}
console.log(resultArray);
const resultString = resultArray.join('').toUpperCase();
console.log(resultString)



// I believe this works the same, and no IFs are needed:
// I just duplicated the vowels to double in the vowels
const input = 'good morning neighbour';
const vowels = ['a', 'e','e', 'i', 'o', 'u', 'u'];
const resultArray = [];

for (let i = 0; i  < input.length; i++){
  for ( let j = 0; j < vowels.length; j++){
    if (input[i] === vowels[j]){
      console.log(`match found: ${vowels[j]}`);
      resultArray.push(vowels[j]);
    }
  }
}
console.log(resultArray);
const resultString = resultArray.join('').toUpperCase();
console.log(resultString)