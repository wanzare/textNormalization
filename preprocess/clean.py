from bs4 import BeautifulSoup
from num2words import num2words
import json
import getopt,sys
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from collections import defaultdict



def remove_urls (text):
    '''
    method to remove urls from text
    :param text: string
    :return: string with http|https links removed
    '''
    text = re.sub(
        r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
        "", text)
    return(text)
def num_there(s):
    """
    method to check if a sttring contains a numeric
    :param s: string
    :return: True if s contains a numeric
    """
    return any(i.isdigit() for i in s)
def load_files(path):
    '''
    method to load the path to all html files in a list
    :param path: path to the html files
    :return: list of paths
    '''
    data = []
    for entry in os.scandir(path):
        if ".html" in entry.path:
            data.append(entry.path)
    return data
def processFile(file,clean_vocab):
    '''
    method to clean the html files and return the vocabulary
    :param file: html file
    :param clean_vocab: dictionary to hold the words
    :return: vocabulary
    '''

    soup = BeautifulSoup(open(file), "html.parser").get_text() # get only the text component of the html files
    word_tokens = word_tokenize(remove_urls(soup))#  remove urls, tokenize the text
    words = [w.lower() for w in word_tokens if w not in stop_words]#lowercase
    type(words)#get the unique words in the document
    vocab = words
    # convert number to spoken form
    for word in vocab:
        num=num_there(word)
        if num:
            try:
                #print(word)
                word = num2words(word)
                #print(word)
            except TypeError:
                m = re.finditer(r"[0-9]+", word)
                n = re.finditer(r"[^0-9]+", word)
                print([x.span() for x in m], word)
                print([x.span() for x in n])

                '''
                TODO: handle cases where the number is between other letters e.g. CO2, 34-34
                '''
                continue

        # remove/ignore words with non printable ascii characters
        try:
            word.encode("ascii")
        except UnicodeEncodeError:
            #print(word)
            #print("Invalid string")
            continue

        c_word = re.sub('\W+', ' ', word)# remove not word tokens e.g. punctuations, special characters and symbols
        #store the words in the dictionary
        if len(c_word) > 1:
            #print(c_word)
            clean_vocab[c_word] +=1

    return clean_vocab


# Get all English stop words
stop_words = set(stopwords.words('english'))

if __name__ == '__main__':
    unixOptions = "i:o:"
    gnuOptions = ["input=", "output="]
    options=len(sys.argv[1:])
    if options!=4:
        print("Give valid options: -i (path to html files), -o (output file to save)")
        sys.exit(2)
    argumentList = sys.argv[1:]
    try:
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        print(str(err))

    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--input"):
            path=currentValue
        elif currentArgument in ("-o", "--output"):
            save_file=open(currentValue, "w")
    data = load_files(path)
    clean_vocab = defaultdict(int)

    for file in data:
        print(file)
        clean_vocab= processFile(file,  clean_vocab)
    #print(clean_vocab)
    json.dump(clean_vocab,save_file)