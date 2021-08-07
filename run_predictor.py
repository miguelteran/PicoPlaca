import sys
from src.pico_placa import can_user_drive


def print_usage():
    print('Usage: python {0} <license_plate> <date> <time>'.format(__file__))
    print('Example: python {0} ABC-123 2021-12-31 17:45:00'.format(__file__))


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 4:
        print_usage()
        exit(0)

    license_plate_arg = args[1]
    date_arg = args[2]
    time_arg = args[3]

    try:
        can_user_drive(license_plate_arg, date_arg, time_arg)
    except Exception as e:
        print(e)