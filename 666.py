from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class DataCollectionForm(FlaskForm):
    grades = StringField('Grades Obtained in Each Course', validators=[DataRequired()])
    feedback = StringField('How do you feel about the classes and teachers of the course?', validators=[DataRequired()])
    ability = StringField('What ability do you improve when you study in GIC?', validators=[DataRequired()])
    suggestions = StringField('Do you have any suggestions to GIC?', validators=[DataRequired()])
    improvement = SelectField('Which part do you think GIC can improve?', choices=[('classes', 'Classes quality'), ('services', 'College services'), ('events', 'GIC social events')], validators=[DataRequired()])

@app.route('/')
def welcome():
    return render_template('FC724 assignment 1 Welcome Page.html')

@app.route('/information')
def information():
    return render_template('FC724 assignment 1 Information Page.html')

@app.route('/data_collection', methods=['GET', 'POST'])
def data_collection():
    form = DataCollectionForm()
    if form.validate_on_submit():
        # Process the form data here
        grades = form.grades.data
        feedback = form.feedback.data
        ability = form.ability.data
        suggestions = form.suggestions.data
        improvement = form.improvement.data

        # Perform data processing or save to database here

        return "Form submitted successfully!"
    return render_template('FC724 assignment 1 Data Collection Page.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)