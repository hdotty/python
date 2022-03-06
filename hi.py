print("Hello World!")


st = 'Print only the words that starts with s in this sencence'
words = st.split()
for word in words:
    if word[0] == 's':
        print(word)


for num in range(0,11):
    if num % 2 == 0:
        print(num)

harmasok = []
for num in range(1,51):
    if num % 3 == 0:
        harmasok.append(num)
print(harmasok)

st1 = 'Print every word in this sentence that has an even number of letters'
words1 = st1.split()
for word in words1:
    if len(word) % 2 == 0:
        print(word, 'even!')

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, 'FizBuzz')
    elif num % 3 == 0:
        print(num, 'Fizz')
    elif num % 5 == 0:
        print(num, 'Buzz')

for num in range(1,101):
    if num % 3 == 0:
        if num % 5 == 0:
            print(num, 'FrizzBuzz')
        else: 
            print(num, 'Frizz')
    elif num % 5 == 0:
        print(num, 'Buzz')

st2 = 'Create a list of the first letters of every word in this string'
first_letters = []
for word in st2.split():
    first_letters.append(word[0])
print(first_letters)
