from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- Route for the main portfolio page ---
@app.route('/')
def home():
    """
    Renders the main portfolio page (index.html).
    
    In a more complex app, you might pass dynamic data here,
    like fetching project details from a database.
    """
    # For now, we'll keep the project data static within the template,
    # but you could define it here like this:
    projects = [
        {
            'title': 'E-commerce Analytics Dashboard',
            'description': 'A web-based dashboard using Flask and Plotly to visualize sales data and user behavior for an e-commerce platform.',
            'tags': ['Python', 'Flask', 'Plotly', 'Pandas']
        },
        {
            'title': 'Machine Learning Model API',
            'description': 'A RESTful API built with Flask-RESTful to serve predictions from a trained sentiment analysis model.',
            'tags': ['Python', 'Flask-RESTful', 'Scikit-learn']
        },
        {
            'title': 'Personal Blog Platform',
            'description': 'A simple, dynamic blog created with Flask and SQLAlchemy, featuring post creation, editing, and user comments.',
            'tags': ['Flask', 'SQLAlchemy', 'Jinja2']
        }
    ]
    return render_template('index.html', projects=projects)

# --- Main execution point ---
if __name__ == '__main__':
    # Runs the Flask app. 
    # debug=True will auto-reload the server when you make changes.
    app.run(debug=True)
