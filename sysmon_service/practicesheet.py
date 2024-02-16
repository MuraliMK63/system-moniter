
# import pygetwindow as gw
# import time

# while True:
#     # def get_active_application():
#         try:
#             active_window = gw.getActiveWindow()
#             if active_window:
#                 # Here I'm removing beginning and trailing spaces inside a app name to avoid app_name redundancy
#                 print(active_window.title.strip()) 
#         except Exception as e:
#             print(f"Error: {e}")
#         print("Unknown")
#         time.sleep(2)
        


# import os 
# print(os.getlogin())


from datetime import datetime, timedelta
today_week_day = datetime.now().date().weekday()
beginning_day = datetime.now().date() - timedelta(days = today_week_day)
print(today_week_day)
print(beginning_day)
print(datetime.now().date() > beginning_day)

