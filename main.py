from product import Product
from electrical import Electrical
from nonelectrical import NonElectrical
from laptop import Laptop
from mobile import Mobile
from speaker import Speaker
from furnitur import Furnitur

lap1 = Laptop()
lap1.price = int(input("Enter laptop Price :"))
lap1.name = input("Enter laptop Name " )

lap1 = Laptop()
lap1.ram = 8
lap1.cpu = 3
print(lap1)

mob1 = Mobile()
mob1.price = int(input("Enter mobile Price :"))
mob1.name = input("Enter mobile name :")

mob1 = Mobile()
mob1.screan_size = 6.1
print(mob1)

spk1 = Speaker()
spk1.power = 12
spk1.price = int(input("Enter speaker Price :"))
spk1.name = input("Enter speaker name :")
print(spk1)

furn1 = Furnitur()
furn1.capacity = 4
furn1.price = int(input("Enter furniture Price :"))
furn1.name = input("Enter furniture Name :")
print(furn1)
