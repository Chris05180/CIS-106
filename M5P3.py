# Christopher Hernandez  M5P3.py  9/22/26

# Input: Enters amount of books purchased
number_books = int(input("Enter number of books: "))

# Input: Enters the price of the book
price_book = float(input("Enter price of books: "))

# Process: Multiplies the number of purchased books by their price
order_total = number_books * price_book

# Assign free shipping if the order total is above $50
if order_total > 50:
    book_shipping = "$0 shipping"
# Assigns $25 shipping the order total is $50 or below
else:
    book_shipping = "$25 shipping"

# Output: Displays the total and shipping cost
print(f"Your total is ${order_total:.2f} with {book_shipping}")