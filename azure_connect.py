import pypyodbc as odbc
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:nuthanserver.database.windows.net,1433;Database=StudentDetails;Uid=CloudSA9645e9f0;Pwd=Nuthan@8106;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)