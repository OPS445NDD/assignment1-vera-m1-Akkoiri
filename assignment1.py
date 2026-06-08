#!/usr/bin/env python3

"""
Assignment 1 Version A
Name: Ambika Koiri
Seneca ID: akkoiri

This script counts the number of weekend days between two dates.
I declare that this is my own work in accordance with Seneca Academic Policy.
"""

import sys


def leap_year(year: int) -> bool:
    """Return True if year is a leap year, otherwise False."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def mon_max(month: int, year: int) -> int:
    """Return the maximum number of days in a month."""
    if month == 2:
        if leap_year(year):
            return 29
        return 28

    days_in_month = {
        1: 31, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    return days_in_month[month]


def after(date: str) -> str:
    """
    Return the next day's date in YYYY-MM-DD format.
    """

    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    day = day + 1

    # If the day goes past the month limit, move to next month.
    if day > mon_max(month, year):
        day = 1
        month = month + 1

    # If the month goes past December, move to next year.
    if month > 12:
        month = 1
        year = year + 1

    return f"{year}-{month:02}-{day:02}"


def valid_date(date: str) -> bool:
    """Return True if date is valid YYYY-MM-DD format."""

    parts = date.split('-')

    if len(parts) != 3:
        return False

    year, month, day = parts

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1583:
        return False

    if month < 1 or month > 12:
        return False

    if day < 1 or day > mon_max(month, year):
        return False

    return True


def day_of_week(date: str) -> str:
    """
    Return the day of week for a date.
    Formula works for Gregorian calendar dates.
    """

    year, month, day = date.split('-')
    year = int(year)
    month = int(month)
    day = int(day)

    if month < 3:
        month = month + 12
        year = year - 1

    k = year % 100
    j = year // 100

    day_number = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j)) % 7

    days = {
        0: "Saturday",
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday"
    }

    return days[day_number]


def day_count(start_date: str, end_date: str) -> int:
    """Count Saturdays and Sundays between two dates, including both dates."""

    weekend_count = 0
    current_date = start_date

    while current_date != after(end_date):
        week_day = day_of_week(current_date)

        if week_day == "Saturday" or week_day == "Sunday":
            weekend_count = weekend_count + 1

        current_date = after(current_date)

    return weekend_count


def earlier(date1: str, date2: str) -> bool:
    """Return True if date1 is earlier than or equal to date2."""

    year1, month1, day1 = date1.split('-')
    year2, month2, day2 = date2.split('-')

    date1_number = int(year1 + month1 + day1)
    date2_number = int(year2 + month2 + day2)

    return date1_number <= date2_number


def usage():
    """Print usage message and exit."""

    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit()


if __name__ == "__main__":

    if len(sys.argv) != 3:
        usage()

    date1 = sys.argv[1]
    date2 = sys.argv[2]

    if not valid_date(date1) or not valid_date(date2):
        usage()

    if earlier(date1, date2):
        start_date = date1
        end_date = date2
    else:
        start_date = date2
        end_date = date1

    total_weekends = day_count(start_date, end_date)

    print(f"The period between {start_date} and {end_date} includes {total_weekends} weekend days.")

