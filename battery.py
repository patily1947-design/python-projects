import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print("Battery Percentage:", battery.percent, "%")

    print("Power plugged in:", battery.power_plugged)

    def convertTime(seconds):
         minutes, seconds = divmod(seconds, 60)
         hours, minutes = divmod(minutes, 60)
         return f"{hours}:{minutes:02d}:{seconds:02d}"

    print("Battery remaining time:", convertTime(battery.secsleft))
else:
    print("No battery information available.")