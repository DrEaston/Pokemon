import random

class Pokemon:
  def __init__(self):
    self.attack=random.randint(0,15)
    self.defense=random.randint(0,15)
    self.hp=random.randint(0,15)
    self.health=100
    self.type="Water"

class Fire(Pokemon):
  def __init__(self):
    moves=["fireblast","firespin","flamethrower"]
    randMove=random.randint(0,len(moves)-1)
    self.moveset=moves[randMove]
    self.type="Fire"
    super().__init__()

class Water(Pokemon):
  def __init__(self):
    moves=["Bubble Beam","Water Gun","Hydro Cannon"]
    randMove=random.randint(0,len(moves)-1)
    self.moveset=moves[randMove]
    super().__init__()

somePoke=Fire()

Dean=Water()
Ethan=Fire()