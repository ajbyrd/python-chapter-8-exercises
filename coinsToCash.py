
def calc_dollars():
    
    piggyBank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
    }

    dollarAmount = (piggyBank["pennies"] / 100) + (piggyBank["nickels"] * .05) + (piggyBank["dimes"] * .10)
    
    return dollarAmount

print(calc_dollars())

 