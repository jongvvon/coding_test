a, b = map(int, input().split())

alarmTime = ((a * 60) + b) - 45

hourTime, minTime = divmod(alarmTime, 60)

if(hourTime < 0) :
    hourTime = 24 + hourTime
    
print(hourTime, minTime)