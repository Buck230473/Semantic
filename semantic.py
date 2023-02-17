# importing spacy
import spacy
# specify the model
nlp = spacy.load('en_core_web_md')

# loop through the words and compare similarities to each other
# display the results
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

######################### What I found interesting #########################
# when the same 2 items are compared it will return 1.0
# a monkey with a fruit scores higher then a cat with a fruit. Probably because cats don't eat fruit
# interestingly enough the 2 fruits together score higher in similarity than the 2 animals
# monkey and banana scored higher than any other animal/fruit combination. Because monkeys are known for eating bananas.



######################### My Example #########################
# loop through the words and compare similarities to each other
# display the results
tokens = nlp('shirt dress man woman')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

######################### What I found interesting #########################
# woman and dress scores higher than woman and shirt.
# man and woman had the highest similarity (even more than shirt and dress).
# shirt and woman had the lowest similarity.
# man and dress had higher similarity than woman and shirt. Because dress can also be used as a verb.


######################### Change to simpler language model #########################
nlp = spacy.load('en_core_web_sm')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
      print(token1.text, token2.text, token1.similarity(token2))

# Message appears in the console suggesting it may not give similarity judgements.
# Results differed significantly from the md model
# Results appear to be less accurate e.g. monkey and apple scored higher than monkey and apple.