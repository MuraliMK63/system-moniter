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
    return list(total_spent.keys()), list(total_spent.values())
