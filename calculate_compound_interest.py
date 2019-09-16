print('How many years?')
years = int(input("Enter years: "))

print('How much money is currently in your account?')
principal = float(input("Enter amount: "))

print('How much money do you plan on investing monthly?')
monthly_invest = float(input("Enter amount: "))

print('What do you estimate will be the yearly interest?')
interest = float(input("Enter interest as decimals (10% = 0.1): "))

print(' ')

monthly_invest = monthly_invest * 12
final_amount = 0

for i in range(0, years):
    if final_amount == 0:
        final_amount = principal

    final_amount = (final_amount + monthly_invest) * (1 + interest)

print('The result after {} years is: {}'.format(years, str(final_amount)))
