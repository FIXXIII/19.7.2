def is_leap_year(x):
    return (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2024))  # True
print(is_leap_year(2022))  # False