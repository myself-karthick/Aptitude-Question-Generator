from fractions import Fraction as frac
def format_decimal_latex(a):
    return_data = ""
    a = str(a)
    l = len(a)
    for e in a:
        if(e == '.'):
            if(a[-1] == '0'):
                break
            else:
                return_data += '\\cdot'
        else:
            return_data += e

    return return_data


def format_zero_integer_latex(a):
    if(a == 0):
        return ''
    else:
        return str(int(a))


def format_complexnumber_latex(a, b):

    operation = '+'
    if(b < 0):
        operation = '-'
        b *= -1
    a = format_zero_integer_latex(a)
    b = format_zero_integer_latex(b)
    if(b == '1'):
        b = ''

    if(a == ''):
       return "\\left(" + "i" + b + "\\right)"

    return "\\left(" + a + " " + operation + " i" + b + "\\right)"

def format_fraction_latex(Frac):
    a=Frac.numerator
    b=Frac.denominator
    return '\\frac{' + str(a) + '}{' +  str(b) + '}'
