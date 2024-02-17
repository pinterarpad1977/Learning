const team = {
  _players : [
    {firstName: 'Bob', lastName: 'Pinkerton', age: 48},
    {firstName: 'Bill', lastName: 'Packard', age: 47},
    {firstName: 'Joe', lastName: 'Sidetrack', age: 45}
  ],
  _games : [
    {opponent: 'LA Killers', teamPoints: 12, opponentPoints: 21},
    {opponent: 'Furry Five', teamPoints: 43, opponentPoints: 1},
    {opponent: 'Thirsty Three', teamPoints: 30, opponentPoints: 21}
  ],
get players() {
  return this._players;
},
get games() {
  return this._games;
},
addPlayer(newFirstName, newLastName, newAge) {
  const newPlayer = {firstName: newFirstName, lastName: newLastName, age: newAge};
  this._players.push(newPlayer);
},
addGame(newOpponent, newTeamPoints, newOpponentPoints) {
  const newGame = {
    opponent: newOpponent, teamPoints: newTeamPoints, opponentPoints: newOpponentPoints};
    this._games.push(newGame);
}

};

team.addPlayer('Gina', 'Suckova', 28);
team.addGame('Titans', 100, 98);
const playerValues = team.players.map(player => Object.values(player));
console.log(playerValues);
console.log(team.games);