from flask import Flask,render_template,request
import pandas as pd
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    global details
    details = {'Name' : [],'Roll no' : [],'year' : []} 
    if request.method == "POST":
        details['Name'].append(request.form.get('name'))
        details['Roll no'].append(request.form.get('roll'))
        details['year'].append(request.form.get('year'))
        print(details)
        return render_template('index.html')
    return render_template('index.html')
app.run(debug=True)
    