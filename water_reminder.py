from plyer import notification
import time

while True:
    notification.notify(
        title = 'WAIT N HYDRATE',
        message = "It's Been an hour, \nTime to drink water",
        app_name = 'WAIT HYDRATE',
        app_icon = r'D:\\PY_COURSE\\CWH\\DrinkWater\\water.ico',
        toast = True,
        timeout = 5,
        )
    time.sleep(60 * 60)
