#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")
#importing common gateway interface,sql

import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
#getting field data from form
f = cgi.FieldStorage()
id = f.getvalue("id")
rid = f.getvalue("rid")
#delete student details
q = """delete from studentdetails where id = '%s'"""%(rid)
cur.execute(q)
conn.commit()
#alert when removed
print("""
    <script>
        alert("Remove successfully")
        location.href = "adminstudentdetails.py?id = %s";
    </script>"""%(id))

conn.close()
