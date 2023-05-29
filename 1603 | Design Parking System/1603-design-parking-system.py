class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.lookup = { 1: big, 2: medium, 3: small }
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        self.lookup[carType] -= 1
        return self.lookup[carType] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
