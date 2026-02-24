# write a calss 'train' which has methods to book tickets, get status and get fair information of train running ynder Indian Railways

from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no:{self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(122,555)}")


t = Train(7546)
t.book("Indore", "Pachore")
t.getStatus()
t.getFare("Indore","Pachore")