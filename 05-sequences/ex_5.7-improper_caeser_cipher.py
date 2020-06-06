# File:            improper_caesar_cipher-progex5.7.py
# Date:            2019-10-19
# Author:          "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:        prog ex 5.7
# Description:
#   A Caesar cipher is a simple substitution based on the idea of shifting each
#   letter of the plaintext message a fixed number (called the key) of
#   positions in the alphabet. For example, if the key value is 2, the word
#   "Sourpuss" would be encoded as "Uqwtrwuu." The original message can be
#   recovered by "reencoding" it using the negative of the key.
#
#   Write a program that encode and decode Caesar ciphers. The input to the
#   program will be a string of plaintext and the value of the key. The output
#   will be an encoded message where each character in the original message is
#   replaced by shifting it 'key' characters in the Unicode character set. For
#   example, if `ch` is a character in the string `key` is the amount to shift,
#   then character that replaces `ch` can be calculated as: `chr(ord(ch) + key)`

#------------------------------------------------------------------------------
# FUNCTIONS
#------------------------------------------------------------------------------
def main():
    print("Program encodes a Caesar cipher for a plaintext message.")

    message = input("Insert message: ").split()
    key = int(input("Insert cipher key (integer value): "))

    emessage = []
    for word in message:
        eword = []
        for letter in word:
            eword.append(chr(ord(letter) + key))
        emessage.append("".join(eword))

    print("Encoded message:", *emessage)



#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
