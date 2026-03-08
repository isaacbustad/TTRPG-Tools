# Import necessary modules for creating a Flask web application
from flask import Flask, render_template

# Import route handlers from the pathfinder2e_pages module
from pathfinder2e_pages import pathfinder2e_pages_bp
from death_slayers_pages import death_slayers_bp

# Create an instance of the Flask class to set up the application
app = Flask(__name__)

# Register the blueprint with the main app instance
app.register_blueprint(pathfinder2e_pages_bp)
app.register_blueprint(death_slayers_bp)

# Define a route for the root URL, linked to the index function
@app.route('/')
def index():
    # Render and return the 'index.html' template when this route is accessed
    return render_template('index.html')





# Check if the script is executed as the main program, then run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)