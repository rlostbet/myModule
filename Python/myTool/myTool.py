from functools import wraps

import os

"""
TEMPLET
from functools import wraps
#import functools

def decorator(func):
    @wraps(func)
    #@functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

# decorators
#  - http://www.posemaniacs.com/archives/1551
"""


def clear():
    os.system("cls")


def LineDecor(func):
    """Decorates a function with lines

    example:
    @LineDecor
    def foo:
        print("foo")

    foo()
    >>> ================
    >>> foo
    >>> ================

    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("-" * 30)
        value = func(*args, **kwargs)
        print("-" * 30)
        return value
    return wrapper


def Cap(text):
    """Capitalise The First Letter and Leave the rest.

    examples:
        a = "AsDf AsdF asDf"

        Cap(a)
        >>> AsDf AsdF asDf

        a.capitalize()
        >>> Asdf asdf asdf
    """
    return text[0].upper() + text[1:]


def rLine(times=50, char='-'):
    """ return a line
    examples:
        rLine(6)
        >>> ------
    """
    char = str(char)
    return char * times


def Line(*args):
    """prints a Line

    example:
        Line()
        >>> -----------------
    """
    print(rLine(*args))


def Password(pswd):
    """Set Password

    Set Password For Program to continue

    example:
        Password(1234)

        >>> Enter PassWord
        >>> > 4321
        >>> Wrong:(
        >>> > 1234
        >>> :)

    Arguments:
        pswd {string} -- the password
    """
    pswd = str(pswd)
    match = False
    print("Enter PassWord")
    Line()
    while not match:
        guess = input(">")
        if guess == pswd:
            print(":)")
            match = True
        else:
            print("Wrong :(")
    Line()


def isIntString(x):
    """Is Integer String

    - Is the string consist of Numbers?

    Returns:
    is Integer String: True
    is Not Int String: False
    Not String: None

    Example:
    print(isIntString("1141951"))
    >>> True

    print(isIntString("1209591DD"))
    >>> False

    print(isIntString("")) # empty string
    >>> False

    print(isIntString(124121))
    >>> None   # meaning it does not return anything
    """
    if isinstance(x, str):
        if x == "":
            return False

        for char in x:
            if char not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                return False

        return True


def correctIntStr(a, str_x, b):
    """Validate a string input to an integer in range of a and b.

    the program takse a string variable and check its type and if its value is in range.

    Arguments:
        a {int} -- minimum value x can be
        str_x {int} -- x as a string
        b {[type]} -- maximum value for x

    Returns:
        int_x -- integer x
    """
    error = True

    while error:
        error = False

        if isIntString(str_x):  # is it string of numbers?
            int_x = int(str_x)

            if not(a <= int_x <= b):
                print(f"\n- The value should be in the range of {a} and {b}\n")
                error = True
        else:
            print("\n- Input Numbers\n")
            error = True

        if error:
            print("Input Again")
            str_x = (input(">>>"))

    return int_x


def UseWindowTerminal(cmd):
    """Use Window Cmd"""
    os.system(cmd)


def REPL():
    """Simple Read Evaluate Print Loop"""
    Line()
    print("!! Warning !!")
    Line()
    print("It's a simple REPL (Repeat Evaluate Print Loop)")
    print("well, exec to be exact")
    Line()
    while True:
        userInput = input(">").split()

        if userInput == ["quit"]:
            break

        while userInput == []:
            userInput = input("> ").split()

        if userInput[0].lower() == "w>":
            UseWindowTerminal(" ".join(userInput[1:]))
            continue

        userInput = " ".join(userInput)
        # print(eval(userInput))
        exec(userInput)

        # except SyntaxError:
        #     exec(userInput)


def clr():
    """to clear shell, this prints a bunch of lines"""
    print("\n" * 30)
    print("\n" * 30)


def autoRepr(obj):
    """automatic repr

    from:
        https://stackoverflow.com/questions/750908/auto-repr-method
    """
    try:
        items = (str(v) for k, v in obj.__dict__.items())
        return f"{obj.__class__.__name__}({', '.join(items)})"
    except AttributeError:
        return repr(obj)

# JUNK
# -----------------------------------------------
# CorrectIntStr() takes a number in string format
# ..and returns it as integer in the given range.

# def CurrentDate(sep = "/" , in_num = true):
#     pass
#     from datetime import datetime
#     today()
#   const MONTHS = ["January", "February", "March", "Apirl", "May", "June", "July", "August", "September", "October", "November", "December"];
#   const WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];

#   var year = DATE.getFullYear(),
#       month = DATE.getMonth(),
#       day = DATE.getDate(),
#       weekday = DATE.getDay();

#   var currentDate = "";

#   if(in_num){
#     month++;
#     if (month<10) month = "0" + month;
#     if (day<10) day = "0" + day;
#     currentDate = year + sep + month + sep + day;
#   }

#   else{
#     currentDate = year + " " + MONTHS[month] + " "  + day + " "  + WEEKDAYS[weekday];
#   }
#   return currentDate;
#   }

# function CurrentTime(sep = ":"){
#     TIME = new Date();
#     var hrs = TIME.getHours() + 1,
#         min = TIME.getMinutes() + 1,
#         sec = TIME.getSeconds() + 1;

#     if (hrs<10) hrs = "0" + hrs;
#     if (min<10) min = "0" + min;
#     if (sec<10) sec = "0" + sec;

#     return a = hrs + sep + min + sep + sec;
#   }

# document.write(CurrentDate() + "</br>");
# document.write(CurrentDate("-") + "</br>");
# document.write(CurrentDate(undefined, 0) + "</br>");
# document.write("</br>");

# document.write(CurrentTime() + "</br>");
# document.write(CurrentTime("-") + "</br>");
#   </script>
# </body>
# </html>
#
# datetime.year
# Between MINYEAR and MAXYEAR inclusive.

# datetime.month
# Between 1 and 12 inclusive.

# datetime.day
# Between 1 and the number of days in the given month of the given year.

# datetime.hour
# In range(24).

# datetime.minute
# In range(60).

# datetime.second
# In range(60).

# datetime.microsecond
# In range(1000000).
