from datetime import datetime

# Функція отримує на вхід дату у форматі рядок 'РРРР-ММ-ДД' (наприклад, '2020-10-09')
def get_days_from_today(date):

    days_difference = None

    try:
        # Перетворення вхідного параметра в об'єкт datetime, і отримання дати без часу
        datetime_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f'Вхідна змінна {date} не має формату "2020-10-09"')
    else:
        # Отримання поточної дати без часу
        today_date = datetime.today().date()

        # Розрахунок кількості днів (в цілих числах) між заданою датою і поточною датою
        days_difference = datetime_date.toordinal() - today_date.toordinal()
    
    return days_difference

str_date = '2024-03-08'
print(f'К-сть днів між поточною датою та датаю "{str_date}": ', get_days_from_today(str_date))