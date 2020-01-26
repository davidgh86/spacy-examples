# Initialize with the shared vocab
from spacy.matcher import Matcher
import spacy

nlp = spacy.load("en_core_web_md")

#matcher = Matcher(nlp.vocab)

# # Patterns are lists of dictionaries describing the tokens
# pattern = [{'LEMMA': 'love', 'POS': 'VERB'}, {'LOWER': 'cats'}]
# matcher.add('LOVE_CATS', None, pattern)
#
# # Operators can specify how often a token should be matched
# pattern = [{'TEXT': 'very', 'OP': '+'}, {'TEXT': 'happy'}]
# matcher.add('VERY_HAPPY', None, pattern)
#
# # Calling matcher on doc returns list of (match_id, start, end) tuples
# doc = nlp("I love cats and I'm very very happy")
# matches = matcher(doc)

matcher = Matcher(nlp.vocab)
matcher.add('DOG', None, [{'LOWER': 'golden'}, {'LOWER': 'retriever'}])
doc = nlp("I have a Golden Retriever")

for match_id, start, end in matcher(doc):
    span = doc[start:end]
    print('Matched span:', span.text)
    # Get the span's root token and root head token
    print('Root token:', span.root.text)
    print('Root head token:', span.root.head.text)
    # Get the previous token and its POS tag
    print('Previous token:', doc[start - 1].text, doc[start - 1].pos_)

from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

pattern = nlp("Golden Retriever")
matcher.add('DOG', None, pattern)
doc = nlp("I have a Golden Retriever")

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Get the matched span
    span = doc[start:end]
    print('Matched span:', span.text)


pattern = [{'LOWER': 'silicon'}, {'LOWER': 'valley'}]
doc = nlp("Can Silicon Valley workers rein in big tech from within?")