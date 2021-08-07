"""
A class that models a day of the week and license plates digits that are not allowed to drive on that day
- day_name: string representation of the day (e.g. Monday)
- day_number: integer representation of the day (values range from 0 to 6)
- license_plate_digits: list of 0-9 digits; license plates ending with these cannot drive
"""
class PicoPlacaDay:
    def __init__(self, day_name, day_number, license_plate_digits):
        self.day_name = day_name
        self.day_number = day_number
        self.license_plate_digits = license_plate_digits

    def print_details(self):
        print('Day of the week: ' + self.day_name)
        if len(self.license_plate_digits) > 0:
            print('License plates ending {0} cannot drive'.format(self.license_plate_digits))
        else:
            print('All license plates can drive')