'''
    Name : Karthick M
    System id: hetint05
    My-id='3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    reviewer: Bhathrinaathan M B
    reviewer_id: 08d3ea48-d909-4d98-8c45-81d6abaceb1b
    Description: The programs genearate question to find the Nth term of an AP and GP
                 using randomization.
'''
from fractions import Fraction as frac
import random as rand
import json
import JSON_Data_Formatter
import LaTexFormatters

def convert_json(question, answer, options):#Functions converts the format into json format
    id = '3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    guid = '82fef919-16c6-46f9-8cbc-418de973c72b'
    name = 'Karthick M'
    final = JSON_Data_Formatter.format_to_json(id, name, guid, 'Bhathrinaathan M B', question, options, '', answer, 5)
    print(json.dumps(final))

def get_latex_fraction(options):#Function converts the normal fraction into latex format
    new_options=[]
    for i in options:
        new_options.append(LaTexFormatters.format_fraction_latex(i))
    return new_options

def get_q(first, diff_ratio, apgp):#Function decides the question(AP or GP)
    if(apgp == 0):
        return  [first, round(first+diff_ratio, 1),round(first+diff_ratio+diff_ratio, 2)]
    else:
        return [first, round(first*diff_ratio, 1),round(first*diff_ratio*diff_ratio, 2)]

def get_answer(first, diff_ratio, terms, apgp):#Function decides the answer based on AP or GP
    if(apgp==0):
        return first+(terms-1)*diff_ratio
    else:
        return first*(diff_ratio**(terms-1))

def get_question(first, diff_ratio, terms, comp, apgp):#Function generates the random question of AP or GP
    q = get_q(first, diff_ratio, apgp)
    answer = get_answer(first, diff_ratio, terms, apgp)
    d = [-2, 1, -1, 2]
    if(comp == 2):
        answer = round(answer, 2)
    options = [answer]
    for i in d:
        options.append(round((answer+i), 1)) if(comp==2) else options.append(answer+i)
    rand.shuffle(options)
    ch = 'A.P' if(apgp == 0) else 'G.P'
    question = "Find the "+str(terms)+"th term of the " + ch + " series, "
    for i in range(0, len(q)):
        question += str(q[i])
        if(i != len(q)-1):
            question += ", "
    if(comp==3):
        options= get_latex_fraction(options)
        answer = LaTexFormatters.format_fraction_latex(answer)
    convert_json(question+" ...", answer, options)


def zero_check(n, m):#Function checks the zero and handles in case if it is fraction or decimal
    if(n == 0 and m == 2):
        return rand.randint(10,20)
    elif(n == 0 and m == 3):
        return rand.randint(100,200)
    return n


def fact_zero(n, c):#Function handles the Zero exception, if denominator is zero
    if(c == 2):
        if(n == 0):
            n = rand.randint(10,20)
        elif(n < 0):
            n = n*-1
    else:
        if(n == 0):
            n = rand.randint(100,200)
    return n


def get_terms(comp, boundary, apgp):#Function Gets the terms based on complexity
    if(comp == 1):
        first = rand.randint(boundary[comp][0][0], boundary[comp][0][1])
        diff_ratio = zero_check(rand.randint(boundary[comp][1][0], boundary[comp][1][1]), 2)
        terms = zero_check(rand.randint(boundary[comp][2][0], boundary[comp][2][1]), 3)
    elif(comp == 2):
        first = round(rand.uniform(boundary[comp][0][0], boundary[comp][0][1]), 1)
        diff_ratio = round(rand.uniform(boundary[comp][1][0], boundary[comp][1][1]), 1)
        terms = rand.randint(boundary[comp][2][0], boundary[comp][2][1])
    elif(comp == 3):
        num = fact_zero(rand.randint(boundary[comp][0][0], boundary[comp][0][1]), 1)
        den = fact_zero(rand.randint(boundary[comp][0][0], boundary[comp][0][1]), 2)
        diff_ratio_num = fact_zero(rand.randint(boundary[comp][1][0], boundary[comp][1][1]), 1)
        diff_ratio_den = fact_zero(rand.randint(boundary[comp][1][0], boundary[comp][1][1]), 2)
        first = frac(num, den)
        diff_ratio = frac(diff_ratio_num, diff_ratio_den)
        terms = zero_check(rand.randint(boundary[comp][2][0], boundary[comp][2][1]), 3)
    get_question(first, diff_ratio, terms, comp, apgp)


def get_complexity(comp):#Function decides the boundary based on the complexity and (AP or GP)
    apgp = rand.randint(0, 1)#if apgp=0, then it is AP, else GP
    boundary1 = {
        1: ((-101, 100), (-10, 10), (50, 150)),
        2: ((-101.5, 100.5), (-10.5, 10.5), (10, 100)),
        3: ((-50, 50), (-10, 10), (10, 50))
    }
    boundary2 = {
        1: ((-101, 100), (-10, 10), (5, 10)),
        2: ((-101.5, 100.5), (-5, 5), (5, 10)),
        3: ((-10, 10), (-5, 5), (5, 10))
    }
    if(apgp == 0):
        get_terms(comp, boundary1, apgp)
    else:
        get_terms(comp, boundary2, apgp)


if __name__ == '__main__': #main function
    comp = int(input("Enter the complexity: "))
    get_complexity(comp)
