from models.House import House

class Infrastructure(House):

    def __init__(self, area, price, rating, adress, numberOfRooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.numberOfRooms = numberOfRooms
        self.city = city

    @property
    def get_isParking(self):
        return self.isParking        
        
    def set_isParking(self, x):
        self.isParking = x
        
    @property
    def get_locatedNear(self):
        return self.locatedNear        
        
    def set_locatedNear(self, x):
        self.locatedNear = x