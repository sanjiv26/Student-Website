#!C:/Users/---your name---/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")

#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
f = cgi.FieldStorage()
id = f.getvalue("id")

q ="""select * from studentdetails where id = %s"""%(id)

cur.execute(q)
r = cur.fetchone()
#html and css
print("""
<html>
<head>
<style>
#css
*{
background-color:rgb(235, 221, 237)
}
h1{
float:left;
margin-top:300px;
text-transform:uppercase;
font-size:60px;
font-family: 'Girassol', cursive;
}
h1:hover{
text-shadow: 3px 4px 5px red;
}
table{
float:right;
margin-right:100px;
margin-top:80px;
}
table,tr,th,td,b{
background-color:rgb(227, 98, 154);
font-size:20px;
padding:15px;
}
b{
text-transform:uppercase;
}
</style>
</head>
<body>
<h1>Welcome %s</h1>
#table for html
<table>
<tr><td><img src = "picture/%s" width = "100" height = "100"></td></tr>
<tr><td><b>Id</b>: %s</td><tr>
<tr><td><b>Name</b> : %s</td><tr>
<tr><td><b>Gender</b> : %s</td><tr>
<tr><td><b>Email</b> : %s</td><tr>
<tr><td><b>Number</b> : %s</td><tr>
<tr><td><b>Age</b> : %s</td><tr>
<tr><td><b>Address</b> : %s</td><tr>
<tr><td><b>Username</b> : %s</td><tr>
<tr><td><b>Password</b> : %s</td><tr>
</table>
</body>
</html>
""" %(r[2],r[10],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9]))
