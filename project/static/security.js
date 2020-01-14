// Verify that passwords match

let passwd = document.getElementById("pswd")
let confirmPasswd = document.getElementById("confirm-pswd")
let errMsg = document.getElementById("error-message")

function onPasswordInput(event) {
    if (passwd.value !== confirmPasswd.value) {
        event.target.classList.add("invalid")
        error()
    } else {
        passwd.classList.remove("invalid")
        confirmPasswd.classList.remove("invalid")
        noError()
    }
}

function error() {
    passwd.style.background = "#fef0f0"
    passwd.style.borderColor = "#de071c"
    confirmPasswd.style.background = "#fef0f0"
    confirmPasswd.style.borderColor = "#de071c"
    errMsg.style.display = "block"
}

function noError() {
    passwd.style.background = "#fff"
    passwd.style.borderColor = "#d6d6d6"
    confirmPasswd.style.background = "#fff"
    confirmPasswd.style.borderColor = "#d6d6d6"
    errMsg.style.display = "none"
}

passwd.addEventListener("focusout", () => {
    passwd.addEventListener("keyup", onPasswordInput)
})

confirmPasswd.addEventListener("keyup", onPasswordInput)

// Minimum password length

function passwordLength(event) {
    if (passwd.value.length < 8) {
        event.target.classList.add("invalid")
        document.getElementById("short-password").style.display = "block"
    } else {
        passwd.classList.remove("invalid")
        errMsg.style.display = "none"
    }
}

// Check if all fields are filled

function validate() {
}
