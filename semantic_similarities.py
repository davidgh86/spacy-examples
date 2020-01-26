import spacy

# Load a larger model with vectors
nlp = spacy.load('en_core_web_md')

# Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like water")
doc3 = nlp("I don't like water")
doc4 = nlp("The dog is black")
print(doc1.similarity(doc2))
print(doc1.similarity(doc3))
print(doc1.similarity(doc4))

# Compare two tokens
doc = nlp("I like pizza, pasta and traffic")
token1 = doc[2]
token2 = doc[4]
token3 = doc[6]
print(token1.similarity(token2))
print(token1.similarity(token3))
print(doc4.similarity(doc[6]))

import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)


import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# Get the similarity of the tokens "TV" and "books"
similarity = token1.similarity(token2)
print(similarity)


import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Get the similarity of the spans
similarity = span1.similarity(span2)
print(similarity)
