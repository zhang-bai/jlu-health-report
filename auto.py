import schedule, random, time
from users import *
from main import check
import datetime as dt
from scheduler import Scheduler
import scheduler.trigger as trigger
minute = random.randint(1, 10)

def check_all():
    for user in users:
        check(user['username'], user['password'])


# Instead of setting the timezones yourself you can use the `pytz` library
tz_shanghai = dt.timezone(dt.timedelta(hours=8))
# can be any valid timezone
schedule = Scheduler(tzinfo=dt.timezone.utc)
# schedule jobs
schedule.daily(dt.time(hour=8, minute=minute, tzinfo=tz_shanghai), check_all)
schedule.daily(dt.time(hour=21, , minute=minute, tzinfo=tz_shanghai), check_all)



if __name__ == "__main__":
    while True:
        schedule.exec_jobs()
        time.sleep(30)
