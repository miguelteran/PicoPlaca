import unittest
from tests.test_utils import *
from src.pico_placa import *


SKIP_RESTRICTION_DAYS_TEST_MSSAGE = 'There are no days with restrictions'
SKIP_NO_RESTRICTION_DAYS_TEST_MSSAGE = 'There are no days without restrictions'


class TestPicoPlaca(unittest.TestCase):

    def test_license_plate_on_day_with_no_restrictions(self):
        
        if len(get_days_without_driving_restrictions()) == 0:
            self.skipTest(SKIP_NO_RESTRICTION_DAYS_TEST_MSSAGE)

        self.assertTrue(can_user_drive(
            get_random_license_plate(),
            get_random_date_without_driving_restrictions(),
            get_random_time()))

        self.assertTrue(can_user_drive(
            get_random_license_plate(),
            get_random_date_without_driving_restrictions(),
            get_random_time_from_range(START_TIME_FIRST_SHIFT, END_TIME_FIRST_SHIFT)))

        self.assertTrue(can_user_drive(
            get_random_license_plate(),
            get_random_date_without_driving_restrictions(),
            get_random_time_from_range(START_TIME_SECOND_SHIFT, END_TIME_SECOND_SHIFT)))


    def test_license_plate_that_cannot_drive(self):

        if len(get_days_with_driving_restrictions()) == 0:
            self.skipTest(SKIP_RESTRICTION_DAYS_TEST_MSSAGE)
        
        first_date = get_random_date_with_driving_restrictions()
        self.assertFalse(can_user_drive(
            generate_license_plate_that_cannot_drive(first_date),
            first_date, 
            get_random_time_from_range(START_TIME_FIRST_SHIFT, END_TIME_FIRST_SHIFT)))
        
        second_date = get_random_date_with_driving_restrictions()
        self.assertFalse(can_user_drive(
            generate_license_plate_that_cannot_drive(second_date),
            second_date, 
            get_random_time_from_range(START_TIME_SECOND_SHIFT, END_TIME_SECOND_SHIFT)))

    
    def test_license_plate_that_can_drive(self):

        if len(get_days_with_driving_restrictions()) == 0:
            self.skipTest(SKIP_RESTRICTION_DAYS_TEST_MSSAGE)
        
        first_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_can_drive(first_date),
            first_date, 
            get_random_time_from_range(START_TIME_FIRST_SHIFT, END_TIME_FIRST_SHIFT)))
        
        second_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_can_drive(second_date),
            second_date, 
            get_random_time_from_range(START_TIME_SECOND_SHIFT, END_TIME_SECOND_SHIFT)))
        
        third_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_can_drive(third_date),
            third_date, 
            get_random_time()))

    
    def test_license_plate_that_cannot_drive_but_is_not_in_restricted_time(self):

        if len(get_days_with_driving_restrictions()) == 0:
            self.skipTest(SKIP_RESTRICTION_DAYS_TEST_MSSAGE)
        
        first_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_cannot_drive(first_date),
            first_date, 
            get_random_time_from_range(DAY_START_TIME, START_TIME_FIRST_SHIFT)))
        
        second_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_cannot_drive(second_date),
            second_date, 
            get_random_time_from_range(END_TIME_FIRST_SHIFT, START_TIME_SECOND_SHIFT)))
        
        third_date = get_random_date_with_driving_restrictions()
        self.assertTrue(can_user_drive(
            generate_license_plate_that_cannot_drive(third_date),
            third_date, 
            get_random_time_from_range(END_TIME_SECOND_SHIFT, DAY_END_TIME)))


if __name__ == '__main__':
    unittest.main()