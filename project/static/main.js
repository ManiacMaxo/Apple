let isNavShown = false

function nav() {
    const navbar = document.getElementById("sideNav")
    if (isNavShown) {
        isNavShown = false
        navbar.style.transform = "translateX(-250px)"
    } else {
        isNavShown = true
        navbar.style.transform = "translateX(0)"
    }
}

// puts placeholders and sets margins
if(document.getElementsByName("username")[0] !== undefined) {
    document.getElementsByName("username")[0].placeholder = "Username"
}
if(document.getElementsByName("email")[0] !== undefined) {
    document.getElementsByName("email")[0].placeholder = "Email"
}
if(document.getElementsByName("password")[0] !== undefined) {
    document.getElementsByName("password")[0].placeholder = "Password"
}
if(document.getElementsByName("confirm")[0] !== undefined) {
    document.getElementsByName("confirm")[0].placeholder = "Confirm Password"
}
if(document.getElementsByName("title")[0] !== undefined) {
    document.getElementsByName("title")[0].placeholder = "Title"
    document.getElementsByName("title")[0].style.marginTop = "15px"
    document.getElementsByName("title")[0].style.marginBottom = "15px"
}
if(document.getElementsByName("deadline")[0] !== undefined) {
    document.getElementsByName("deadline")[0].placeholder = "Deadline"
    document.getElementsByName("deadline")[0].style.marginTop = "15px"
    document.getElementsByName("deadline")[0].style.marginBottom = "15px"
}
if(document.getElementsByName("description")[0] !== undefined) {
    document.getElementsByName("description")[0].placeholder = "Description"
    document.getElementsByName("description")[0].style.marginTop = "15px"
    document.getElementsByName("description")[0].style.marginBottom = "15px"
}