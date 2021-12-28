# 1. Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:
#
# # = 5
# O = 3
# X = 1
# ! = -1
# !! = -3
# !!! = -5
#
# A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.
#
# If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

def checklist(l):
    d={"#" :5,"O" : 3,"X" : 1,"!" : -1,"!!" : -3,"!!!" : -5}
    sum=0
    for i in l:
        if type(i)== list:
            for j in i:
                sum=sum+d[j]
    if sum>0:
        return sum
    else:
        return 0

print(checklist([["#", "!"],["!!", "X"]]))

print(checklist([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]]))

# 2. Create a function that takes a variable number of arguments, each argument representing the number of items in a group, and returns the number of permutations (combinations) of items that you could get by taking one item from each group.
#
# Examples
#
# combinations(2, 3) ➞ 6

def combinations(*args):
    j=1
    for i in args:
        j=j*i

    return j

print(combinations(2, 3))
print(combinations(2, 3, 4, 5))
print(combinations(3, 7, 4))

# 3. Create a function that takes a string as an argument and returns the Morse code equivalent.
#
# Examples
#
# encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
#
# encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

def encode_morse(string):
    char_to_dots = {
      'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
      'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
      '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
      '6': '-....', '7': '--...', '8': '---..', '9': '----.',
      '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
      ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
      '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    newstr=""
    for i in string:
        if i in char_to_dots:
            newstr=newstr+" "+char_to_dots[i]
    return newstr

print(encode_morse("HELP ME !"))
print(encode_morse("EDABBIT CHALLENGE") )


# 4.  Write a function that takes a number and returns True if it's a prime; False otherwise. The number can be 2^64-1 (2 to the power of 63, not XOR). With the standard technique it would be O(2^64-1), which is much too large for the 10 second time limit.

from math import sqrt
def prime(no):
    prime_flag = 0

    if (no > 1):
        for i in range(2, int(sqrt(no)) + 1):
            if (no % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            print("True")
        else:
            print("False")
    else:
        print("False")

prime(7)
prime(56963)
prime(5151512515524)

# 5.  Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:
#
#     1. Locate the position of the letter in the English alphabet (from 1 to 26).
#     2. Odd positions will be represented as 1 and 0 otherwise.
#     3. Convert the represented positions to boolean values, 1 for True and 0 for False.
#     4. Store the conversions into an array.
import string
def to_boolean_list(name):
    li=[]
    for i in name:
         num=string.ascii_lowercase.index(i) +1
         if num%2 == 0:
             li.append(False)
         else:
             li.append(True)
    return li

print(to_boolean_list("deep"))
print(to_boolean_list("loves"))
