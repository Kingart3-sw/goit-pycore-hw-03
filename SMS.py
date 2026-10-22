import re
def normalize_phone(phone_number: str) -> str:
    cleaned = re.sub(r'[^\d+]', '', phone_number)
    if cleaned.startswith('+380'):
        return cleaned
    elif cleaned.startswith('380'):
        return '+' + cleaned
    else:
        if cleaned.startswith('+'):
            cleaned = cleaned.replace('+', '')
            return '+38' + cleaned
test_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
]
print("result normalize_phone:")
for phone in test_numbers:
        result = normalize_phone(phone)
        print(f"Вхідний: {phone.strip():<20} -> Результат: {result}")