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

let isDarkMode = false

function darkMode() {
    const backdrop = document.getElementById("body").style.background
    if (isDarkMode) {
        isDarkMode = true
        backdrop = "#313131"
    } else {
        isDarkMode = false
        backdrop = "#fafafa"
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

// check passwords

const passwd = document.getElementsByName("password")
const confirmPasswd = document.getElementById("confirm-password")
const errMsg = document.getElementById("error-message")

function onPaswordInput(event) {
    if (passwd.value !== confirmPasswd.value) {
        event.target.classList.add("invalid")
        errMsg.style.display = "block"
    } else {
        passwd.classList.remove("invalid")
        confirmPasswd.classList.remove("invalid")
        errMsg.style.display = "none"
    }
}

passwd.addEventListener("focusout", () => {
    passwd.addEventListener("keyup", onPaswordInput)
})

confirmPasswd.addEventListener("keyup", onPaswordInput)

function moreInfo() {
    document.getElementById("list-info-modal").style.display = "block"
}
