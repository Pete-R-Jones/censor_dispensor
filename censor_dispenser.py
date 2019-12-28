# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

import string
import re

def censor(phrase, document):
    new_word = ""
    censored_doc = document
    if phrase.lower() in document.lower():
        for letter in phrase:
            if (letter not in string.punctuation) and (letter not in " "):
                new_word += "X"
            else:
                new_word += letter
        insensitive_phrase = re.compile(re.escape(phrase), re.IGNORECASE)
        censored_doc = insensitive_phrase.sub(new_word, document)
    return censored_doc

print(censor("learning algorithms", email_one))

def censor_many(phrases, document):
    censored_doc = document
    for i in range(len(phrases)):
        new_word = ""
        if phrases[i].lower() in document.lower():
            for letter in phrases[i]:
                if (letter not in string.punctuation) and (letter not in " "):
                    new_word += "X"
                else:
                    new_word += letter
        insensitive_phrase = re.compile(re.escape(phrases[i]), re.IGNORECASE)
        censored_doc = insensitive_phrase.sub(new_word, censored_doc)
    return censored_doc

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

print(censor_many(proprietary_terms, email_two))
