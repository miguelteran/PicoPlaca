import time
import string
import random
from datetime import datetime, timedelta
from src.pico_placa import DATE_FORMAT, TIME_FORMAT, DIGITS_PER_DAY


DAY_START_TIME = time.strptime('00:00:00', TIME_FORMAT)
DAY_END_TIME = time.strptime('23:59:59', TIME_FORMAT)


def get_random_time():
    return get_random_time_from_range(DAY_START_TIME, DAY_END_TIME)


def get_random_time_from_range(start_time, end_time):
    start = time.mktime(start_time)
    end = time.mktime(end_time)
    random_time = start + random.randrange(end - start)
    return time.strftime(TIME_FORMAT, time.localtime(random_time))


def get_random_date_with_driving_restrictions():
    return get_random_date(True)


def get_random_date_without_driving_restrictions():
    return get_random_date(False)


"""
Returns an empty string if it cannot satisfy the "with_restrictions" parameter
"""
def get_random_date(with_restrictions=True):
    days_with_restrictions = get_days_with_driving_restrictions()
    days_without_restrictions = get_days_without_driving_restrictions()
    if (with_restrictions and len(days_with_restrictions) == 0) or \
        (not with_restrictions and len(days_without_restrictions) == 0):
        return ''
    else:
        return get_random_date_recursive(with_restrictions)


"""
Returns a randomly generated date. 
Recurses until it produces a date that satisfies the "with_restrictions" parameter. 
"""
def get_random_date_recursive(with_restrictions):
    random_date = generate_random_date()
    if (with_restrictions and random_date.weekday() in get_days_with_driving_restrictions()) or \
        (not with_restrictions and random_date.weekday() in get_days_without_driving_restrictions()):
        return random_date.strftime(DATE_FORMAT)
    else:
        return get_random_date(with_restrictions)


def generate_random_date():
    start = datetime.strptime('1970-01-01', DATE_FORMAT)
    end = datetime.strptime('2050-12-31', DATE_FORMAT)
    delta = end - start
    return start + timedelta(random.randrange(delta.days))


def get_days_with_driving_restrictions():
    return list(filter(lambda i: len(DIGITS_PER_DAY[i]) > 0, DIGITS_PER_DAY.keys()))


def get_days_without_driving_restrictions():
    return list(filter(lambda i: len(DIGITS_PER_DAY[i]) == 0, DIGITS_PER_DAY.keys()))


def generate_license_plate_that_cannot_drive(date_string):
    not_allowed_digits = DIGITS_PER_DAY[datetime.strptime(date_string, DATE_FORMAT).weekday()]
    last_digit = random.choice(not_allowed_digits) if len(not_allowed_digits) > 0 else random.choice(string.digits)
    return generate_random_license_plate(last_digit)


def generate_license_plate_that_can_drive(date_string):
    not_allowed_digits = DIGITS_PER_DAY[datetime.strptime(date_string, DATE_FORMAT).weekday()]
    digits = list(filter(lambda x: x not in not_allowed_digits, range(10)))
    return generate_random_license_plate(random.choice(digits)) 


def get_random_license_plate():
    return generate_random_license_plate(random.choice(string.digits))


def generate_random_license_plate(last_digit):
    license_plate = ''.join(random.choice(string.ascii_uppercase) for x in range(3))  
    license_plate += '-'
    license_plate += ''.join(random.choice(string.digits) for x in range(2))
    license_plate += str(last_digit)
    return license_plate
