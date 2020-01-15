import math

def make_change():
    dollarAmount = 8.69
    piggy_bank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    piggy_bank["quarters"] = math.floor(dollarAmount / .25)
    dollarAmount = dollarAmount % .25

    piggy_bank["dimes"] = math.floor(dollarAmount / .10)
    dollarAmount = dollarAmount % .10

    piggy_bank["nickels"] = math.floor(dollarAmount / .05)
    dollarAmount = dollarAmount % .05

    piggy_bank["pennies"] = math.ceil(dollarAmount / .01)

    return piggy_bank 

print(make_change())
