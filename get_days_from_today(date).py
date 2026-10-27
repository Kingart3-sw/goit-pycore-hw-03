from datetime import datetime
def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
         print("Invalid date format. Please use 'YYYY-MM-DD'.")
         return None
    current_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = current_date - target_date
    return delta.days
print("Past date (2026-10-20):", get_days_from_today('2026-10-20'))
print("Future date (2026-10-22):", get_days_from_today('2026-10-22'))
print("Future date (2026-10-25):", get_days_from_today('2026-10-25'))
print("Invalid date format (09-10-2020):", get_days_from_today('09-10-2020'))
print("Invalid raw (text):", get_days_from_today('invalid date'))