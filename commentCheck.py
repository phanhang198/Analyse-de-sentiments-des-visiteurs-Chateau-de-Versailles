# -*- coding: utf-8 -*-

def commentCheck(comment, vectorizer, model):
    # New data to predict
    from commentTransform import commentTransform
    X = commentTransform(comment)
    X_pred = vectorizer.transform([X])
    pred = model.predict(X_pred)
    return pred