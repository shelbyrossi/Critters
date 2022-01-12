from datetime import date


class Lion():
    
    def __init__(self, id, name, species, shift, food):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        self.shift = shift
        self.food = food
        
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
        
new_lion = Lion(1, "Bob", "Lion", "morning", "meat")
print(f'{new_lion.name} the {new_lion.species} is available to be pet during the {new_lion.shift} shift')
new_lion.feed()

        
        
class Elephant(): 
    
    def __init__(self, id, name, species, shift): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        self.shift = shift 
        
class Tiger(): 
    
    def __init__(self, id, name, species, shift): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        self.shift = shift 
        
class Bear():
    
    def __init__(self, id, name, species, shift): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        self.shift = shift         
class Monkey():
    
    def __init__(self, id, name, species, shift): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        self.shift = shift 
        
        