from datetime import datetime

print("=" * 52)
name = str(input("Enter Your Name: "))
income = float(input("Enter Income: €"))
txCredit = float(input("Enter Tax Of credits: €"))
txDeducted = float(input("Enter Tax Deducted: €"))
usc = float(input("Enter USC: €"))
print("=" * 52)
date = datetime.now()

# Rate Band
rateBand05 = float(0.005)
rateBand2 = float(0.02)
rateBand4 = float(0.04)
rateBand45 = float(0.045)
rateBand475 = float(0.0475)

#
incomeUsc1 = float(12012)
incomeUsc2 = float(10908)
incomeUsc3 = float(3977.01)

adjustments = txCredit + txDeducted
txDue = income * 0.2 if income < 35300 else income * 0.4
payeResulted = (txCredit + txDeducted) - txDue
totalResulted = (incomeUsc1 * rateBand05) + (incomeUsc2 * rateBand2) + (incomeUsc3 * rateBand45)
uscResulted = totalResulted - usc
gross = incomeUsc1 + incomeUsc2 + incomeUsc3
totalOfResult = payeResulted - uscResulted

if income > 35300:
    print(name.title(), " you were taxed on 40% of your salary")
else:
    print(name.title(), "you were taxed on 20% of your salary ")
print("=" * 52)
print("PAYE Calculation:")
print("Adjustments: €" + "{:.2f}".format(adjustments))
print("Tax Due: €" + "{:.2f}".format(txDue))
print("PAYE Result: €" + "{:.2f}".format(payeResulted))

print("=" * 52)
print("Income Chargeable to USC: ")
print("SELF")
print("{:.2f}".format(incomeUsc1), " @ 0.5% =....." + "{:.2f}".format(incomeUsc1 * rateBand05))
print("{:.2f}".format(incomeUsc2), " @ 2% =....." + "{:.2f}".format(incomeUsc2 * rateBand2))
print("{:.2f}".format(incomeUsc3), " @ 4.5% =....." + "{:.2f}".format(incomeUsc3 * rateBand45))
print("USC Deducted: €" + "{:.2f}".format(usc))
print("Total USC Result: €" + "{:.2f}".format(uscResulted))

print("=" * 52)
if totalOfResult > 1:
    print("FINAL RESULT: \033[1;32mOverpayment €" + "{:.2f}\033[m".format(totalOfResult))

elif totalOfResult < -1:
    print("FINAL RESULT: \033[1;31mUnderpayment €" + "{:.2f}\033[m".format(totalOfResult))
else:
    print("FINAL RESULT: €" + "{:.2f}".format(totalOfResult))

print("=" * 52)
print(date.strftime("%d-%b-%Y  %H:%M"))
