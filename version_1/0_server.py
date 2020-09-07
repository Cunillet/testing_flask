from flask import Flask, render_template

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    function to respond to a browser URL:
    localhost:5000/

    :return:    the rendered template 'home.html'
    """

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    