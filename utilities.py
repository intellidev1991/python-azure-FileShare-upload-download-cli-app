import sys

# --- Terminal Color
TC_RED = "\033[1;31m"
TC_BLUE = "\033[1;34m"
TC_CYAN = "\033[1;36m"
TC_GREEN = "\033[0;32m"
TC_RESET = "\033[0;0m"
TC_BOLD = "\033[;1m"
TC_REVERSE = "\033[;7m"
# ---


def print_blue(msg):
    sys.stdout.write(TC_BLUE)
    print(msg)
    sys.stdout.write(TC_RESET)


def print_green(msg):
    sys.stdout.write(TC_GREEN)
    print(msg)
    sys.stdout.write(TC_RESET)


def print_red(msg):
    sys.stdout.write(TC_RED)
    print(msg)
    sys.stdout.write(TC_RESET)
