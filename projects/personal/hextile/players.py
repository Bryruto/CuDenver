class Player:
    def __init__(self,name,health,strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def show_player_stats(self):
        print(f"Name: {self.name}\nHealth: {self.health}\nStrength: {self.strength}")