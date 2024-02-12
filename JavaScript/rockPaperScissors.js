console.log('hi');
const cheatCodes = ['bomb', 'lava', 'inferno']
const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
/* old version could not accommodate the list of cheatcodes
  switch (userInput) {
    case 'rock' : return userInput;
    break;
    case 'scissors': return userInput;
    break;
    case 'paper' : return userInput;
    break;
    case cheatCodes.includes(userInput) : return userInput;
    default: console.log('Invalid choice! Pick rock, scissors or paper')
  }
}*/
  if (cheatCodes.includes(userInput)) {
    return userInput;
  } else {
    switch (userInput) {
      case 'rock':
      case 'scissors':
      case 'paper':
        return userInput;
      default:
        console.log('Invalid choice! Pick rock, scissors, or paper');
    }
  }
}

const getComputerChoice = function() {
  let choice = Math.floor(Math.random()*3);
  switch (choice){
    case 0 : return 'rock';
    break;
    case 1 : return 'scissors';
    break;
    case 2 : return 'paper';
    break;
    default: console.log(choice)
  }
}

// nested IFs are crazy with these figging curly braces.
// very important to remember to put the condition within brackets!
const determineWinner = function (userChoice, computerChoice) {
  if (cheatCodes.includes(userChoice)) { return 'Player won, but cheated!' };
  if (userChoice === computerChoice) { return 'draw' };
  if (userChoice === 'paper')  {
    if (computerChoice === 'rock')  { 
      return 'Player won';
    } else { 
      return 'Computer won';
    }
  }
  else if (userChoice === 'rock') {
    if (computerChoice === 'scissors')  { 
      return 'Player won';
    } else { 
      return 'Computer won';
    }
  }
  else if (userChoice === 'scissors')  {
    if (computerChoice === 'paper')  {
      return 'Player won';
    } else { 
      return 'Computer won';
    }
  }
  }

const playGame = function () {
  const userChoice = getUserChoice('lava');
  console.log(`Player: ${userChoice}`);
  const computerChoice = getComputerChoice();
  console.log(`Computer: ${computerChoice}`);
  console.log(determineWinner(userChoice, computerChoice))
}

//console.log(getUserChoice('rocK'))
//console.log(getComputerChoice())
//console.log(determineWinner('rock', 'rock'))

playGame()