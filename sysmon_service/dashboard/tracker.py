import pygetwindow as gw

from time import time
from datetime import timedelta, datetime

from .models import TimeUsage


def get_active_application():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            # Here I'm removing beginning and trailing spaces inside a app name to avoid app_name redundancy
            return active_window.title.strip()
    except Exception as e:
        print(f"Error: {e}")
    return "Unknown"


def main_tracker(user):
    while True:
        current_app = get_active_application()
        entry = TimeUsage.objects.filter(useraccount = user, date = datetime.now().date()).first()
        if not entry:
            entry = TimeUsage.objects.create(useraccount = user, date = datetime.now().date(), usage_json = {}, previous_app = None, previous_url = None) 
        current_app_name = current_app.split('-')[-1]
        current_url_name = "/".join(current_app.split("-")[::-1])           
        if entry.previous_app == None:
            # Previous code
            # current_application = current_app
            # app_timestamp[current_application] = time()
            # app_timings[current_application] = 0
            # New code
            temp_json = { current_url_name : {"time_spent" : 0, "in_time" : time()} }
            entry.usage_json[current_app_name] = temp_json
            entry.previous_app = current_app_name
            entry.previous_url = current_url_name
            entry.save()
        else:
            # Previous code
            # if current_app != current_application:
            #     time_duration = time() - app_timestamp[current_application]
            #     app_timings[current_application] += time_duration
            #     current_application = current_app
            #     if current_application not in app_timings:
            #         app_timings[current_application] = 0
            #     app_timestamp[current_application] = time()
            # New code
            if entry.previous_url != current_url_name:
                # Getting previous API's start time
                url_start_time = entry.usage_json[entry.previous_app][entry.previous_url]['in_time']
                time_duration = time() - url_start_time
                # Updating the time spent in previous url
                entry.usage_json[entry.previous_app][entry.previous_url]['time_spent'] += time_duration
                # Checking if current app already in usage_json
                if current_app_name in entry.usage_json:
                    # Checking if current url not in usage_json's current app
                    if current_url_name not in entry.usage_json[current_app_name]:
                        temp_json = {"time_spent" : 0, "in_time" : time()}
                        entry.usage_json[current_app_name][current_url_name] = temp_json
                    # Checking if current url in usage_json's current app, then updates it's timestamp
                    else:
                        entry.usage_json[current_app_name][current_url_name]['in_time'] = time()
                # If current app not in usage json, then create a new app with new url
                else:
                    temp_json = { current_url_name : {"time_spent" : 0, "in_time" : time()} }
                    entry.usage_json[current_app_name] = temp_json
                # Updating previous app and url
                entry.previous_app = current_app_name
                entry.previous_url = current_url_name
                entry.save()
    # else:
    #     time_duration = time() - app_timestamp[current_application]
    #     app_timings[current_application] += time_duration
    