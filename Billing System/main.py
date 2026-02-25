import datetime

print("===== WELCOME TO PYTHON BILLING SYSTEM =====")

items = []
total = 0

while True:
    name = input("\nEnter product name (or 'q' to quit): ")
    
    if name.lower() == 'q':
        break

    try:
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
    except:
        print("Invalid input! Try again.")
        continue

    cost = price * quantity
    total += cost

    items.append((name, price, quantity, cost))

    print(f"{name} added successfully!")


discount = 0
if total > 1000:
    discount = total * 0.10  

final_total = total - discount


print("\n========== FINAL BILL ==========")
print("Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("--------------------------------")

for item in items:
    print(f"{item[0]}  |  {item[1]} x {item[2]} = {item[3]}")

print("--------------------------------")
print(f"Subtotal: ₹{total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Total Payable: ₹{final_total:.2f}")
print("================================")

with open("bill.txt", "w") as file:
    file.write("===== BILL RECEIPT =====\n")
    file.write("Date: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")
    
    for item in items:
        file.write(f"{item[0]}  |  {item[1]} x {item[2]} = {item[3]}\n")
    
    file.write("\n")
    file.write(f"Subtotal: ₹{total:.2f}\n")
    file.write(f"Discount: ₹{discount:.2f}\n")
    file.write(f"Total Payable: ₹{final_total:.2f}\n")

print("\nBill saved as bill.txt successfully!")