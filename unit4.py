def gen_secs():
    x = 0
    while x < 60:
        yield x
        x += 1

def gen_minutes():
    x = 0
    while x < 60:
        yield x
        x += 1

def gen_hours():
    x = 0
    while x < 24:
        yield x
        x += 1

def gen_time():
    """
    this generator uses gen_hours, gen_minutes and gen_secs to yield a time in format hh:mm:ss
    """
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield '%02d:%02d:%02d' % (hour, min, sec)

def gen_years(start=2024):
    while True:
        yield start
        start += 1

def gen_months():
    x = 1
    while x < 13:
        yield x
        x += 1

def gen_days(month, leap_year=True):
    x = 1
    while x < 32:
        yield x
        if month == 2 and (x == 29 or (x == 28 and not leap_year)):
            x = 32
        elif month in [2, 4, 6, 9, 11] and x == 30: # months with 30 days
            x = 32
        else:
            x += 1

def is_leap_year(year):
    """
    returns boolean if the year provided is a leap year
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def gen_date():
    """
    this generator uses gen_years, gen_months, gen_days and gen_time to yield a datetime in format dd/MM/yyyy hh:mm:ss
    """
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for time in gen_time():
                    yield "%02d/%02d/%d %s" % (day, month, year, time)

def main():
    date_gen = gen_date()
    while True:
        print(next(date_gen))
        for _ in range(1_000_000):
            next(date_gen)


if __name__ == '__main__':
    main()
