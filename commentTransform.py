
def commentTransform(comment):

    import spacy
    nlp = spacy.load('fr_core_news_sm')
    #print(comment)
    #print('===============================')
    comment = comment.lower()
    # TODO: enlever non word
    # "avons visité le château en famille tout ce que vous voyez de l'extérieur est tout ce que vous verrez de l'intérieur alors pourquoi acheter une entrée"
    import re
    comment = re.sub(r"[\#\$%\&'\*\+\-\.\^_`\|\~:\(\)\!,\[\]]", '', comment)
    comment = re.sub(r"\s[a-z]\s", ' ', comment)
    comment = re.sub(r"\s+", ' ', comment)
    #print(comment)
    #print('===============================')
    commentNLP = nlp(comment)

    tokens = [token.text for token in commentNLP if not token.is_stop or token.is_space or token.is_punct]

    # return tokens
    # tokens = [avons, visité, château, famille, tout, voyez, extérieur, est, tout, ce, que, vous, verrez, intérieur, alors, pourquoi, acheter, entrée]
    #print(tokens)
    #print('===============================')

    # tokens = "avons visité, château, famille, tout, voyez, extérieur, est, tout, ce, que, vous, verrez, intérieur, alors, pourquoi, acheter, entrée]
    commentTranform = ""
    for token in tokens:
        commentTranform += ' ' + token

    return commentTranform