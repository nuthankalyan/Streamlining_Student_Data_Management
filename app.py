from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        # from azure_connect import cursor,conn
        roll = request.form.get('roll')
        name = request.form.get('name')
        gender = request.form.get('gender')
        email = request.form.get('email')
        phone = request.form.get('phone')
        mother = request.form.get('mother')
        father = request.form.get('father')
        branch = request.form.get('branch')
        yearofstudy = request.form.get('yearofstudy')
        yearofgrad = request.form.get('yearofgraduation')
        caste = request.form.get('caste')
        # cursor.execute(f"insert into dbo.test1 values(?,?)",(roll,name))
        # conn.commit()
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
