# In this file, I try to write the birthday app without defining as many functions as in the author's example
# and then passing the information from one variable to the next within the main function. Instead, here I wanted
# to use only two functions, and use the second function to do the calculation part, while the get_user_bday function
# got the birthday and printed the result. This way I only had to call one function in the main function, and the
# information is just passed between get_user_bday and calc_diff without involving main and writing all those
# additional functions. And it worked :)

import datetime


def main():
    print_header()
    get_user_bday()


def print_header():
    print("-----------------------------------")
    print("          Birthday app")
    print("-----------------------------------")


def get_user_bday():
    print("When is your birthday?")
    year = int(input("Enter year [YYYY]: "))
    month = int(input("Enter month [MM]: "))
    day = int(input("Enter day [DD]: "))

    bdate = datetime.date(year, month, day)

    diff = calc_diff(bdate)

    if diff < 0:
        print("Your birthday was {} days ago.".format(-diff))
    elif diff > 0:
        print("Your birthday is in {} days!".format(diff))
    else:
        print("Happy birthday! Your birthday is today!")


def calc_diff(data):
    today = datetime.date.today()

    bday_this_year = datetime.date(today.year, data.month, data.day)

    delta = bday_this_year - today

    return delta.days


main()