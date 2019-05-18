from models.House import House
 
class Apartment(House):
    
    def __init__(self, area, price, rating, adress, numberOfRooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.numberOfRooms = numberOfRooms
        self.city = city
        
    @property
    def get_flour(self):
        return self.flour        
        
    def set_flour(self, x):
        self.flour = x