// ---a function to save the username in local storage and retrieve to display in leaderboard--->
var username = ""

function save_username(){
    username = $("#name").val();
    localStorage.setItem("username", username);
}

function get_username(){
    return username;
}

