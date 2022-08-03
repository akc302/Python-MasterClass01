import datetime
import pytz


class Kettle(object):
    power_source = "electricity"
    def __init__(self, makingCost, sellingPrice):
        self.makingCost = makingCost
        self.sellingPrice = sellingPrice
    def show(self):
        print("Name and price= {},{}".format(self.makingCost,self.sellingPrice))
        print(pytz.utc.localize(datetime.datetime.utcnow()))
rice = Kettle("ring",75)
bells = Kettle("onion",100)
print("models: {}={}, {}={}".format(rice.makingCost, rice.sellingPrice, bells.makingCost,bells.sellingPrice))

print(Kettle.__dict__)
Kettle.power_source="Fire!"
print(rice.power_source)
print(bells.power_source)
print(rice.__dict__)
rice.show()
