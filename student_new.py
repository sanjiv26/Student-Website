#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")

#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
f = cgi.FieldStorage()
id  = f.getvalue("id")

q = """select * from studentdetails where accept = 'New'"""
cur.execute(q)
r = cur.fetchall()
cnt = 0
#updating details
if id != None:
    q1 = """update studentdetails set accept='Verified' where id = '%s'"""%(id)
    cur.execute(q1)
    conn.commit()
#alert after completion
    print("""
        <script>
            alert("Request accepted");
            location.href = "adminstudentdetails.py";
        </script>
    """)
