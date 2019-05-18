import os

class House:
    
    def __init__(self, area, price, rating, adress, numberOfRooms, city):
        self.area = area
        self.price = price
        self.rating = rating
        self.adress = adress
        self.numberOfRooms = numberOfRooms
        self.city = city
    
    def __repr__(self):
        return repr((self.area, self.price, self.rating, self.adress, self.numberOfRooms, self.city))    
        
    @property
    def get_area(self):
        return self.area        
    
    def set_area(self, x):
        self.area = x
        
    @property
    def get_price(self):
        return self.price

    def set_price(self, x):
        self.price = x
        
    @property
    def get_rating(self):
        return self.rating

    def set_rating(self, x):
        self.rating = x
        
    @property
    def get_adress(self):
        return self.adress

    def set_adress(self, x):
        self.adress = x
        
    @property
    def get_numberOfRooms(self):
        return self.numberOfRooms

    def set_numberOfRooms(self, x):
        self.numberOfRooms = x
        
    @property
    def get_city(self):
        return self.city

    def set_city(self, x):
        self.city = x
        
def main():
    house = House(155, 11465432, 5, 'Warsaw, 5', 6, 'Lviv')
    
    print(house.get_city)
    house.set_city("Kiev")
    print(house.get_city)

if __name__ == "__main__": main()

os.system("PAUSE")