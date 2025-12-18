from flask import Flask,render_template, url_for
app= Flask(__name__)
@app.route('/')
def home():

    return render_template('index.html')
@app.route('/Length')
def Length():
    return "length"

@app.route('/ Weight')
def  Weight():
    return " Weight"

@app.route('/Temperature')
def Temperature():
    return "temperature"

    

if __name__== '__main__':
    app.run(debug=True)