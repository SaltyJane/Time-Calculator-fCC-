def add_time(start: str, duration: str, day=None):
    """
    add_time("11:43 AM", "00:20")
    # Returns: 12:03 PM
    
    add_time("10:10 PM", "3:30")
    # Returns: 1:40 AM (next day)
    
    add_time("11:43 PM", "24:20", "tueSday")
    # Returns: 12:03 AM, Thursday (2 days later)
    """
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days_amt = 0
    new_ampm = ''
    if day is not None:
        new_day = day
    else:
        new_day = None
    # get start values for hr, min, am/pm
    start_split = start.split(' ')
    start_split2 = start_split[0].split(':')
    start_hr = start_split2[0]
    start_min = start_split2[1]
    start_ampm = start_split[1]

    # get duration values for hr, min
    dur_split = duration.split(':')
    dur_hr = dur_split[0]
    dur_min = dur_split[1]

    # add 12 hours if time is PM, to make it 24-hr format
    if start_ampm.lower() == "pm":
        start_hr = int(start_hr) + 12

    # start calculations
    new_hr = int(start_hr) + int(dur_hr)
    new_min = int(start_min) + int(dur_min)
    if new_min >= 60:
        new_hr = int(new_hr) + int(int(new_min) / 60)
        new_min = int(new_min) % 60
    while new_hr > 24:
        new_hr -= 24
        days_amt += 1
        # print(str(new_hr) + "- " + str(days_amt))
    # order matters here
    if new_hr <= 11:
        new_ampm = 'AM'
    if new_hr == 12:
        new_ampm = 'PM'
    if new_hr == 24:
        days_amt += 1
        new_hr = 12
        new_ampm = 'AM'
    # if this block goes before any of the above, the output will be wrong. It needs to happen AFTER the 12 and 24 are set to 0
    if (new_hr > 11) and (new_hr != 12):
        new_hr -= 12
        new_ampm = 'PM'

    if day is not None and (day.strip() != ''):
        weekday = day.strip().lower().title()
        week_index = week_days.index(weekday)
        new_week_index = (week_index + days_amt) % 7
        new_day = week_days[new_week_index]
    
    # if new_hr < 10:
    #     new_hr = '0' + str(new_hr)
    if new_min < 10:
        new_min = '0' + str(new_min)

    # start output
    # if no days have passed
    if days_amt == 0:
        # if day was entered
        if new_day is not None:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm) + ', ' + new_day
        else:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm)
    # if only 1 day has passed
    elif days_amt == 1:
        if new_day is not None:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm) + ', ' + new_day + ' (next day)'
        else:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm) + ' (next day)'
    # if more than 1 day has passed        
    else:
        if new_day is not None:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm) + ', ' + str(new_day) + f' ({days_amt} days later)'
        else:
            new_time = str(new_hr) + ':' + str(new_min) + ' ' + str(new_ampm) + ' ' + f'({days_amt} days later)'
        
    return new_time
