time = input("What time is it? ").strip()

hours, minutes = time.split(":")
hours =float(hours)
minutes = float(minutes)
minutes = round(minutes/ 60.0,2)
time =hours+minutes

print(time)
