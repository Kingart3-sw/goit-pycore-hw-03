from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    # Отримуємо поточну дату системи
    today = datetime.today().date()
    
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until = (birthday_this_year - today).days
        if 0 <= days_until <= 7:
            congratulation_date = birthday_this_year
            weekday = congratulation_date.weekday()
            if weekday == 5:
                congratulation_date += timedelta(days=2)
            elif weekday == 6:
                congratulation_date += timedelta(days=1)
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays
test_users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.10.24"},
    {"name": "Alice Jones", "birthday": "1992.10.25"},
    {"name": "Bob Brown", "birthday": "2000.12.05"}
]
print("John Doe","Jane Smith","Alice Jones","Bob Brown")
results = get_upcoming_birthdays(test_users)
print(results)         