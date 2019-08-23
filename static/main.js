
var username = ""

function save_username(){
    username = $("#name").val();
    localStorage.setItem("username", username);
}

function get_username(){
    return username;
}