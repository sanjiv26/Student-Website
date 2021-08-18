#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe


print("Content-type: text/html\n")
#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
q1 = """select max(id) from newstudents"""
cur.execute(q1)
r = cur.fetchone()
#id number auto generate
if r[0]!= None:
    n = r[0]
else:
    n = 0

z = ""
if n < 10:
    z = "000"
elif n<100:
    z = "00"
elif n< 1000:
    z = "0"
else:
    z = ""

stdid = "idstd" + z + str(n+1)
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
            <h1>STUDENT REGISTRATION</h1>
            #form method
            <form method = "post" action = "#" enctype = "multipart/form-data">
                <label for="id">Id:</label><br>""")
print("""
            #details
            <input type="text" name = "stid" id = "stid" value = "%s" readonly><br><br>
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name" placeholder="Name"><br><br>
            <p>Gender:</p>
            <input type="radio" id="male" name="gender" value="male">
            <label for="male">Male</label>
            <input type="radio" id="female" name="gender" value="female">
            <label for="female">Female</label><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" placeholder="Email"><br><br>
            <label for="contact">Contact:</label><br>
            <input type="tel" id="contact" name="contact" placeholder="Contact"><br><br>
            <label for="age">Age:</label><br>
            <input type="text" id="age" name="age" placeholder="Age"><br><br>
            <label for="address">Address:</label><br>
            <input type="text" id="address" name="address" placeholder="Address"><br><br>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" placeholder="Username"><br><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" placeholder="Password"><br><br>
            <label for="photo">Photo:</label><br>
            <input type="file" id="photo" name="photo"><br><br>
            <button type="submit" name = "register" id = "register">Register</button>
            <button type="submit">Cancel</button>
    </form>
</body>
</html>
""" %(stdid))
#getting field data from form
f = cgi.FieldStorage()
sub = f.getvalue("register")
if sub !=None:
    stdid = f.getvalue("stid")
    name = f.getvalue("name")
    gender = f.getvalue("gender")
    email = f.getvalue("email")
    contact = f.getvalue("contact")
    age = f.getvalue("age")
    address = f.getvalue("address")
    username = f.getvalue("username")
    password = f.getvalue("password")
    photo = f['photo']

    if photo != None:
        if photo.filename:
            import os

            fp = os.path.basename(photo.filename)
            open("picture/" + fp, "wb").write(photo.file.read())
            #insert into studentdetails
            q = """insert into studentdetails(stid,name,gender,email,contact,age,address,username,password,photo) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(stdid,name,gender,email,contact,age,address,username,password,fp)
            cur.execute(q)
            conn.commit()
            conn.close()

            #alert when inserted
            print("""
                <script>
                    alert("Data inserted successfully");
                    location.href = "studentlogin.py"
                </script>
            """)
    else:
        print("""
            <script>
                alert("file error");
                location.href = "studentregister.py"
            </script>
        """)

    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    #mail content
    mail_content = """Hello, %s
                            USERNAME : %s,
                            PASSWORD : %s
                    """ % (name, username, password)
    #senders mail address
    sender_address = 'Enter your email'
    sender_pass = 'Enter the Email password'
    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Registration successfull '
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail sent')

