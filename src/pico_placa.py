from time import strptime
from datetime import datetime, date
from src.pico_placa_day import PicoPlacaDay

# Format to parse the time string
TIME_FORMAT = '%H:%M:%S'

# Days of the week as per datetime library
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

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

START_FIRST_SHIFT = strptime('7:00:00', TIME_FORMAT)
END_FIRST_SHIFT = strptime('9:30:00', TIME_FORMAT)
START_SECOND_SHIFT = strptime('16:00:00', TIME_FORMAT)
END_SECOND_SHIFT = strptime('19:30:00', TIME_FORMAT)


def can_user_drive(license_plate_arg, date_arg, time_arg):
    user_can_drive = predict(license_plate_arg, date_arg, time_arg)
    print_result(user_can_drive)
    return user_can_drive


def predict(license_plate_arg, date_arg, time_arg):

    print('License plate: ' + license_plate_arg)
    print('Date: ' + date_arg)
    print('Time: ' + time_arg)

    # Parse date and get day of the week as an integer
    day_number = date.fromisoformat(date_arg).weekday()

    # Find day that matches the day_number
    day = list(filter(lambda day: day.day_number == day_number, DAY_OBJECTS))[0]
    digits = day.license_plate_digits
    day.print_details()
    
    if len(digits) == 0: # A day with no restrictions
        return True
    
    if int(license_plate_arg[-1]) not in digits:
        return True
    else:
        time = strptime(time_arg, TIME_FORMAT)
        if (time >= START_FIRST_SHIFT and time < END_FIRST_SHIFT) or \
            (time >= START_SECOND_SHIFT and time < END_SECOND_SHIFT):
            return False
        else:
            return True


def print_result(can_drive):
    verb = 'can' if can_drive else 'cannot'
    print('========================')
    print('     You {0} drive'.format(verb))
    print('========================')