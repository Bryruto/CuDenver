import datetime
def set_alarm():
    alarms = {"Year":0,"Month":0,"Day":0,"Hours":0,"Minutes":0} 

    alarm_calendar_day = input("(YYYY/MM/DD)").strip()
    year,month,day = alarm_calendar_day.split("/")
    alarms["Year"],alarms["Month"],alarms["Day"] = int(year),int(month),int(day)
    
    alarm_time_of_day = input("(HH:MM)").strip()
    hours,minutes = alarm_time_of_day.split(":")
    alarms["Hours"],alarms["Minutes"] = int(hours),int(minutes)

    alarm_set = datetime.datetime(year=alarms["Year"],month=alarms["Month"],day=alarms["Day"],hour=alarms["Hours"],minute=alarms["Minutes"])

    return alarm_set



