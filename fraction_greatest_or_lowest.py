'''
    Name : Karthick M
    System id: hexint05
    My-id='3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    reviewer: Bhathrinaathan M B
    reviewer_id: 8d3ea48-d909-4d98-8c45-81d6abaceb1b
    Description: The programs generates random fraction and askes the user to find the largest or smallest to the given fraction from the randomly generated options
'''
from fractions import Fraction as frac
import json
import JSON_Data_Formatter
import LaTexFormatters
import random as rand

def get_json_format(question, answer, options):#Function converts the normal format into latex format.
    id = '3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    guid = '82fef919-16c6-46f9-8cbc-418de973c72b'
    name = 'Karthick M'
    final = JSON_Data_Formatter.format_to_json(id, name, guid, 'Bhathrinaathan M B', question, get_latex_fraction(options), '', LaTexFormatters.format_fraction_latex(answer), 5)
    print(json.dumps(final))


def get_latex_fraction(options):#Function converts the normal fraction options into latex formatted options
    new_options=[]
    for i in options:
        new_options.append(LaTexFormatters.format_fraction_latex(i))
    return new_options

def get_value(comp): #Function geneates a random fraction and returns it
    if(comp==1):
        return rand.randint(5,10)
    elif(comp==2):
        return rand.randint(11,20)
    else:
        return rand.randint(21,25)

def get_question(options, _Frac_):#Based on lowest or largest the question is created in the function
    low_high = rand.randint(0,1)# if low_high=0, then smallest to be found else largest
    min_max = "smallest" if(low_high==0) else "largest"
    question = "Find the "+str(min_max)+" fraction than "+str(_Frac_)+" from the following: "
    answer =  min(options) if(low_high==0) else max(options) #Answer is generated according to the question created
    get_json_format(question, answer, options)

def get_deciding_fraction():#Function generates random fraction to make options more randomized 
    n=rand.randint(0,1)
    num=rand.randint(1,5)
    den=rand.randint(1,5)
    num= num*-1 if(n==1) else num #If n=1 then the fraction is converted to negative by num*=1
    return frac(num,den)


def fact_zero(n, c):#Function handles the Zero exception, if denominator or numerator is zero
    if(c == 2):
        if(n == 0):
            n = rand.randint(10,20)
    else:
        if(n == 0):
            n = rand.randint(100,200)
    return n

def get_options(_Frac_, comp): #Function generates options for the passed the fraction
    temp = rand.randint(0,1)
    value = get_value(comp)
    temp_answer = value + _Frac_  if(temp==0) else value - _Frac_
    count=5
    options=[temp_answer]
    while(count>0):
        options.append(get_deciding_fraction()+temp_answer)#random options are generated and appended
        count-=1
    get_question(options, _Frac_)

def get_fraction(comp, negative, boundary):#Function generates fraction using randomization
    num = fact_zero( rand.randint(boundary[comp][0], boundary[comp][1]), 1) #Numrator is generated
    den = fact_zero( rand.randint(boundary[comp][0], boundary[comp][1]), 2) #Denominator is generated
    num = num * -1 if(negative==1) else num #The fraction will be converted to neagtive if negative =1
    get_options(frac(num,den), comp)

def get_complexity(comp):#Function contains the upper or lower limit of the fraction
    negative=rand.randint(0,1)#if negative=1 the fraction will be negative else positive
    boundary={
            1: ((1, 50)),
            2: ((101, 250)),
            3: ((500, 1000))
    }
    get_fraction(comp, negative, boundary)

if __name__ == '__main__': #main function
    comp = int(input("Enter the complexity: "))
    if(comp>=0 and comp<4):
        get_complexity(comp)
    else:
        print("Invalid")