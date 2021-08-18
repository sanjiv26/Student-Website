#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")
#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host="localhost", user="root", password="", database="student")
cur = conn.cursor()
f = cgi.FieldStorage()
sid = f.getvalue("sid")

q = """select * from studentdetails"""

cur.execute(q)
r = cur.fetchall()
count = 0
#hmtl and css
print("""
        <html>
        <head><title>profile</title></head>
        <style>
        table,th,td
        {
            border-collapse:collapse;
            border:3px solid blue;
            padding:30px
        }
        </style>
        <body>
        #table
        <table border = "2" width = "50">
            <tr>
            <th>S.no</th>
            <th>Student-id</th><th>Name</th><th>Gender</th><th>Email</th><th>Contact</th>
            <th>Age</th><th>Address</th><th>Username</th><th>Password</th><th>Profile</th><th>Change</th><th>Remove</th>
            </tr>""")
#table display
for i in r:
    count = count + 1
    print("""
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>        
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td><img src = "picture/%s" width = "50" height = "50"></td>
            <td><a href = "studentchange.py?cid=%s&id=%s">Change</a></td>
            <td><a href = "studentremove.py?rid=%s&id=%s">Remove</a></td>
            </tr>

            """ % (count, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[0], id, i[0], id))
print("""
     </table>
     </body>
     </html>
     """)

conn.close()
