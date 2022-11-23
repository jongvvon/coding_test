hour, minute = map(int, input().split())
time = int(input())

next_min = minute + time

if next_min > 59:
    hour += next_min // 60
    minute = next_min % 60
    if hour > 23:
        hour -= 24
else:
    minute = next_min

print("{} {}".format(hour, minute))
