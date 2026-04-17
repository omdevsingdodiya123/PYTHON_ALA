print("Toll Plaza")

vehicle = input("Enter vehicle type: ")

fee = 100

if vehicle == "Car":
    amount = fee

elif vehicle == "Truck":
    amount = fee * 2

else:
    amount = fee * 3

print("Amount:", amount)

for i in range(3):
    print("Paid")

print("Exit")