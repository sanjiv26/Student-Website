#!C:/Users/---your name---/AppData/Local/Programs/Python/Python39/python.exe
print("Content-type: text/html\n")
#importing common gateway interface,sql
import cgi,pymysql,cgitb;cgitb.enable()
#html and css
print("""
<html>
<head>
<title>Forget Password</title>
</head>
<body>
<center>
<h3>Forget Password</h3>
#form
    <form method = "post" action = "#">
        Username:
        <input type = "text" name = "username"><br><br>
        <input type = "submit" value = "OK" name = "submit"> <input type ="button" value ="cancel" onclick = "location.href = 'studentlogin.py'">
        </form>
        </center>
        </body>
        </html>""")

conn = pymysql.connect(host = "localhost",user="root",password = "",database="student")
cur = conn.cursor()
#getting field data from form
f = cgi.FieldStorage()
username = f.getvalue("username")
v = f.getvalue("submit")
#email verification for forgetpass
if v != None:
    q = """select password ,email from studentdetails where username = '%s'"""%(username)
    cur.execute(q)
    r = cur.fetchone()

    if r[0] != None:
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        # importing email
        sender_address = 'Enter your email'
        sender_pass = 'Enter the email password'
        to_address = r[1]
        # message in mail
        msg = """
            hi Welcome %s,
                password : %s
            """%(username,r[0])
        # receiver address
        receiver_address = to_address
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'New Password'
        message.attach(MIMEText(msg, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address,sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        # mail condition ends here and alert is displayed
        print('Mail sent')
        print("""
            <script>
            alert("Please check your mail");
            </script>
            """)
