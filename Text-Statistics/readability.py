import os
from textstat.textstat import textstat
import csv
from csv import DictWriter

direc = os.getcwd() # Get current working directory
ext = '.txt' # Select your file delimiter
univ = '5filename' #name for csv file
uni = {}# Create an empty dict

# Select only files with the ext extension
txt_files = [i for i in os.listdir(direc) if os.path.splitext(i)[1] == ext]
print (txt_files)

#setup the csv file structure
myfile = open(univ + '.csv', 'wb')
myfields = ['department', 'character count', 'syllable count', 'lexicon count', 'sentence count', 'polysyllable count', 'difficult words', 'average letter per word', 'average sentence lenght', 'average sentence per word', 'average syllables per word', 'smog index', 'automated readability index', 'coleman liau index', 'dale chall readability score', 'flesch kincaid grade', 'flesch reading ease', 'gunning fog index', 'linsear write formula', 'text standard']
with myfile:
    writer = csv.DictWriter(myfile, fieldnames=myfields)
    writer.writeheader()

# Iterate over your txt files
for i in txt_files:
    # Open them and doe the readability calculations and writes the result to the csv
    with open(os.path.join(direc,i)) as file_object:
        print ('working on ' + i)
        uni['department'] = i
        content = file_object.read()
        uni['character count'] = textstat.char_count(content)
        print ('    calculated the amount of characters')
        uni['syllable count'] = textstat.syllable_count(content)
        print ('    calculated the amount of syllables')
        uni['lexicon count'] = textstat.lexicon_count(content)
        print ('    calculated lexicon')
        uni['sentence count'] = textstat.sentence_count(content)
        print ('    calculated the amount of sentences')
        uni['polysyllable count'] = textstat.polysyllabcount(content)
        print ('    calculated the amount of polysyllable')
        uni['difficult words'] = textstat.difficult_words(content)
        print ('    calculated the amount of difficult words')
        uni['average letter per word'] = textstat.avg_letter_per_word(content)
        print ('    calculated the average letter per word')
        uni['average sentence lenght'] = textstat.avg_sentence_length(content)
        print ('    calculated average sentence lenght')
        uni['average sentence per word'] = textstat.avg_sentence_per_word(content)
        print ('    calculated average sentence per word or is it word per sentence?')
        uni['average syllables per word'] = textstat.avg_syllables_per_word(content)
        print ('    calulated average syllable per word')
        uni['smog index'] = textstat.smog_index(content)
        print ('        did smog index')
        uni['automated readability index'] = textstat.automated_readability_index(content)
        print ('        did automated readability index')
        uni['coleman liau index'] = textstat.coleman_liau_index(content)
        print ('        did coleman liau index')
        uni['dale chall readability score'] = textstat.dale_chall_readability_score(content)
        print ('        did dale chall readability score')
        uni['flesch kincaid grade'] = textstat.flesch_kincaid_grade(content)
        print ('        did flesch kincaid grade')
        uni['flesch reading ease'] = textstat.flesch_reading_ease(content)
        print ('        did flesch reading ease')
        uni['gunning fog index'] = textstat.gunning_fog(content)
        print ('        did gunngin fog index')
        uni['linsear write formula'] = textstat.linsear_write_formula(content)
        print ('        did linsear write formula')
        uni['text standard'] = textstat.text_standard(content)
        print ('        did text standard')
        print ('start writing to csv')
        myfile = open(univ + '.csv', 'ab')
        with myfile:
           writer = csv.DictWriter(myfile, fieldnames=myfields)
           writer.writerow(uni)
        print ('finished writing')
print (uni)
