# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 13:02:23 2022

@author: David Luby

# CS 410P - Lab assignment 16L

# intake gettysburg.txt
    # strip out all punctuation and make the address case insenstive
    # store every unique word in the dictionary as a key (0 initially)
        # add one to each key value for repeat words
        # print every word that appears at least three times
            # in order of most to least occurrences

"""
file = open("Gettysburg.txt",'r')
speech=[]
for word in file:
    #words.append(word.strip().rstrip(".").rstrip(",").rstrip(":").split(" "))
        speech.append(word.strip().split(" "))
file.close()

clean = []
insens = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f','G':'g','H':'h',
        'I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o','P':'p',
        'Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x',
        'Y':'y','Z':'z'}
characters =  '.,:'
case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for speeches in speech:
    for words in speeches:
        for letters in words:
            if letters in characters:
                words = words.replace(letters,"")
            elif letters in case:
                words = words.replace(letters,insens[letters])
        clean.append(words)

frequency = {}
wCount = 0
for words in clean:
    wCount +=1
    if (words in frequency):
        frequency[words] +=1
    else:
        frequency[words] =1
print("There are ",wCount," words")
print("There are ",len(frequency)," unique words")
print("The most common words are: ")
ordered = sorted(frequency.items(), reverse = True, key = lambda item:item[1])
for x in ordered:
    if x[1] >=3:
        print(x)