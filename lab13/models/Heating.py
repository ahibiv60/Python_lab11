from enum import Enum

class Heating(Enum):
    CENTRAL_SYSTEM = "CENTRAL_SYSTEM" 
    ELECTRIC_BOILER = "ELECTRIC_BOILER"
    GAS_BOILER = "GAS_BOILER"
    HEAT_PUMP = "HEAT_PUMP"