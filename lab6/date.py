# 1
import datetime
date_today = datetime.date.today()
new_date = date_today - datetime.timedelta(days=5)
print(new_date)
# 2
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(f"Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")
# 3
current_datetime = datetime.datetime.now()
current_datetime = current_datetime.replace(microsecond=0)
print(current_datetime)
# 4
date1 = datetime.datetime(2023, 10, 19)
date2 = datetime.datetime(2023, 10, 20)
difference = date2 - date1
print(difference.total_seconds())