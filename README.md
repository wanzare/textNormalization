Text normalization
==================
Given a html files for scientifx texts, normalize the text so as to extract relevant domain terminology

Example hml from [https://cellculturedish.com/]

## Requirements
- install nltk
- pip install bs4
- pip install num2words
- import nltk 
- nltk.download("stopwords")


##
 Create a domain specific vocabulary from the data
Procedure:
1. Load html files
2. Use BeautifulSoup package to extract only the text components of the html files
3. Preprocess text - remove urls, tokenize, lowercase, remove stopwords
4. Convert numeric words to spoken form # ToDo
5. Remove none word tokens e.g. punctuations, special characters and symbols, ignore words that contain none printable ascii characters
6. Put words to vocabulary dictionary
7. Save vocabulary to json file

## To run the code
```bash
python clean.py -i "   PATH TO FILES" -o "OUTPUT FILE TO SAVE THE VOCABULARY"
e.g. python clean.py -i ../files -o ../files/vocab.txt
```
