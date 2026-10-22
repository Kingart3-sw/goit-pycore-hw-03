from datetime import datetime
def days_from_today(date: str) -> int:
    target_date = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = current_date - target_date
    return delta.days
print(days_from_today('2026-10-20'))
print(days_from_today('2026-10-22'))
print(days_from_today('2026-10-25'))