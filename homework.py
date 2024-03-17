from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays = defaultdict(list)

    # we find today's date
    today = datetime.today().date()

    # Iterate through each user
    for user in users:
        # get name
        name = user["name"]
        # get birthday
        birthday = user["birthday"].date()

        # Converting by the type date*
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            # If yes, consider the date for the following year
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # We define the difference between the birthday and the current day
        delta_days = (birthday_this_year - today).days

        # Calculate the week day
        birthday_day = (today + timedelta(days=delta_days)).strftime('%A')

        if 0 <= delta_days < 7:
            # if birthday on weekend, move to Monday
            if birthday_day in ['Saturday', 'Sunday']:
                birthday_day = 'Monday'

            birthdays[birthday_day].append(name)

    return birthdays


users=[
           {"name": "Cozma Malina", "birthday": datetime(1997, 3, 11)},
           {"name": "Avram Ionut", "birthday": datetime(1995, 10, 28)},
           {"name": "Dorca Carla", "birthday": datetime(1996, 3, 13)},
           {"name": "Pop Amalia", "birthday": datetime(2003, 3, 18)},
           {"name": "Birle Alexandru", "birthday": datetime(1990, 4, 15)},
           {"name": "Marcus Ioana", "birthday": datetime(1989, 3, 21)}
           ]

birthdays_per_week = get_birthdays_per_week(users)

for day, names in birthdays_per_week.items():
    print(f"{day}: {', '.join(names)}")










