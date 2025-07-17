from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    greetings = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year = today.year + 1)

        days_until_birthdays = (birthday_this_year - today).days

        if 0 <= days_until_birthdays <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)

            greetings.append({"name": user["name"],
                            "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return greetings

users = [
    {"name": "John Doe", "birthday": "1985.07.19"},
    {"name": "Jane Smith", "birthday": "1990.07.22"}
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)