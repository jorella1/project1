

const button = document.getElementById("loginButton")

button.addEventListener("click", login)

function login(){
    let userName = document.getElementById("username").value
    let password = document.getElementById("password").value
    let login_info = {userName,password}

    json_body = JSON.stringify(login_info)

    $.ajax({
        url:"/login",
        type:"POST",
        contentType:"application/json",
        data: JSON.stringify(s)
    });
}