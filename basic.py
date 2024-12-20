from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# @app.route('/signup_form')
# def signup_form():
#     return render_template("signup.html")

@app.route('/thank_u')
def thank_u():
    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')

    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()

    # Check if all are True.
    report = lower_letter and upper_letter and num_end

    return render_template('report.html',report=report,
                           lower=lower_letter,upper=upper_letter,
                           num_end=num_end)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == '__main__':
    app.run(debug = True)