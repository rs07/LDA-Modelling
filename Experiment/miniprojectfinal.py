import gensim
import os
filelist=os.listdir("Articles")
for a in range(len(filelist)):
    filelist[a] = "Articles/"+filelist[a]
#FOR CLEANING THE DOCUMENT
#SUCH AS REMOVING OF STOPWORDS LIKE - a, and, the, in , or, etc.
#REMOVING OF PUNCTUATION MARKS LIKE- "." , ","
#BRINGING THE WORD TO THEIR ROOT WORD
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string
stop=set(stopwords.words("english"))
exclude=set(string.punctuation)
lemma=WordNetLemmatizer()
def clean(file):
    a=open(file)
    doc=a.read()
    doc = word_tokenize(doc)
    doc=[a for a in doc if a.lower() not in stop]
    doc=[a for a in doc if a not in exclude]
    doc=[a for a in doc if a.isalpha()]
    doc=" ".join(lemma.lemmatize(a) for a in doc)
    a.close()
    return doc
doc_clean=[clean(t).split() for t in filelist]
#FOR DOCUMENT TERM MATRIX
from gensim import corpora

dictionary = corpora.Dictionary(doc_clean)
doc_term_matrix= [dictionary.doc2bow(doc) for doc in doc_clean]

#CREATING THE OBJECT FOR LDA MODEL
LDA = gensim.models.ldamodel.LdaModel

#Running and Training LDA model on th document Term Matrix
ldamodel = LDA(doc_term_matrix, num_topics=10, id2word=dictionary, passes=100)
print(ldamodel.print_topics(num_topics=10, num_words=10))
