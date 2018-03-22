import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
text="hello world this is a simple text. Mr. Jack & Mrs. Jill went up the Hill"
sents=sent_tokenize(text)
print(sents)
