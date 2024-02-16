# Write your helper functions

def apps_and_times(data):
    total_spent = {}
    for app in data:
        app_name = app
        time_spent = 0
        for url in data[app]:
            each_url_time = data[app][url]['time_spent']
            time_spent += each_url_time
        total_spent[app_name] = round(float("{:.2f}".format(round(time_spent))))/60
    total_spent = dict(list(sorted(total_spent.items(), key = lambda x: x[1], reverse = True))[:10])
    return list(total_spent.keys()), list(total_spent.values())

def apps_and_duration(data):
    total_spent = {}
    for app in data:
        app_name = app
        time_spent = 0
        for url in data[app]:
            each_url_time = data[app][url]['time_spent']
            time_spent += each_url_time
        total_spent[app_name] = round(float("{:.2f}".format(round(time_spent))))/60
    total_spent = dict(list(sorted(total_spent.items(), key = lambda x: x[1], reverse = True))[:5])
    finaldata = []
    for data in total_spent.items():
        temp = {'appname' : data[0], 'duration' : data[1]}
        finaldata.append(temp)
    return finaldata, list(total_spent.keys()), list(total_spent.values())


def days_and_times(datas):
    days_time = {}
    for data in datas:
        total_time = 0
        time_usage = data['usage_json']
        for app in time_usage:
            if app not in ("Others", "Unknown"):
                for url in time_usage[app]:
                    each_url_time = time_usage[app][url]['time_spent']
                    total_time += each_url_time
        days_time[data['date'].strftime('%A')] = round(float("{:.2f}".format(round(total_time))))/60
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_days = list(days_time.keys())
    final_json = []
    for day in weekdays:
        if day not in current_days:
            final_json.append(0)
        else:
            final_json.append(days_time[day])
    return final_json
