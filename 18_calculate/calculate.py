def calculate(operation, a, b, make_int=False, message='The result is'):
    """Identifies which math calculation to use on inputs a and b.
    Runs the desired calculation and returns the result plus a message (defaulted to 'The result is').
    If no operation is properly provided, returns None.
    """
    if make_int == True:
        a = int(a)
        b = int(b)
    if operation == 'add':
        result = a + b
        return message + f" {result}"
    if operation == 'subtract':
        result = a - b
        return message + f" {result}"
    if operation == 'multiply':
        result = a * b
        return message + f" {result}"
    if operation == 'divide':
        result = a / b
        return message + f" {result}"
    else:
        return None
