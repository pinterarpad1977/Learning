import random

class Player:
  def __init__(self, name, level = 0, armor = 0):
    self.name = name
    self.life = random.randint(30,100)
    self.strength = random.randint(10,30)
    self.level = level
    self.armor = armor
  
  def __repr__(self):
    return f'I am {self.name}, my attributes are:'+'\n'+ f'- life: {self.life}'+'\n'+f'- strength: {self.strength}'+'\n'+f'- armor: {self.armor}'+'\n'+f'- level: {self.level}'

  def get_attack_power(self):
    self.attack_power = (self.life + self.armor) * self.strength
    return self.attack_power

  def battle(self, mob):
    outcome = self.get_attack_power() - mob.get_attack_power()
    if outcome < 0:
      return f'{self.name} was slain by {mob.breed}'
    else :
      return f'{self.name} killed {mob.breed}'

class Mob():
  def __init__(self, breed, player, elite = False):
    self.breed = breed
    self.elite = elite
    if self.elite:
      multiplier = 1.6
    else:
      multiplier = 1
    self.life = int(player.life * random.randint(9,11) / 10 * multiplier)
    self.strength = int(player.strength *random.randint(9,11) / 10 * multiplier)
    self.armor = int(player.armor * random.randint(9,11) / 10 * multiplier)
    self.level = player.level + random.randint(-1,1)

  def __repr__(self):
    return f'I am {self.breed}, my attributes are:'+'\n'+ f'- life: {self.life}'+'\n'+f'- strength: {self.strength}'+'\n'+f'- armor: {self.armor}'+'\n'+f'- level: {self.level}'+'\n'+ f'I\'m an elite: {self.elite}'

  def get_attack_power(self):
    self.attack_power = (self.life + self.armor) * self.strength
    return self.attack_power

ragnar = Player('ragnar', level = 1, armor = 100)
beholder = Mob('beholder',ragnar)

print(ragnar)
print(beholder)
print(ragnar.battle(beholder))
