from flask import Flask, render_template

app = Flask(__name__)

# Default route
@app.route('/')
def home():
    return "Hello CPS3500!"

# New page route
@app.route('/new_page')
def new_page():
    return "This is a New Page!"

# Route with variable username
@app.route('/user/<username>')
def user_page(username):
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
