import re
def normalize_phone(phone_number: str) -> str:
    digits_only = re.sub(r'\D', '', phone_number)
    if digits_only.startswith('380'):
        return '+' + digits_only
    else:
        return '+38' + digits_only
if __name__ == "__main__":
    test_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   "
        "38050+1234567",
        "+380501234567+"
]
print("result normalize_phone:")
for phone in test_numbers:
        result = normalize_phone(phone)
        print(f"Вхідний: {phone.strip():<22} -> Результат: {result}")