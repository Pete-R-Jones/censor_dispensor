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

# print(censor("learning algorithms", email_one))

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

# print(censor_many(proprietary_terms, email_two))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_3(censor_phrases, negative_words, document):
    censored_doc = document
    document_words = []
    document_phrases_2 = []
    document_phrases_3 = []
    j = 0
    for i in document.split():
        k = i.split("\n")
        for word in k:
            document_words.append(word)
    for i in range(len(document_words)-1):
        document_phrases_2.append(document_words[i] + " " + document_words[i+1])
    document_phrases_2.append("")
    for i in range(len(document_words)-2):
        document_phrases_3.append(document_words[i] + " " + document_words[i+1] + " " + document_words[i+2])
    document_phrases_3.append("")
    document_phrases_3.append("")
    count = 0
    while j < len(document_words):
        new_word = ""
        if document_words[j].lower().translate(str.maketrans('', '', string.punctuation)) in censor_phrases:
            for letter in document_words[j]:
                if (letter not in string.punctuation):
                    new_word += "X"
                else:
                    new_word += letter
            document_words[j] = new_word
            j += 1
        elif document_phrases_2[j].lower().translate(str.maketrans('', '', string.punctuation)) in censor_phrases:
            temp = []
            for letter in document_phrases_2[j]:
                if (letter not in string.punctuation) and (letter not in " "):
                    new_word += "X"
                else:
                    new_word += letter
            temp = new_word.split()
            document_words[j] = temp[0]
            document_words[j+1] = temp[1]
            j += 2
        elif document_phrases_3[j].lower().translate(str.maketrans('', '', string.punctuation)) in censor_phrases:
            temp = []
            for letter in document_phrases_3[j]:
                if (letter not in string.punctuation) and (letter not in " "):
                    new_word += "X"
                else:
                    new_word += letter
            temp = new_word.split()
            document_words[j] = temp[0]
            document_words[j+1] = temp[1]
            document_words[j+2] = temp[2]
            j += 3
        elif (document_words[j].lower().translate(str.maketrans('', '', string.punctuation)) in negative_words) or (document_phrases_3[j].lower().translate(str.maketrans('', '', string.punctuation)) in negative_words):
            count += 1
            if count > 2:
                if document_words[j].lower().translate(str.maketrans('', '', string.punctuation)) in negative_words:
                    for letter in document_words[j]:
                        if (letter not in string.punctuation):
                            new_word += "X"
                        else:
                            new_word += letter
                    document_words[j] = new_word
                    j += 1
                elif document_phrases_3[j].lower().translate(str.maketrans('', '', string.punctuation)) in negative_words:
                    temp = []
                    for letter in document_phrases_3[j]:
                        if (letter not in string.punctuation) and (letter not in " "):
                            new_word += "X"
                        else:
                            new_word += letter
                    temp = new_word.split()
                    document_words[j] = temp[0]
                    document_words[j+1] = temp[1]
                    document_words[j+2] = temp[2]
                    j += 3
            elif document_words[j].lower().translate(str.maketrans('', '', string.punctuation)) in negative_words:
                j += 1
            else:
                j+= 3
        else:
            j += 1
    return " ".join(document_words)

print(censor_3(proprietary_terms, negative_words, email_three))

