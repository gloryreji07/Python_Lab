def is_leap_year(year):
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year=None):

    days = {
        'January': 31,
        'February': 29 if year and is_leap_year(year) else 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    
    return days.get(month, "Invalid month")

def main():
    
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    
   
    month = input("Enter the month name: ").strip()
    
    if month not in months:
        print("Invalid month entered.")
        return
    
   
    if month == 'February':
        year = int(input("Enter the year: ").strip())
    else:
        year = None
    
    
    days = days_in_month(month, year)
    
    if days == "Invalid month":
        print(days)
    else:
        print(f"{month} {year if year else ''} has {days} days.")


if __name__ == "__main__":
    main()
