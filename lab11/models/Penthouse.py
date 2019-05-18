from models.House import House
 
class Penthouse(House):
    
    def __init__(self, area, price, rating, adress, numberOfRooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.numberOfRooms = numberOfRooms
        self.city = city
        
    @property
    def is_terrace(self):
        return self.terrace        
        
    def set_terrace(self, x):
        self.terrace = x