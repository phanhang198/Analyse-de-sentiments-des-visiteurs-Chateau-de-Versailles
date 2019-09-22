from sklearn.externals import joblib

#Loading the saved model with joblib
model = joblib.load('NLP_model1.pkl')

# New data to predict
comment_test = "Le chateau a trop de monde, le prix est cher et la queue est horriblement longue"

from commentTransform import commentTransform

X = commentTransform(comment_test)
# apply the whole pipeline to data
# pred = model.predict(comment_test)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# vectorizer = TfidfVectorizer(max_features=50000)
# X_pred = vectorizer.fit_transform([X])

# X_train, X_test, y_train, y_test = train_test_split(X_pred, ['Positive'], test_size=0.0, random_state=42)

import pickle
with open(r"vectorizer1.pickle", "rb") as input_file:
   vectorizer = pickle.load(input_file)

X_pred = vectorizer.transform([X])

print(vectorizer.get_feature_names())
print(X_pred.shape)

# print(X_pred[0])
pred = model.predict(X_pred)
print (pred)