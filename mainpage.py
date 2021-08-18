#!C:/Users/---your name----/AppData/Local/Programs/Python/Python39/python.exe


print("Content-type: text/html\n")

#html and css
print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
    <style>
        .heading{
                padding:50px;
                background-color: lightskyblue;
                color:white;
                text-align: center;
                font-family: Verdana,Tahoma, sans-serif;
        }
        .image img{
            width:1517px;
            height:800px;
            margin-top: -17px;
        }
    </style>
    #linking bootstrap, jquery
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
    <div class="heading">
        <h1>Global College of Education</h1>
    </div>

    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="studentlogin.py"><span class="glyphicon glyphicon-user"></span> Student</a></li>
                <li><a href="adminlogin.py"><span class="glyphicon glyphicon-log-in"></span> Admin</a></li>
            </ul>
        </div>
    </nav>
    <div class="image">
        <img src="1209519.jpg" alt="college photo">
    </div>

</body>
</html>
    
""")
