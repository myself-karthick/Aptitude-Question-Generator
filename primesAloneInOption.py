'''
Author:
    Name : Karthick M
    System id: hetint05
    My-id='3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    reviewer: Bhathrinaathan M B
    reviewer_id: 8d3ea48-d909-4d98-8c45-81d6abaceb1b
    Description: The program generates randon list of numbers, the options will contain
                    one correct option which contains the all the numbers are prime 
'''
import random
import json
import JSON_Data_Formatter

def convert_json(question, answer, options): #Function converts the format into json format
    id = '3c1f7834-0265-4c6f-8f33-34f1dfa358c2'
    guid = '8d3ea48-d909-4d98-8c45-81d6abaceb1b'
    name = 'Karthick M'
    final = JSON_Data_Formatter.format_to_json(id, name, guid, 'Bhathrinaathan M B', question, options, '', answer, 4)
    print(json.dumps(final))

def primes_in_range(x,y):# Function to get the prime numbers in a range and return the prime numbers as list
    prime_list = []
    for n in range(x, y):
        is_prime = True

        for num in range(2, n):
            if n % num == 0:
                is_prime = False

        if is_prime:
            prime_list.append(n)

    return prime_list


def generate_random_prime(x,y,length):  # Function generates randon prime number
    prime_list = primes_in_range(x, y)
    final_prime = []
    index = 0
    while(index < length):
        num = random.choice(prime_list)
        if(num not in final_prime):
            final_prime.append(num)
            index += 1
    return final_prime


def generateList(Len, x, y):  # Functions generates the random list oof prime number
    List = []
    while(Len > 0):
        num = random.randint(x, y)
        if(num not in List):
            List.append(num)
            Len -= 1
    return List


# Functions generates the options based the given complexity 
def generate_options(rand_prime, x, y):
    count = 0
    options = []
    options.append(rand_prime)
    while(count < 4):
        options.append(generateList(len(rand_prime), x, y))
        count += 1
    random.shuffle(options)
    answer = options.index(rand_prime)
    question="Find the sequences which contains prime numbers alone"
    convert_json(question,options[answer],options)

def generate_prime(comp):#Function generates prime based on complexity
    rand_prime = []
    if(comp == 1):  # 2nd standard
        rand_prime = generate_random_prime(1, 100, 6)
        generate_options(rand_prime, 1, 100)
    elif(comp == 2):  # 8th standard
        rand_prime = generate_random_prime(100, 1000, 8)
        generate_options(rand_prime, 100, 1000)
    elif(comp == 3):  # 10th standard to 12
        rand_prime = generate_random_prime(1000, 10000, 10)
        generate_options(rand_prime, 1000, 10000)

# Gets the complexity from the user
if __name__ == "__main__":
    comp = int(input("Enter the complexity: "))
    generate_prime(comp)