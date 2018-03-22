doc1= "India is a very good country. There are many religions in India."
doc2= "IIEST is founded in 2014. Before that its name was Bengal Engineering Science University."
doc3= "I am from Chittaranjan. Chittaranjan is a very nice and clean place in India."
doc4= "I am a second year Student currently studying in IIEST."
doc5= "My sister is in the 12th class. She studies in Kendriya Vidyalaya Chittaranjan."
doc_complete=[doc1, doc2, doc3, doc4, doc5]


from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
stop=set(stopwords.words('english'))
exclude=set(string.punctuation)
lemma= WordNetLemmatizer()
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    return normalized

doc_clean = [clean(doc).split() for doc in doc_complete]

print("Cleaned Document")
for doc in doc_clean:
    print(doc)
    
print("\n")
# Importing Gensim
import gensim
from gensim import corpora

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
dictionary = corpora.Dictionary(doc_clean)
print(dictionary)
print(dictionary.token2id)
# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]
print("\n")
print(doc_term_matrix)

# Creating the object for LDA model using gensim library
#Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
#ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)


#print(ldamodel.print_topics(num_topics=3, num_words=3))
