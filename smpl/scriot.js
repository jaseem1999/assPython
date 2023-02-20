 function validate(){
        var name = document.getElementById("name").value;
        var email = document.getElementById("email").value;
        var phone = document.getElementById("phone").value;
        var password = document.getElementById("password").value;
        var error_message = document.getElementById("error_message");
        var text;
        error_message.style.padding = "10px";
        if(name.length < 5){
            document.getElementById("name").style.border = "2px solid red";
            text = "Please Enter valid Name";
            error_message.innerHTML = text;
            return false;
        }
        if(email.indexOf("@") == -1 || email.length < 6){
            document.getElementById("email").style.border = "2px solid red";
            text = "Please Enter valid Email";
            error_message.innerHTML = text;
            return false;
        }
        if(isNaN(phone) || phone.length != 10){
            document.getElementById("phone").style.border = "2px solid red";
            text = "Please Enter valid Phone Number";
            error_message.innerHTML = text;
            return false;
        }
        if(password.length < 6){
            document.getElementById("password").style.border = "2px solid red";
            text = "Please Enter Correct Password";
            error_message.innerHTML = text;
            return false;
        }
        alert("Form Submitted Successfully!");
        return true;
    }