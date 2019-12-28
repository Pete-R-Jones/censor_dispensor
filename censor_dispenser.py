# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import string

def censor(phrase, document):
    new_word = ""
    censored_doc = document
    if phrase.lower() in document.lower():
        for letter in phrase:
            if (letter not in string.punctuation) and (letter not in " "):
                new_word += "X"
            else:
                new_word += letter
        censored_doc = document.lower().replace(phrase.lower(), new_word)
    return censored_doc

print(censor("learning algorithms", email_one))
