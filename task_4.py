from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.16"},
    {"name": "Test Test", "birthday": "1984.03.17"},
    {"name": "Jane Smith", "birthday": "1990.03.12"},
    {"name": "P B", "birthday": "1984.01.21"}
        ]


def find_next_weekday(date, weekday):

    day_ahead = weekday - date.weekday()
    if day_ahead <= 0:
        day_ahead += 7

    return date + timedelta(days=day_ahead)


def get_prepared_users(users):

    prepared_users = []

    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            prepared_users.append({"name": user["name"], "birthday": birthday})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    return prepared_users


def get_upcoming_birthdays(users):

    greeting_period = 7 # період контролю привітань на 7 днів
    today = datetime.today().date()
    upcoming_birthdays = [] # список для зберігання користувачів, яких потрібно привітати

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year) # конвертуємо рік народження в поточний рік # 1985 -> 2024
        
        if birthday_this_year < today: # якщо день народження вже минув в цьому році
            birthday_this_year = birthday_this_year.replace(year=today.year + 1) # то розглянути дату на наступний рік
        
        if 0 <= (birthday_this_year - today).days <= greeting_period:
            if birthday_this_year.weekday() >= 5: # якщо випадає на субота, неділя
                birthday_this_year = find_next_weekday(birthday_this_year, 0) # то переносимо привітання на понеділок

            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
        
    return upcoming_birthdays


prepared_users = get_prepared_users(users)
upcoming_birthdays = get_upcoming_birthdays(prepared_users)
print("Список привітань на цьому тижні:", upcoming_birthdays)