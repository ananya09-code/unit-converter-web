from flask import Flask,render_template, url_for,request
from converter.weght import convert_len
from converter.length import convert_met
from converter.tem import convert_tem
app= Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Length', methods =['GET','POST'])
def Length():
    if request.method=='POST':
        ask_met=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return convert_met(float(ask_met),from_unit,to_unit)
    else:
        return render_template('Length.html')

@app.route('/Weight', methods =['GET','POST'])
def  Weight():
    if request.method=='POST':
        ask_len=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return convert_len(float(ask_len),to_unit,from_unit)
    else:
       return render_template('weght.html')

@app.route('/Temperature',methods =['GET','POST'])
def Temperature():
    if request.method=='POST':
        ask_tem=request.form['value']
        from_unit=request.form['from_unit']
        to_unit=request.form['to_unit']
        return convert_tem(float(ask_tem),from_unit,to_unit)
    else:
      return render_template('tem.html')
 

if __name__== '__main__':
    app.run(debug=True)