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

function openLogin() {
    closeRegistration()
    document.getElementById("login-modal").style.display = "block"
    document.getElementById("backdrop").style.display = "flex"
}

function closeLogin() {
    document.getElementById("login-modal").style.display = "none"
    document.getElementById("backdrop").style.display = "none"
}

function openRegistration() {
    closeLogin()
    document.getElementById("registration-modal").style.display = "block"
    document.getElementById("backdrop").style.display = "flex"
}

function closeRegistration() {
    document.getElementById("registration-modal").style.display = "none"
    document.getElementById("backdrop").style.display = "none"
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
