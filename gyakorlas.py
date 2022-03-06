def myfunc(string):
    output = ''
    for i in range(0,len(string)):
        if i % 2 == 1:
            output = output + string[i].upper()
        else:
            output = output + string[i].lower()
    print(output)

myfunc('sad')


#Write function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd 
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print(b)
            return b
        else:
            print(a)
            return a
    elif a > b:
        print(a)
        return a
    else:
        print(b)
        return b

lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)


#Write a function takes a two-word string and returns True if both 
#words begin with same letter
def animal_cracker(text):
    lista = text.split()
    if lista[0][0].lower() == lista[1][0].lower():
        print('yes')
        return True
    else:
        print('nope')
        return False

animal_cracker('Levelheaded Llama')
animal_cracker('Crazy Kangaroo')


 #Given a value, return a value that twice as far away
#on the other side of 7
def other_side_of_seven(num):
    if num == 7:
        return 7
    elif num < 7:
        print(((7 - num)*2) + 7)
        return ((7 - num)*2) + 7
    elif num > 7:
        print( 7 - (num - 7)*2  )
        return 7 - (num - 7)*2

other_side_of_seven(4)
other_side_of_seven(12)


#Write a function that capitalize the first and tourth letters of name
def old_macdonald(name):
    lista = list(name)
    lista[0] = name[0].upper()
    lista[3] = name[3].upper()
    string = ''
    for letter in lista:
        string = string + letter
    print(string) 
    return string

old_macdonald('macdonald')


#Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    lista = text.split()[::-1]
    string = ''
    for word in lista:
        string = string + word + ' ' 
    print(string)
    return string

master_yoda('I am home')
master_yoda('We are ready')


#Given an integer n, return True if n is whitin 10 of either 100 or 200
def almost_there(n):
    if ((n>=90 and n <=110) or (n>=190 and n <=210)) : 
        print('true')
        return True
    else:
        print('false')
        return False

almost_there(90)
almost_there(150)


#LEVEL 2
#Write a function that counts the number of times a given pattern appears in string, including overlap
def laugther(pattern,text):
    counter = 0
    for i in range(0,len(text)):
        if pattern in text[i:i + len(pattern)]:
            counter = counter + 1
    print(counter)

laugther('hah','hahahah') #ezt nem tudtam megcsinálni


#Given a list of ints, return True if the array contains
#a 3 next to a 3 somewhere
def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1,3,3]))
print(has_33([1,3,1,3]))


##Given a string, return a string where for every character 
#in the original there are three characters
def paper_doll(text):
    new_string = ''
    for i in range(0,len(text)):
        new_string = new_string + text[i]*3
    return new_string

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


#Given three integers between 1 and 11, if their sum is 
#less than or equal to 21, return their sum. 
#If their sum exceeds 21 and there's an eeleven,
#reduce the toal sum by 10. 
#If the sum exceeds 21, return 'BUST'
def blackjack(a,b,c):
    if (a == 11 or b == 11 or c == 11) and a+b+c<=31: return a + b + c -10
    elif a + b + c > 21: return 'BUST'
    else: return a+b+c

print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))


#Return the sum of the numbers in the array, except ignore 
#sections of numbers starting with a 6 and extending to the 
#next 9 (every 6 will be followed by at least one 9)
#Return 0 for no numbers
def summer_69(arr):
    pass

print(summer_69([1,3,5]))
print(summer_69([4,5,6,7,8,9]))
print(summer_69([2,1,6,9,11]))


#CHALLENGING PROBLEMS
#Write a function that takes in a list of integers and 
#returns True if it contains 007 in order
def spy_game(nums):
    for i in range(0,len(nums)):
        if nums[i]==0:
            for j in range(i,len(nums)):
                if nums[j]==0:
                    for k in range(j,len(nums)):
                        if nums[k]==7: return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


#Write a function that returns the number of prime
#numbers that exist up to and including a given number
def count_primes(num):
    counter = 0
    for i in (2,num):
        for j in (2,i):
            if i % j == 0: continue
            else: counter = counter + 1
    return counter


print(count_primes(100))    


def print_big(letter):
    lista = [' x ', 'x x', 'xxx', 'x x', 'x x', '---']
    listb = ['xx ', 'x x', 'xx ', 'x x', 'xx ', '---']
    listc = [' x ', 'x x', 'x  ', 'x x', ' x ', '---']
    listd = ['xx ', 'x x', 'x x', 'x x', 'xx ', '---']

    if letter == 'a': 
        for line in lista: print(line)
    if letter == 'b': 
        for line in listb: print(line)
    if letter == 'c': 
        for line in listc: print(line)
    if letter == 'd': 
        for line in listd: print(line)

print_big('a')
print_big('b')
print_big('c')
print_big('d')