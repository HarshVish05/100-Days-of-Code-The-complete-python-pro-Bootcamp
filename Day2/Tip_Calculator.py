print("Welcome to the tip calculator!")
totalBill = int(input("How much was the total bill? ₹"))
tipPercent = int(input("How much tip would you like to give? 10, 12, or 15? "))
noOfPeople = int(input("How many people to split the bill?"))

totalBillAfterTip = totalBill + ((tipPercent*totalBill)/100)
perPersonAmount = round(totalBillAfterTip/noOfPeople, 2)
print(f"Each person should pay: ₹{perPersonAmount}")