from datetime import datetime, timedelta


date_string = input()

given_date = datetime.strptime(date_string, "%Y %m %d")

today = datetime.now().date()
time_difference = today - given_date

print(f"{given_date} ")
