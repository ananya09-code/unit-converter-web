from flask import Flask,render_template, url_for,request
from converter.length import convert_len
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Length', methods =['GET','POST'])
def Length():
    if request.method=='POST':
        global ask_len,from_unit,to_unit
        ask_len=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return convert_len(ask_len,to_unit,from_unit)
    else:
        return render_template('Length.html')

@app.route('/Weight', methods =['GET','POST'])
def  Weight():
    if request.method=='POST':
        global ask_weight,from_unit,to_unit
        ask_weight=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return f'{ask_weight} {from_unit} {to_unit} this is asked'
    else:
       return render_template('weght.html')

@app.route('/Temperature',methods =['GET','POST'])
def Temperature():
    if request.method=='POST':
        global ask_tem,from_unit,to_unit
        ask_tem=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return f'{ask_tem} {from_unit} {to_unit} this is asked'
    else:
      return render_template('tem.html')
 

if __name__== '__main__':
    app.run(debug=True)