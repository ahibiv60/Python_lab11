from managers.HouseManagerImpl import HouseManagerImpl
from models.Mansion import Mansion
from models.Penthouse import Penthouse
from models.Apartment import Apartment

def main():    
    h = HouseManagerImpl()
    
    house1 = Mansion(155, 11465432, 5, 'Warsaw, 5', 6, 'Lviv')
    house2 = Penthouse(136, 2383150, 4, 'Charles Michelosh, 7', 4, 'Kiev')
    house3 = Apartment(100, 530400, 3, 'Solomyanska, 20A', 2, 'Odessa')
    h.addHouse(house1)
    h.addHouse(house2)
    h.addHouse(house3)    
    
    h.printListOfHouses()
    print("\n"+"."*20)
    h.sortByArea(True)
    h.printListOfHouses()
    print("\n"+"."*20)
    h.sortByPrice(False)
    h.printListOfHouses()
    
    h.findPropositionByCity('Lviv');

if __name__ == "__main__": main()