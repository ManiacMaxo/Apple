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

// let isDarkMode = false

// function darkMode() {
//     const backdrop = document.getElementById("body").style.background
//     if (isDarkMode) {
//         isDarkMode = true
//         backdrop = "#313131"
//     } else {
//         isDarkMode = false
//         backdrop = "#fafafa"
//     }
// }
