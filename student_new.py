#!C:/Users/---your name---/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")

#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
#getting field data from form
f = cgi.FieldStorage()
sid = f.getvalue("sid")
q ="""select * from newstudents where accept='new'"""
cur.execute(q)
r = cur.fetchall()
if sid!=None:
    q1="""update studentdetails set accept='Verified' where id=%s"""%(sid)
    cur.execute(q1)
    conn.commit()
    #alert when accepted
    print("""
        <script>
          alert("Request accepted");
          location.href="adminstudentdetails.py";
          </script>
         """)

conn.close()
