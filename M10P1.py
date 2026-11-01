# Christopher Hernandez  M10P1.py  10/26/26

# Input: Asks user if they want to initiate program
begin_program = str(input("Start program? (Yes/No): "))

# Process: Sets next month sales as float value
next_month_sales = float()

# Process: Sets forecast percent as float value
forecast_percent = float()

# Process: Creates a function to determine next month's forecast
def get_next_month_forecast():

# Process: Treats "next_month_sale" as a global
    global next_month_sales

# Process: Treats "forecast_percent" as global
    global forecast_percent

# Process: Sets forecast percent at 10% if "Jan", "Feb", or "Mar" are typed
    if current_month == "Jan" or current_month == "Feb" or current_month == "Mar":
        forecast_percent = .10

# Process: Sets forecast percent at 15% if "Apr", "May", or "Jun" are typed for month
    elif current_month == "Apr" or current_month == "May" or current_month == "Jun":
        forecast_percent = .15

# Process: Sets forecast percent at 20% if "Jul", "Aug", or "Sep" are typed for month
    elif current_month == "Jul" or current_month == "Aug" or current_month == "Sep":
        forecast_percent = .20

# Process: Sets forecast percent at 25% if "Oct", "Nov", or "Dec" are typed for month
    elif current_month == "Oct" or current_month == "Nov" or current_month == "Dec":
        forecast_percent = .25

# Process: Multiplies current sales by the sum of 1 and forecast percent
    next_month_sales = current_sales * (1 + forecast_percent)

# Process: Continues to run program while "Yes" is entered
while begin_program == "Yes":

# Input: Asks user for their last name
    last_name = str(input("Enter last name: "))

# Input: Asks user for the current month
    current_month = str(input("Enter first three letters of month: "))

# Input: Asks user for current sales
    current_sales = float(input("Enter current sales: "))

# Process: Calls the function
    get_next_month_forecast()

# Output: Displays next month's sales
    print(f"Next month sales are projected to be ${next_month_sales:.2f}")

# Input: Asks user if they want to continue program
    begin_program = str(input("Continue? "))
