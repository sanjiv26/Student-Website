#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html \r\n\r\n")

#importing common gateway interface,sql

import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host="localhost",user="root",password="",database="student")
cur = conn.cursor()

#html and css

print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
    #body style
        body{
            background-image: url("wp2140463.jpg");
            background-size: cover;
            text-align: center;
            margin-top: 200px;
            font-size: large;
        }
    #form style
        form{
            display: inline-block;
            border: 5px solid black;
            padding: 20px;
            background-color: lightblue;
        }
    </style>
</head>
<body>
    <h1>ADMINISTRATOR LOGIN</h1>
    #form for admin login
    <form>
        <label for="username">Username:</label><br>
        <input type="text" id="username" name="username" placeholder="Username"><br><br>
        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" placeholder="Password"><br><br>
        <button type="submit" name = "login" value = "login">Login</button>
        <button type="submit"><a href="mainpage.py" style="text-decoration: none;color:black">Cancel</button></a>
    </form>
</body>
</html>
""")

#getting field data from form

f = cgi.FieldStorage()
username = f.getvalue("username")
password = f.getvalue("password")
v = f.getvalue("login")
#selecting the username and password

if v!=None:
    q = """select id from adminlogin where username='%s' and password = '%s'""" %(username,password)
    cur.execute(q)
#fetch the login details

    r = cur.fetchone()
#check and alert if login is successfull

    if r != None:
        print("""
            <script>
                alert("Login successfull")
                location.href = "adminpage.py"
            </script>
        """)
    else:
        print("""
            <script>
                alert("Login error")
                location.href = "adminlogin.py"
            </script>
        """)
