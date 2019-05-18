from models.House import House
 
class Mansion(House):
    
    def __init__(self, area, price, rating, adress, numberOfRooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.numberOfRooms = numberOfRooms
        self.city = city
        
    @property
    def get_waterSupply(self):
        return self.waterSupply        
        
    def set_waterSupply(self, x):
        self.waterSupply = x
    
    @property
    def get_floors(self):
        return self.floors       
        
    def set_floors(self, x):
        self.floors = x