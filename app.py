import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
import random

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
@app.route('/', methods=['GET'])
def get_index():
    # Use the template's helper function to get the connection
    connection = get_flask_database_connection(app)
    rows = connection.execute("SELECT * FROM tech_terms;")
    return render_template('index.html', terms=rows)


@app.route('/add', methods=['GET', 'POST'])
def add_term():
   
    if request.method == 'POST':
        
        topic = request.form.get('topic')
        concept_name = request.form.get('concept_name')
        analogy = request.form.get('analogy')
        key_notes = request.form.get('key_notes')
        deep_dive = request.form.get('deep_dive')
        
        connection = get_flask_database_connection(app)
        
        query = """
            INSERT INTO tech_terms (topic, concept_name, analogy, key_notes, deep_dive)
            VALUES (%s, %s, %s, %s, %s);
        """
        connection.execute(query, [topic, concept_name, analogy, key_notes, deep_dive])
        return redirect(url_for('get_index'))
    return render_template('add.html')


@app.route('/term/<int:term_id>', methods=['GET'])
def get_single_term(term_id):
    connection = get_flask_database_connection(app)
    query = "SELECT * FROM tech_terms WHERE id = %s;"
    result = connection.execute(query, [term_id])
    
    if not result:
        return "Flashcard not found!", 404
        
    single_term = result[0]
    return render_template('show.html', term=single_term)

@app.route('/term/<int:term_id>/edit', methods=['GET'])
def edit_single_term(term_id):
    connection = get_flask_database_connection(app)
    query = "SELECT * FROM tech_terms WHERE id = %s;"
    result = connection.execute(query, [term_id])
    
    if not result:
        return "Flashcard not found!", 404
        
    return render_template('edit.html', term=result[0])


@app.route('/term/<int:term_id>/update', methods=['POST'])
def update_single_term(term_id):
    topic = request.form.get('topic')
    concept_name = request.form.get('concept_name')
    analogy = request.form.get('analogy')
    key_notes = request.form.get('key_notes')
    deep_dive = request.form.get('deep_dive')
    
    connection = get_flask_database_connection(app)
    query = """
        UPDATE tech_terms 
        SET topic = %s, concept_name = %s, analogy = %s, key_notes = %s, deep_dive = %s
        WHERE id = %s;
    """
    connection.execute(query, [topic, concept_name, analogy, key_notes, deep_dive, term_id])
    return redirect(url_for('get_single_term', term_id=term_id))







if __name__ == '__main__':
    app.run(debug=True, port=5001)