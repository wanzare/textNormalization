Text notmalization
==================
Given a html files for scientifx texts, normalize the text so as to extract relevant domain terminology

Example hml from [https://cellculturedish.com/]

## Requirements
pip install nltk
pip install bs4
pip install num2words

##
 Create a domain specific vocabulary from the data
Procedure:
1: Load html files
2: Use BeautifulSoup package to extract only the text components of the html files
3: Preprocess text - remove urls, tokenize, lowercase
4: Convert numeric words to spoken form
5: Remove none word tokens e.g. punctuations, special characters and symbols, ignore words that contain none printable ascii characters
6: Put words to vocabulary dictionary
7: Save vocabulary to json file