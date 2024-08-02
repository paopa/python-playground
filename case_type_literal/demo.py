from typing import Literal, get_args

TRACE_TYPES = Literal["execution", "shallow", "summary"]


def check_value(value: TRACE_TYPES):
    if value in get_args(TRACE_TYPES):
        print("Value is valid")
    else:
        print("Value is invalid")


check_value("execution")
check_value("shallow")
check_value("summary")
check_value("invalid")
