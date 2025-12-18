from flask import Flask,render_template, url_for
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Length')
def Length():
    return render_template('Length.html')

@app.route('/Weight')
def  Weight():
    return render_template('weght.html')

@app.route('/Temperature')
def Temperature():
    return render_template('tem.html')
 

if __name__== '__main__':
    app.run(debug=True)