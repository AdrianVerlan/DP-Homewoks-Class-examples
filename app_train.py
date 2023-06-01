class Wagon:
    def __init__(self, number):
        if type(number) != int:
            raise TypeError("Must be an integer value!")                    #HW
        if number < 0:
            raise ValueError(f"Incorrect wagon number: {number}")           #HW
        else:
            self.number = number

    def __str__(self):
        return f"[{self.number:^4}]"

    def __repr__(self):
        return self.__str__()


class Train:
    def __init__(self):
        self.wagons = []

    def addWagon(self, wagon):                                  
        wagon_numbers = [w.number for w in self.wagons]            #HW                  
        if wagon.number in wagon_numbers:
            print(f"Cannot add wagon with duplicate number: {wagon.number}")
        else:
            self.wagons.append(wagon)

    def removeWagon(self, number): #HW
        for wagon in self.wagons:
            if wagon.number == number:
                self.wagons.remove(wagon)
                return
        print(f"Wagon {number} not found in the train!")

    def __str__(self): #HW
        wagon_str = "=".join(str(w) for w in self.wagons)
        return f"<Train> {wagon_str}"


train = Train()
train.addWagon(Wagon(10))
train.addWagon(Wagon(20))
train.addWagon(Wagon(32))
train.removeWagon(32)
print(train)
