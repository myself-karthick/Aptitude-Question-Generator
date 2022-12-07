'''
    Name: Karthick M
    System id: hexint05
    Program: Subtraction in Complex number
    Description:    The programs performs subtraction in the range of complex numbers, and using randomization
                    the options are generated for enchancing difficulty of the problem.
'''
import random as rand
import LaTexFormatters
import json
import JSON_Data_Formatter

def display(options, answer,question): #The displays the question, option and author details in JSON format
    latex_answer=LaTexFormatters.format_complexnumber_latex(answer.real,answer.imag)
    latex_options=[]
    for i in options:
        latex_options.append(LaTexFormatters.format_complexnumber_latex(i.real,i.imag))
    i_d='3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    guid='82fef919-16c6-46f9-8cbc-418de973c72b'
    name=['Karthick M','john bauer']
    final=JSON_Data_Formatter.format_to_json(i_d,name[0],guid,name[1],question,latex_options,'',latex_answer,4)
    print(json.dumps(final))


def sub(complex_list): #Function performs subtraction of complex numbers and return the final value
    t1 = complex_list[0].real
    t2 = complex_list[0].imag
    z = complex(t1, t2)
    for i in range(1, len(complex_list)):
        z = z-complex_list[i]
    return z


def generate_options(complex_list, question):#This function generates options based on randomization
    answer = sub(complex_list)
    options = [answer]
    diff = [-1, -2, 1]
    Len = 2
    for i in range(0, 3):
        z1 = answer.real+i
        z2 = answer.imag+diff[Len]
        Len -= 1
        options.append(complex(z1, z2))
    display(options, answer, question)


def get_complexity(comp): #Function decides the range of numbers for the complex number based on the complexity passed
    boundary = {
                1: ((-10, -1), (1, 10), (2)),
                2: ((-50, -11), (11, 50), (3)),
                3: ((-500, -51), (51, 500), (4)),
                4: ((-3000, -501), (501, 3000), (5)),
                5: ((-10000, -3001), (3000, 10000), (5))
                }
    complex_list = []
    taken = rand.randint(0, 1)
    question=""
    for i in range(0, boundary[comp][2]):
        if(i==0):
            ch=''
        else:
            ch ='+'
        real = rand.randint(boundary[comp][taken][0], boundary[comp][taken][1])
        taken = rand.randint(0, 1)
        imag = rand.randint(boundary[comp][taken][0], boundary[comp][taken][1])
        question += ch + LaTexFormatters.format_complexnumber_latex(real,imag)
        complex_list.append(complex(real, imag))
    generate_options(complex_list,question)


if __name__ == '__main__':#Main function which asks for the complexity level
    comp = int(input("Enter the complexity : "))
    get_complexity(comp)
