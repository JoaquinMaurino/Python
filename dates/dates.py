from datetime import datetime, time, date, timedelta

time_units = ['year', 'month', 'day', 'hour', 'minute', 'second', 'timestamp']

def print_date(date):
    for i in time_units:
        if i == 'timestamp':
            print(date.timestamp())
        else:
            print(getattr(date,i))

    # print(date.year)
    # print(date.month)
    # print(date.day)
    # print(date.hour)
    # print(date.minute)
    # print(date.second)
    # print(date.timestamp())

now = datetime.now()
#print_date(now)

year_2023 = datetime(2023, 1, 1)
#print_date(year_2023)

#--------------------------------

current_time = time(21,6,0)

# print(current_time.hour)
# print(current_time.minute)
# print(current_time.second)

#--------------------------------

current_date = date.today()

# print(current_date.year)
# print(current_date.month)
# print(current_date.day)

#---------------------------------


#Ambos son iguales:
print(year_2023.date() - current_date)
print(year_2023 - now)

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)