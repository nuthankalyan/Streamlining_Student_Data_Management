from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        from azure_connect import cursor,conn
        name = request.form.get('name')
        roll = request.form.get('roll')
        year = request.form.get('year')
        cursor.execute(f"insert into dbo.test1 values(?,?)",(roll,name))
        print(cursor.rowcount)
        conn.commit()
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
