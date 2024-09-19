from flask import Flask, render_template
from climate_dashboard import create_dashboard

server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')

# Create the Dash app and attach it to the Flask server
dash_app = create_dashboard(server)

if __name__ == '__main__':
    server.run(debug=True, port=5000)
