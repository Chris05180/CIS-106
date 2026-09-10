# Christopher Hernandez M3P1 9/9/26


stock_symbol = input("")
# Input stock symbol

number_shares = int(input(""))
# Input amount of shares

cost_per_share = float(input(""))
# Input cost per share

amount_invested = number_shares * cost_per_share
# Multiply number of shares per cost

print(f"You have invested ${amount_invested:.2f} in {stock_symbol}")
# Displays the total amount invested