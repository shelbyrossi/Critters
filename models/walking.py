from datetime import date


class Lion():
    
    def __init__(self, id, name, species):
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        
new_lion= Lion(1, "Bob", "Lion")
print(new_lion.name)
        
        
class Elephant(): 
    
    def __init__(self, id, name, species): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        
class Tiger(): 
    
    def __init__(self, id, name, species): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        
class Bear():
    
    def __init__(self, id, name, species): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 
        
class Monkey():
    
    def __init__(self, id, name, species): 
        self.id = id
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True 