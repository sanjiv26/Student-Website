#!C:/Users/----your name-----/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")
#importing common gateway interface,sql

import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
f = cgi.FieldStorage()
id  = f.getvalue("id")
#getting the value
if len(f) == 2:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
else:
    id = f.getvalue("id")
    cid = f.getvalue("cid")
    stdid = f.getvalue("studentid")
    name = f.getvalue("name")
    email = f.getvalue("email")
    contact = f.getvalue("contact")
    age = f.getvalue("age")
    address = f.getvalue("address")
    username = f.getvalue("username")
    password = f.getvalue("password")
    profile = f['photo']

    if profile.filename:
        import os
        fp = os.path.basename(profile.filename)
        open("picture/" + fp, "wb").write(profile.file.read())
        #updating details
        q1 = """update studentdetails set name = '%s',email = '%s',contact = '%s',age = '%s',address = '%s',username = '%s',password = '%s',photo = '%s' where id = '%s'"""%(name,email,contact,age,address,username,password,fp,cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "adminstudentdetails.py?id=%s";
            </script>
            """%(id))
    else:
        q1 = """update studentdetails set name = '%s',email = '%s',contact = '%s',age = '%s',address = '%s',username = '%s',password = '%s' where id = '%s'"""%(name,email,contact,age,address,username,password,cid)
        cur.execute(q1)
        conn.commit()
        print("""
             <script>
                alert("Profile updated successfully");
                location.href = "adminstudentdetails.py?id=%s";
            </script>
            """%(id))

q = """select * from studentdetails where id = '%s'"""%(cid)
cur.execute(q)
r = cur.fetchone()
#html and css
print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Register</title>
            <style>
                body{
                    background-image: url("photo-1523050854058-8df90110c9f1.jpg");
                    background-size: cover;
                    font-size: large;
                    margin-left: 30px;
                }
                form{
                    display: inline-block;
                    width:250px;
                    border: 5px solid steelblue;
                    padding: 20px;
                    background-color: lightsteelblue;
                }
            </style>
        </head>
        <body>
        #form for details entry
            <h1>STUDENT REGISTRATION</h1>
            <form method = "post" action = "#" enctype = "multipart/form-data">
            <label for="id">Id:</label><br>
            <input type="text" name = "stid" id = "stid" value = "%s" readonly><br><br>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" value = "%s"  placeholder="Name"><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" value = "%s"  placeholder="Email"><br><br>
            <label for="contact">Contact:</label><br>
            <input type="tel" id="contact" name="contact" value = "%s"  placeholder="Contact"><br><br>
            <label for="age">Age:</label><br>
            <input type="text" id="age" name="age" value = "%s"  placeholder="Age"><br><br>
            <label for="address">Address:</label><br>
            <input type="text" id="address" name="address" value = "%s"  placeholder="Address"><br><br>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" value = "%s"  placeholder="Username"><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" value = "%s"  placeholder="Password"><br><br>
            <label for="photo">Photo:</label><br>
            <input type="file" id="photo" value = "%s"  name="photo"><br><br>
            <button type="submit" name = "register" id = "register">Register</button>
            <button type="submit">Cancel</button>
    </form>
</body>
</html>
""" %(r[1],r[2],r[4],r[5],r[6],r[7],r[8],r[9],r[10]))
conn.close()
