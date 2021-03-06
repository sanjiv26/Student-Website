#!C:/Users/---Your name------/AppData/Local/Programs/Python/Python39/python.exe


print("Content-type: text/html\n")

#html and css for admin page
print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
    <style>
    #body css
        body{
    margin:0;
    padding:0;
}
.header{
    padding:50px;
    background-color: lightskyblue;
    color:white;
    text-align: center;
    font-family: Verdana,Tahoma, sans-serif;
    margin-top: -5%;
}

.Sidenav{
    height: 100%;
    width: 0;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: lightsteelblue;
    overflow-x: hidden;
    transition: 0.5s;
    padding-top: 60px;
}
.Sidenav a, .dropdown-btn{
    padding: 8px 8px 8px 32px;
    text-decoration: none;
    font-size: 25px;
    color:white;
    display: block;
    border: none;
    background: none;
    transition: 0.3s;
    outline: none;
}

.Sidenav a:hover, .dropdown-btn:hover {
    color: black;
}
.active {
    color: white;
  }
.dropdown-container {
    display: none;
    background-color: lightsteelblue;
    padding-left: 8px;
}
.fa-caret-down {
    float: right;
    padding-right: 30px;
  }
.Sidenav .close{
    position: absolute;
    top: 0;
    right: 25px;
    font-size: 36px;
    margin-left: 50px;
}
.content {
    transition: margin-left .5s;
    margin-top: 30px;
    font-size: larger;
    color: black;
  }
  
@media screen and (max-height: 450px) {
    .Sidenav {padding-top: 15px;}
    .Sidenav a {font-size: 18px;}
  }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>
    <div id="Sidenav" class="Sidenav">
        <a href="javascript:void(0)" class="close" onclick="closeNav()">&times;</a>
        <a href="#admin">Admin</a>
        <a href="mainpage.py">Home</a>
        <button class="dropdown-btn">Students<i class="fa fa-caret-down"></i>
          </button>
          <div class="dropdown-container">
            <a href="adminnewstudent.py">New</a>
            <a href="adminstudentdetails.py">Existing</a>
          </div>
          <a href="#logout">Logout</a>
    </div>

    <div class="content">
        <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776;</span>
        <div class="header">
            <h1>Global College of Education</h1>
        </div>
    </div>
#javascirpt
    <script>
        function openNav() {
          document.getElementById("Sidenav").style.width = "250px";
          document.getElementById("content").style.marginLeft = "250px";
        }
        
        function closeNav() {
          document.getElementById("Sidenav").style.width = "0";
          document.getElementById("content").style.marginLeft= "0";
        }
        var dropdown = document.getElementsByClassName("dropdown-btn");
        var i;

        for (i = 0; i < dropdown.length; i++) {
        dropdown[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
        } else {
        dropdownContent.style.display = "block";
        }
        });
    }
    </script>
</body>
</html>
""")
