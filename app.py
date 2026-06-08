import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
@app.route('/', methods=['GET'])
def get_index():
    # Use the template's helper function to get the connection
    connection = get_flask_database_connection(app)
    
    # Use that connection variable to run your query
    rows = connection.execute("SELECT * FROM tech_terms;")
    
    # Pass those rows directly into your HTML template
    return render_template('index.html', terms=rows)


@app.route('/add', methods=['GET', 'POST'])
def add_term():
    # Check if the user is submitting the form
    if request.method == 'POST':
        # 1. Grab the raw text typed into the form inputs
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
        
        # Bounce back to the index dashboard once saved
        return redirect(url_for('get_index'))
    
    # If request.method is 'GET' (they just clicked the link), show the form page
    return render_template('add.html')


@app.route('/term/<int:term_id>', methods=['GET'])
def get_single_term(term_id):
    connection = get_flask_database_connection(app)
    
    # Selecting everything handles pulling our new deep_dive column
    query = "SELECT * FROM tech_terms WHERE id = %s;"
    result = connection.execute(query, [term_id])
    
    if not result:
        return "Flashcard not found!", 404
        
    single_term = result[0]
    return render_template('show.html', term=single_term)


# 1. GET Route: Renders the edit form pre-filled with database values
@app.route('/term/<int:term_id>/edit', methods=['GET'])
def edit_single_term(term_id):
    connection = get_flask_database_connection(app)
    query = "SELECT * FROM tech_terms WHERE id = %s;"
    result = connection.execute(query, [term_id])
    
    if not result:
        return "Flashcard not found!", 404
        
    return render_template('edit.html', term=result[0])


# 2. POST Route: Takes the updated text and executes an UPDATE SQL command
@app.route('/term/<int:term_id>/update', methods=['POST'])
def update_single_term(term_id):
    topic = request.form.get('topic')
    concept_name = request.form.get('concept_name')
    analogy = request.form.get('analogy')
    key_notes = request.form.get('key_notes')
    deep_dive = request.form.get('deep_dive')
    
    connection = get_flask_database_connection(app)
    
    # Secure SQL update using parameterized placeholders
    query = """
        UPDATE tech_terms 
        SET topic = %s, concept_name = %s, analogy = %s, key_notes = %s, deep_dive = %s
        WHERE id = %s;
    """
    connection.execute(query, [topic, concept_name, analogy, key_notes, deep_dive, term_id])
    
    # Redirect straight back to the single term view to see the updates!
    return redirect(url_for('get_single_term', term_id=term_id))

if __name__ == '__main__':
    app.run(debug=True, port=5001)