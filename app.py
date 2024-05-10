from flask import Flask,render_template,request
import pypyodbc as odbc
app = Flask(__name__)
@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        roll = request.form.get('roll')
        year = request.form.get('year')
        connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:nuthanserver.database.windows.net,1433;Database=StudentDetails;Uid=CloudSA9645e9f0;Pwd=Nuthan@8106;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute(f"insert into dbo.test1 values(?,?)",(roll,name))
        print(cursor.rowcount)
        conn.commit()
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
