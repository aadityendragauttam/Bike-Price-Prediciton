from flask import Flask,url_for,request , render_template
app = Flask(__name__)
@app.route('/')             # / == homeroute
# def home():
#     return 'hello hii kese ho'
# @app.route('/bio')
# def intro():
#     return 'My name is Aadityendra'
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/project')
def project():
    return render_template('project.html')
@app.route('/history')
def history():
    return render_template('history.html')
if __name__ == '__main__':
    app.run(debug=True)