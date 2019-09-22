from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from sqlalchemy import create_engine, MetaData

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# * ===========================================
# TODO: Connect to the database
engine = create_engine('mysql://root:giun0812@localhost/nlp?charset=utf8mb4')
META_DATA = MetaData(bind=engine, reflect=True)
AVIS_TABLE = META_DATA.tables['avis']

listeChateaux = ['Versailles', 'Fontainebleau', 'VauxVicomte', 'Vaux-le-Vicomte', 'Amboise', 'Azay_le_Rideau', 'Chambord', 'Chantilly', 'Chenonceau', 'Cheverny', 'Villandry', 'Usse', 'Beynac', 'Blois', 'Koenigsbourg', 'Bretagne', 'Pierrefonds', 'Angers', 'Castelnaud', 'Murol']

# * ===========================================
# TODO: Loading the saved model with joblib
from sklearn.externals import joblib
model = joblib.load('NLP_model.pkl')
# TODO: Load vectorizer
import pickle
with open(r"vectorizer.pickle", "rb") as input_file:
    vectorizer = pickle.load(input_file)

class ReusableForm(Form):
    avis = TextField('Avis:', validators=[validators.required()])
    
    @app.route("/", methods=['GET', 'POST'])
    def home():
        form = ReusableForm(request.form)
        
        print(form.errors)
        if request.method == 'POST':
            avis=request.form['avis']
            chateau=request.form['chateau']
            label=request.form['label']
        
        if form.validate():
        # Save the comment here.
            if chateau == 'None':
                flash('Error: Merci de choisir un château. ')
            else:
                flash('Vous avez donné avis pour le chateau ' + chateau + ': '+ avis + ' (' + label + ')')
                engine.execute(AVIS_TABLE.insert(), Chateau=chateau, Comments=avis, Label=label)
        else:
            flash('Error: All the form fields are required. ')
        
        return render_template('avis.html', form=form, chateaux=listeChateaux, avis='')
    
    @app.route('/check', methods=['GET', 'POST'])
    def check():
        form = ReusableForm(request.form)
        
        print(form.errors)
        if request.method == 'POST':
            avis=request.form['avis']
        
        from commentCheck import commentCheck
        if form.validate():
        # Save the comment here.
            print(avis)
            if avis == '':
                flash('Error: Merci de rédiger 1 avis ')
            else:
                result = commentCheck(avis, vectorizer, model)
                flash('Vous avez donné avis : "' + avis + '"  (' + result[0] + ')')
        else:
            flash('Error: All the form fields are required. ')
        return render_template('check.html', form=form)

if __name__ == "__main__":
    app.run()