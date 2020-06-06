# File:            caesar_cipher-progex5.8.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.8
# Description:

#   One problem with the previous exercise is that it does not deal with the
#   case when we "drop off the end" of the alphabet. A true Caesar cipher does
#   the shifting in a circular fashion where the next character after "z" is
#   "a." Modify your solution to the previous problem to make it circular. You
#   may assume that the input consists only of letters and spaces. Hint: make a
#   string containing all the characters of your alphabet and use positions in
#   this string as your code. Yo do not have to shift "z" into "a" just make
#   sure that you use a circular shift over the entire sequence of character in
#   your alphabet string.

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program encodes a Caesar cipher for a plaintext message.")

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    message = input("Insert message: ").split()
    key = int(input("Insert cipher key (integer value): "))

    emessage = []
    for word in message:
        eword = []
        for letter in word:
            if letter in alphabet:
                eword.append(
                        alphabet[ (alphabet.find(letter) + key) % 26 ]
                        )
            elif letter in alpha_upper:
                eword.append(
                        alpha_upper[ (alpha_upper.find(letter) + key) % 26 ]
                        )
            else:
                eword.append(letter)
        emessage.append("".join(eword))

    print("Encoded message:", *emessage)

#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
