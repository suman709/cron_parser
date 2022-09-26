import croniter
import datetime
import sys

if __name__ == '__main__':
    try:
        arguments = sys.argv[1:]
        cron_str = arguments[0]

        now = datetime.datetime.now()

        cron = croniter.croniter(cron_str, now)
        schedule = cron.get_next(datetime.datetime)
        datem = datetime.datetime.strptime(str(schedule), "%Y-%m-%d %H:%M:%S")
        print("Next Cron will trigger on following day:")
        print("***********************************************************************************************")
        print("Minute of cron:", datem.minute)
        print("Hour of cron:", datem.hour)
        print("Day of cron:", datem.day)
        print("Month of cron:", datem.month)
        print("Day of Week of cron:", schedule.weekday())
        print("Command:", arguments[1])

    except Exception as e:
        print("ERROR:", str(e))




