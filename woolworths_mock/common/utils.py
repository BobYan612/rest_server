##################################################################################
# This is a practice project from Biao Yan (Bob Yan), and it's free to be
# downloaded for study and test project.
##################################################################################

import re
import os
import datetime
import time
import logging
import pytz

utc=pytz.UTC

DATETIME_FORMATE = "%Y-%m-%d %H:%M:%S"
DATETIME_OUTPUT_FORMATE = "%Y-%m-%d-%H-%M-%S"
LOGGER = logging.getLogger(__name__)


def convert_to_datetime(datetime_str):
    # type: (string) -> datetime
    """
    Convert string to datetime object for often datetime formate
    such as "%Y-%m-%d %H:%M:%S" or ""%Y_%m_%d_%H_%M_%S"
    :param datetime_str (string): The datetime string
    :return (datetime): datetime object
    """
    if not datetime_str:
        return None
    date_match = re.match("(\d+)[-/_](\d+)[-/_](\d+)\s*(\d*)[:-]?(\d*)[:-]?(\d*)", datetime_str)
    year = date_match.groups()[0]
    (month, date, hour, minute, second) = [date_value.strip() if len(date_value.strip()) == 2
                                           else "0" + date_value.strip() for date_value
                                           in date_match.groups()[1:]]
    datetime_str = "{}-{}-{} {}:{}:{}".format(year, month, date, hour, minute, second)
    LOGGER.info("datetime str is :".format(datetime_str))
    datetime_value = datetime.datetime.strptime(datetime_str, DATETIME_FORMATE)
    datetime_value = datetime_value.replace(tzinfo=utc)
    return datetime_value


def convert_datetime_to_string(datetime_obj):
    # type: (datetime) -> string
    """
    Convert a datetime object to a string as the standard format %Y-%m-%d-%H-%M-%S
    :param datetime_obj (datetime): datetime object
    :return (string): the string value of the datetime
    """
    if not datetime_obj:
        return ""
    return datetime_obj.strftime(DATETIME_OUTPUT_FORMATE)


def get_time_delta_to_minute(time_unit):
    # type: (schedular_str) -> int
    """
    Convert the time delta from different time unit to minutes
    It supports week(w), day(d), hour(h), minute(m)
    :param time_unit (string): time unit:week(w), day(d), hour(h), minute(m)
    :return (int): The value of minutes equal to input unit
    """
    time_full_unit = ['week', 'day', 'hour', 'minute']
    time_abbre_unit = ['w', 'd', 'h', 'm']
    delta_diff = [0, 60, 24 * 60, 7 * 24 * 60]
    if time_unit in time_full_unit:
        expect_pos = time_full_unit.index(time_unit)
    elif time_unit in time_abbre_unit:
        expect_pos = time_abbre_unit.index(time_unit)
    else:
        raise RuntimeError("Unexpected unit for {}".format(time_unit))
    minutes_detla = delta_diff[expect_pos]
    return minutes_detla


def convert_to_timedelta(schedular_str):
    #type: (schedular_str) -> int
    """
    Convert a time delta with various timeunit to minutes
    For example: convernt 2 w to 20160 minutes
    :param schedular_str (string): one delta of time
    :return (int): total minutes
    """
    time_value_match = re.match("(\d+)\s*(\w+)", schedular_str)
    if not time_value_match:
        return None
    schedular_number, schedular_time_unit = time_value_match.groups()
    actual_minute_detla = get_time_delta_to_minute(schedular_time_unit)
    total_minutes = actual_minute_detla * int(schedular_number)
    time_detla = datetime.timedelta(minutes=total_minutes)
    return time_detla


def retry(func, retry_count=2, interval=10, if_return=True, **kwargs):
    # type: (function, int, int, bool, object, callable) -> Any
    """
    :param func (function): The function to run
    :param retry_count (int, optional): The number of times to retry the command, default is 10
    :param interval (int, optional): The time in seconds to wait for before two retries, default is 10
    :param if_return (bool, optional): if return is expected from the command, default is True
    :param kwargs (args, optional): any args for func.
    :return: Any return from the function or None if no return
    """
    count = 0
    while count < retry_count:
        try:
            ret = func(**kwargs)
            if if_return and ret is not None:
                return ret
            return
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception as err:  # pylint: disable=broad-except
            if count >= retry_count - 1:
                raise
            else:
                LOGGER.info("error:{}".format(err))

        LOGGER.info("sleep %s seconds and retry", interval)
        time.sleep(interval)
        count += 1

    raise RuntimeError("%s timeout" % func)

