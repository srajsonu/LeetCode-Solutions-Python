class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if self.big >= 1:
            if carType == 1:
                self.big -= 1
                return True
        if self.medium >= 1:
            if carType == 2:
                self.medium -= 1
                return True
        if self.small >= 1:
            if carType == 3:
                self.small -= 1
                return True
        return False
