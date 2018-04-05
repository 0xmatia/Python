from datetime import datetime


def duration(time):
    """
    Checks the duration between two different times
    :param time: The time given in format: HH:MM-HH:MM
    :type time: str
    :return:The duration between two times
    :rtype: str
    """
    first_time = time[:5]
    second_time = time[6:]
    first_time = datetime.strptime(first_time, "%H:%M")
    first_time = first_time.strftime("%I:%M")

    second_time = datetime.strptime(second_time, "%H:%M")
    second_time = second_time.strftime("%I:%M")
    # separate hours and minutes
    f_hours = int(first_time[0:2])
    f_minutes = int(first_time[3:])
    s_hours = int(second_time[0:2])
    s_minutes = int(second_time[3:])
    # hours:
    if not f_minutes == s_minutes:
        hours = abs(f_hours - s_hours) - 1
        if f_minutes > s_minutes:
            minutes = f_minutes - s_minutes + 10
        else:
            minutes = s_minutes - f_minutes + 10
    else:
        hours = abs(f_hours - s_hours)
        minutes = 00
    print("Total duration: " + str(hours) + " hours and " + str(minutes) + " minutes")


duration("16:30-20:40")
