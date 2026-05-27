import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index

# Connect to your development database


@app.route('/', methods=['GET'])
def get_index():
    # Use the template's helper function to get the connection
    connection = get_flask_database_connection(app)
    
    # Use that connection variable to run your query
    rows = connection.execute("SELECT * FROM tech_terms;")
    
    # Pass those rows directly into your HTML template
    return render_template('index.html', terms=rows)

@app.route('/add-term', methods=['POST'])
def add_term():
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
    return redirect(url_for('get_index'))

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



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
