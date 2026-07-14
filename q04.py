# 4. Write a program to calculate an electricity bill based on slab rates

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = units * 4

else:
    bill = units * 6

print("Electricity Bill =", bill)