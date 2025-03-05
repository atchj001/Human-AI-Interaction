
import numpy as np 
import random
import sklearn
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import pairwise_distances
import pandas as pd
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from spell_check import text_preprocessing

# un = user name
# for when changing names
CN = ["rename", "switch", "change", "call"] # CN change name
NAME = ["call", "me", "change", "my", "name", "to", "please", "rename", "switch", "yes", "sure"]

def check_name_change(input):
    text_tokens = word_tokenize(input)
    if not set(text_tokens).isdisjoint(CN):
        return True
    else:
        return False

def name_change(input):
    text_tokens = word_tokenize(input)
    un = [i for i in text_tokens if not i.lower() in NAME and i.isalpha() and not i.lower() in stopwords.words('english')]
    un = (' ').join(un)
    return un

# dataset path
data_path = './dataset/name.csv'

def name_response(query, threshold):

    df = pd.read_csv(data_path)

    # TF-IDF
    tfidf_vec = TfidfVectorizer(analyzer='word')
    X_tfidf = tfidf_vec.fit_transform(df['Question']).toarray()
    df_tfidf = pd.DataFrame(X_tfidf, columns = tfidf_vec.get_feature_names_out())

    # process query 
    input_tfidf = tfidf_vec.transform([query.lower()]).toarray()

    # cosine similarity
    cos = 1 - pairwise_distances(df_tfidf, input_tfidf, metric = 'cosine')
    
    if cos.max() >= threshold:
        return 'RESPOND'
    else:
        return 'NOT FOUND'
    
