from crontab import CronTab
import os

current_directory = os.path.dirname(os.path.realpath(__file__))

cron = CronTab(user=True)
job = cron.new(
    command=f"DISPLAY=:0 python3 {current_directory}/check_site.py"
)
job.day.every(3)

cron.write()
