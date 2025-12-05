** start of main.py **

def add_time(start, duration, starting_day=None):
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if period.upper() == "PM":
        start_hour += 12
    if start_hour == 24:  # özel durum: 12:00 AM
        start_hour = 0

    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"

    if starting_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        index = days_of_week.index(starting_day.capitalize())
        final_day = days_of_week[(index + days_later) % 7]
        day_part = f", {final_day}"
    else:
        day_part = ""

    if days_later == 1:
        later_part = " (next day)"
    elif days_later > 1:
        later_part = f" ({days_later} days later)"
    else:
        later_part = ""

    return f"{final_hour}:{final_minute:02d} {final_period}{day_part}{later_part}"


** end of main.py **

