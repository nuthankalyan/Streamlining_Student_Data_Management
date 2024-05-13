from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        import pyodbc as odbc
        connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:nuthanserver.database.windows.net,1433;Database=StudentDetails;Uid=CloudSA9645e9f0;Pwd=Nuthan@8106;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        roll = request.form.get('rollno')
        name = request.form.get('name')
        gender = request.form.get('gender')
        email = request.form.get('email')
        phone = request.form.get('phone')
        mother = request.form.get('mothername')
        father = request.form.get('fathername')
        branch = request.form.get('branch')
        yearofstudy = request.form.get('yearofstudy')
        yearofgrad = request.form.get('gradyear')
        caste = request.form.get('caste')
        cursor.execute(f"insert into dbo.Student values(?,?,?,?,?,?,?,?,?,?,?)",(roll,name,gender,email,phone,mother,father,yearofstudy,yearofgrad,caste,branch))
        conn.commit()
        print(roll,name,gender,email,phone,mother,father,branch,yearofstudy,yearofgrad,caste)
        return render_template('first.html')
    return render_template('first.html')

if __name__ == '__main__':
    app.run(debug=True)
