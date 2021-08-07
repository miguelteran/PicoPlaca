from os import pardir
from time import strptime
from datetime import datetime, date
import re
from src.pico_placa_day import PicoPlacaDay


# Format to parse the time string
TIME_FORMAT = '%H:%M:%S'

# License plate format
LICENSE_PLATE_REGEX = '\\b[A-Z]{3}-[0-9]{3}\\b'

# Days of the week as per datetime library
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# Default "Pico y Placa" rules for each day
DIGITS_PER_DAY = {
    MONDAY: [0,1],
    TUESDAY: [2,3],
    WEDNESDAY: [4,5],
    THURSDAY: [6,7],
    FRIDAY: [8,9],
    SATURDAY: [],
    SUNDAY: []
}

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAY_OBJECTS = [PicoPlacaDay(DAYS[i], i, DIGITS_PER_DAY[i]) for i in range(len(DAYS))]

# Default "Pico y Placa" times
START_FIRST_SHIFT = '7:00:00'
END_FIRST_SHIFT = '9:30:00'
START_SECOND_SHIFT = '16:00:00'
END_SECOND_SHIFT = '19:30:00'

# Time objects
START_TIME_FIRST_SHIFT = strptime(START_FIRST_SHIFT, TIME_FORMAT)
END_TIME_FIRST_SHIFT = strptime(END_FIRST_SHIFT, TIME_FORMAT)
START_TIME_SECOND_SHIFT = strptime(START_SECOND_SHIFT, TIME_FORMAT)
END_TIME_SECOND_SHIFT = strptime(END_SECOND_SHIFT, TIME_FORMAT)


"""
Wrapper function that predicts if user can drive and prints the result
"""
def can_user_drive(license_plate_arg, date_arg, time_arg):
    user_can_drive = predict(license_plate_arg, date_arg, time_arg)
    print_result(user_can_drive)
    return user_can_drive


"""
Returns whether user can drive given a license plate, date, and time
All arguments are strings
"""
def predict(license_plate_arg, date_arg, time_arg):

    parsed_date, parsed_time, license_plate_last_digit = validate_arguments(license_plate_arg, date_arg, time_arg)

    print('License plate: ' + license_plate_arg)
    print('Date: ' + date_arg)
    print('Time: ' + time_arg)

    # Parse date and get day of the week as an integer
    day_number = parsed_date.weekday()

    # Find day that matches the day_number
    day = list(filter(lambda day: day.day_number == day_number, DAY_OBJECTS))[0]
    digits = day.license_plate_digits
    day.print_details()

    print('Restriction times: {0}-{1}, {2}-{3}'.format(START_FIRST_SHIFT, END_FIRST_SHIFT, 
                                                        START_SECOND_SHIFT, END_SECOND_SHIFT))
    
    if len(digits) == 0: # A day with no restrictions
        return True
    
    if int(license_plate_last_digit) not in digits:
        return True
    else:
        if (parsed_time >= START_TIME_FIRST_SHIFT and parsed_time < END_TIME_FIRST_SHIFT) or \
            (parsed_time >= START_TIME_SECOND_SHIFT and parsed_time < END_TIME_SECOND_SHIFT):
            return False
        else:
            return True


"""
Validates user input and throw exceptions if they are invalid
"""
def validate_arguments(license_plate_arg, date_arg, time_arg):
    
    try:
        parsed_date = date.fromisoformat(date_arg)
    except Exception:
        raise Exception('Date format must be YYYY-MM-DD')

    try:
        parsed_time = strptime(time_arg, TIME_FORMAT)
    except Exception:
        raise Exception('Time format must be hh:mm:ss')

    if re.search(LICENSE_PLATE_REGEX, license_plate_arg) is None:
        raise Exception('License plate format must ABC-123')

    return parsed_date, parsed_time, license_plate_arg[-1]


def print_result(can_drive):
    verb = 'can' if can_drive else 'cannot'
    print('========================')
    print('     You {0} drive'.format(verb))
    print('========================')