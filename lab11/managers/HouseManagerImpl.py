import sys
sys.path.insert(0,'D:\\Python\\labs\\Python-Lab-11\\__main__\\python\\ua\\lviv\\iot\\airline\\models')

class HouseManagerImpl:
    house_list = []
    
    @staticmethod
    def getList():
        return HouseManagerImpl.house_list

    @staticmethod
    def sortByArea(is_reversed):
        HouseManagerImpl.house_list.sort(key=lambda house: house.area, reverse=is_reversed)
            
    @staticmethod    
    def sortByPrice(is_reversed):
        HouseManagerImpl.house_list.sort(key=lambda house: house.price, reverse=is_reversed)
            
    @staticmethod    
    def setNewListOfHouses(houses):
        HouseManagerImpl.house_list = houses
    
    @staticmethod
    def clearHouses():
        HouseManagerImpl.house_list.clear()
    
    @staticmethod
    def addHouse(house):
        HouseManagerImpl.house_list.append(house)
    
    @staticmethod
    def printListOfHouses():
        for v in HouseManagerImpl.house_list:
            print("adress: %s, city: %s\n" % (v.get_adress, v.get_city))
            
    @staticmethod
    def findPropositionByCity(city):
        houses.stream().filter(x -> city.equals(x.getCity())).collect(Collectors.toList());