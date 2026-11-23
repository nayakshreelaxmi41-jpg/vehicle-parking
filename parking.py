
name = input("Enter customer name: ")
vehicle = input("Enter vehicle number: ")
vtype = input("Enter vehicle type: ")
date = input("Enter parking date: ")
entry = input("Enter entry time: ")
hours = int(input("Enter parking hours: "))
rate = float(input("Enter charge per hour: "))

total = hours * rate

print("\n--- Vehicle Parking Receipt ---")
print("Customer Name:", name)
print("Vehicle Number:", vehicle)
print("Vehicle Type:", vtype)
print("Parking Date:", date)
print("Entry Time:", entry)
print("Parking Hours:", hours)
print("Charge Per Hour:", rate)
print("Total Parking Fee:", total)

with open("parking.txt", "a") as f:
    f.write(f"{name}, {vehicle}, {vtype}, {date}, {entry}, {hours}, {rate}, {total}\n")

print("Parking details saved successfully!")
