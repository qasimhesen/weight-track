from datetime import date

# Create two date objects
date1 = date(2024, 10, 17)
date2 = date(2023, 5, 21)

# Compare the dates
if date1 > date2:
    print(f"{date1} is later than {date2}")
elif date1 < date2:
    print(f"{date1} is earlier than {date2}")
else:
    print(f"{date1} is the same as {date2}")