import pandas as pd

listeChateaux = ['Versailles', 'Fontainebleau', 'VauxVicomte', 'Vaux-le-Vicomte', 'Amboise', 'Azay_le_Rideau', 'Chambord', 'Chantilly', 'Chenonceau', 'Cheverny', 'Villandry', 'Usse', 'Beynac', 'Blois', 'Koenigsbourg', 'Bretagne', 'Pierrefonds', 'Angers', 'Castelnaud', 'Murol']
categorie = ['excellent', 'mediocre', 'horrible']

import os

listCSV = []
for chateau in listeChateaux:
    for cat in categorie:
        filename = 'csv/' + cat + chateau + '.csv'
        if os.path.isfile(filename):
            fileCSV = pd.read_csv(filename,encoding='utf8')
            if chateau == 'Versailles':
                fileCSV.insert(loc=0,column='Chateau',value='Versailles')
            
            listCSV.append(fileCSV)
            
## Concatener all dataframes
dt = pd.concat(listCSV,axis=0,ignore_index=True,sort=True)
dt['Label'] = dt['Label'].replace('Négative', 'Negative')

import spacy
nlp = spacy.load('fr_core_news_sm')

listNLP = []
txt = ""

# "Avons visité le château en famille. Tout ce que vous voyez de l'extérieur est tout ce que vous verrez de l'intérieur. Alors pourquoi acheter une entrée :"

import re
# comment = dt1['Comments'][0]
# if True:
#for comment in (dt1['Comments'].iloc[:100]):
for comment in dt['Comments']:
    #print(comment)
    #print('===============================')
    comment = comment.lower()
    # TODO: enlever non word
    # "avons visité le château en famille tout ce que vous voyez de l'extérieur est tout ce que vous verrez de l'intérieur alors pourquoi acheter une entrée"
    comment = re.sub(r"[\#\$%\&'\*\+\-\.\^_`\|\~:\(\)\!,\[\]]", '', comment)
    comment = re.sub(r"\s[a-z]\s", ' ', comment)
    comment = re.sub(r"\s+", ' ', comment)
    #print(comment)
    #print('===============================')
    commentNLP = nlp(comment)

    tokens = [token.text for token in commentNLP if not token.is_stop or token.is_space or token.is_punct]
    # tokens = [avons, visité, château, famille, tout, voyez, extérieur, est, tout, ce, que, vous, verrez, intérieur, alors, pourquoi, acheter, entrée]
    #print(tokens)
    #print('===============================')
    listNLP.append(tokens)

# tokens = "avons visité, château, famille, tout, voyez, extérieur, est, tout, ce, que, vous, verrez, intérieur, alors, pourquoi, acheter, entrée]
listCommentNLP = []
for tokens in listNLP:
    txt = ""
    for token in tokens:
        txt += ' ' + token
    listCommentNLP.append(txt)
# print(listCommentNLP)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

vectorizer = TfidfVectorizer(max_features=5000)
tfidf = vectorizer.fit_transform(listCommentNLP)

print(vectorizer.get_feature_names())
print(tfidf.shape)

import pickle
pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))


# SPLIT Train/Test
X_train, X_test, y_train, y_test = train_test_split(tfidf, dt['Label'], test_size=0.2, random_state=42)

classifier = MultinomialNB()
classifier.fit(X_train,y_train)
# print(classifier.feature_count_)
y_pred = classifier.predict(X_test) 

from sklearn.metrics import classification_report, accuracy_score
print(classification_report(y_test,y_pred)) 
print(accuracy_score(y_test, y_pred))

# Saving Model
from sklearn.externals import joblib
joblib.dump(classifier, 'NLP_model.pkl')
