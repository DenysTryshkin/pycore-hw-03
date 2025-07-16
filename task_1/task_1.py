from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError ("Incorrect date format. Expected 'YYYY-MM-DD'")
    
    date_today = datetime.today().date()
    days_delta = (date_today - date_object).days

    return days_delta

print(get_days_from_today("2020-10-09"))
