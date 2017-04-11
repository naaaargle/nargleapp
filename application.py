from flask import Flask, render_template

application = Flask(__name__)
# Make AWS happy - it is configured to look for the `application` variable when deploying.
app = application

# You can set these routes to be any string you want - even an emoji1
@app.route('/')
def home():
    # Flask knows to look in the /templates/ folder for the html file specified
    # in render_template
    return render_template('home.html')


@app.route('/fordham')
def fordham():
    return render_template('fordham.html')


@app.route('/mary-page')
def mary_page():
    return render_template('mary_new.html')

# Python assigns the name "__main__" to a script when it is executed. Since this file
# is the one doing the executing, it retains the name "__main__" rather than inheriting
# the name of the file it lives in (e.g. filename.py).
if __name__ == '__main__':
    # Setting debug to True will give you more informative tracebacks when there's an
    # error in your app. Not recommended for production if your website will be
    # consumer-facing.
    app.run(debug=True)
