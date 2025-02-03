# print("Electricity bill estimator")
# price_per_kwh = float(input("Enter cents per kWh: ")) / 100
# kwh_per_day = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days: "))
#
# total_kwh = billing_days * kwh_per_day
# total_bill = total_kwh * price_per_kwh
# print(f"Estimated bill: ${total_bill:.2f}")


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

tariff_type = input("Which tariff? 11 or 31: ")
while tariff_type != "11" and tariff_type != "31":
    print("Invalid tariff")
    tariff_type = input("Which tariff? 11 or 31: ")
if tariff_type == "11":
    tariff_type = TARIFF_11
elif tariff_type == "31":
    tariff_type = TARIFF_31

kwh_per_day = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

total_kwh = billing_days * kwh_per_day
total_bill = total_kwh * tariff_type
print(f"Estimated bill: ${total_bill:.2f}")
