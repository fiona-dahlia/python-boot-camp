def is_leap(p_year):
    if p_year % 4 == 0:
        if p_year % 100 == 0:
            if p_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(p_year, p_month):
    """
    If you enter a year and a month, it returns the days in that month.

    :param p_year: Input year
    :param p_month: Input month
    :return: Days in the month
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(p_year)
    # print(is_leap_year)
    if is_leap_year and p_month == 2:
        return 29
    return month_days[p_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
