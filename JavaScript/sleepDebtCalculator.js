// This is a really stupid program just to practise function creation and condiotionals
// I really want to get to the point where I can interact with the user

const getSleepHours = (day) => {
  switch (day) {
    case 'Monday' : return 7;
    case 'Tuesday' : return 6.5;
    case 'Wednesday' : return 7;
    case 'Thursday' : return 7;
    case 'Friday' : return 7;
    case 'Saturday' : return 8;
    case 'Sunday' : return 7.5;
    default: console.log('This is not a day of the week.');

  }
}

const getActualSleepHours = () => {
  const hoursSlept = getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday') +  getSleepHours('Sunday');
  return hoursSlept; 
}

const getIdealSleepHours = (hours) => {
  return hours * 7;
}

const calculateSleepDebt = (idealSleep) => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours(idealSleep);
  if (actualSleepHours === idealSleepHours) {
    console.log('You get the perfect amount of sleep');
  } else if (actualSleepHours > idealSleepHours) {
    console.log(`You sleep ${actualSleepHours-idealSleepHours} hour(s) more than needed`);
  } else if (actualSleepHours < idealSleepHours) {
    console.log(`You need to sleep ${idealSleepHours-actualSleepHours} hour(s) more`);
  }
}


console.log(calculateSleepDebt(10))