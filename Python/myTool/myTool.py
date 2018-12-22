from functools import wraps

import os

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
    
