from datetime import datetime, timedelta

def get_birthdays_per_week(users, greetins_days=7):

    """
    This function prints the days of week and names of people who will celebrate the bithday
    next 7 days (can be changed when call the function as the second arg = greetins_days)
    If the birthday will be on Saturday or Sunday, the names will be shown for greeting on Monday
    

    """

    mon_list = []
    tue_list = []
    wed_list = []
    thu_list = []
    fri_list = []

    mon_dict = {"Monday": mon_list}
    tue_dict = {"Tuesday": tue_list}
    wed_dict = {"Wednesday": wed_list}
    thu_dict = {"Thursday": thu_list}
    fri_list = {"Friday": fri_list}
    final_dict = {}

    dates_for_greeting = []
    weekdays_list = [mon_dict, tue_dict, wed_dict, thu_dict, fri_list]


    current_day = datetime.now()

    for i in range(greetins_days):
        date_for_greting = current_day + timedelta(days=i)
        dates_for_greeting.append(date_for_greting)

    if current_day.weekday() == 0:
        
        dates_for_greeting.append(current_day - timedelta(days=1))
        dates_for_greeting.append(current_day - timedelta(days=2))
        dates_for_greeting.remove(current_day + timedelta(days=5))
        dates_for_greeting.remove(current_day + timedelta(days=6))

    if current_day.weekday() == 6:
        
        dates_for_greeting.append(current_day - timedelta(days=1))
        dates_for_greeting.remove(current_day + timedelta(days=6))


    for user in users:

        for key, value in user.items():

            for elem in dates_for_greeting:

                if elem.month == value.month and elem.day == value.day:

                    if elem.weekday() in [0, 5, 6]:

                        mon_list.append(key)

                    elif elem.weekday() == 1:

                        tue_list.append(key)

                    elif elem.weekday() == 2:

                        wed_list.append(key)
                        
                    elif elem.weekday() == 3:

                        thu_list.append(key)
                        
                    elif elem.weekday() == 4:

                        fri_list.append(key)

    for day in weekdays_list:

        for key, val in day.items():

            if val:

                final_dict.update(day)

    return print(final_dict)

if __name__ == '__main__':
    
    get_birthdays_per_week([{"Bob": datetime(year=1990, month=1, day=6)}, {"Alisa": datetime(year=1986, month=12, day=8)}, {"Maria": datetime(year=1999, month=12, day=3)}])
    get_birthdays_per_week([{"Bob": datetime(year=2022, month=12, day=4)}, {"Alisa": datetime(year=2022, month=12, day=8)}, {"Maria": datetime(year=2022, month=12, day=10)}])


                


            

            
