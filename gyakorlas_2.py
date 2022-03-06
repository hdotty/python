#write a function that computes the volume of a sphere given its radius
pi = 3.14
def vol(rad):
    return (4*pi*(rad**3))/3

print(vol(2))


#Write a function that checks whether a number is in a given range 
def ran_check(num,low,high):
    #return num in range(low,high+1)
    return num<high and num>low

print(ran_check(5,2,7))
print(ran_check(3,1,10))
print(ran_check(1,3,6))


#Write a finction that accepts a string and calculates the number of upper case
#letters and lower case letters.
def up_low(s):
    up = 0
    low = 0
    for letter in s:
        if letter.isupper(): up += 1
        elif letter.islower(): low += 1
    print('Original string: {}'.format(s))
    print('No. of Upper case characters: {}'.format(up))
    print('No. of Lower case characters: {}'.format(low))

up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


#Write a function that takes a list and returns a new list with unique 
#elements of the list
def unique_list(lst):
    return list(set(lst))

print(unique_list([1,1,1,1,2,2,2,3,3,3,4,5]))


#write a function to multiply all the numbers in a list
def multiply(numbers):
    multi = 1
    for item in numbers: multi *= item
    return multi

print(multiply([1,2,3,-4]))


#Write a function that checks whether a word or pharse is palindrome or not
def palindrome(s):
    nospace = ''
    for letter in s:
        if letter == ' ': continue
        else: nospace += letter
    return nospace.lower() == nospace.lower()[::-1]
#itt is lehetett volna használni a replace()-t!!
print(palindrome('asd'))
print(palindrome('he heh'))
print(palindrome('Indul a gorog aludni'))


#Write a function to check whether a string is pangram or not
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    str2 = str1.replace(' ','').lower()
    for letter in alphabet:
        if letter in str2: continue
        else: return False
    return True
#set-el is meg lehetett volna oldani
print(ispangram('Asd fklr'))
print(ispangram('The quick brown fox jumps over the lazy dog'))


