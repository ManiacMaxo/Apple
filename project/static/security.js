// Verify that passwords match

let passwd = document.getElementById("pswd")
let confirmPasswd = document.getElementById("confirm-pswd")
let errMsg = document.getElementById("error-message")
let passLen = document.getElementById("short-password")

let typingTimer //timer identifier
let doneTypingInterval = 2000 //time in ms

confirmPasswd.addEventListener("keyup", () => {
    clearTimeout(typingTimer)
    if (confirmPasswd.value) {
        typingTimer = setTimeout(doneTyping, doneTypingInterval)
    }
})

function doneTyping() {
    if (passwd.value !== confirmPasswd.value) {
        event.target.classList.add("invalid")
        error(errMsg)
    } else {
        passwd.classList.remove("invalid")
        confirmPasswd.classList.remove("invalid")
        noError(errMsg)
    }
}

// function onPasswordInput(event) {
//     if (passwd.value !== confirmPasswd.value) {
//         event.target.classList.add("invalid")
//         error()
//     } else {
//         passwd.classList.remove("invalid")
//         confirmPasswd.classList.remove("invalid")
//         noError()
//     }
// }

// passwd.addEventListener("focusout", () => {
//     passwd.addEventListener("keyup", () => {
//         setTimeout(onPasswordInput, 1000)
//     })
// })

// confirmPasswd.addEventListener("keyup", onPasswordInput)

function error(err) {
    passwd.style.background = "#fef0f0"
    passwd.style.borderColor = "#de071c"
    confirmPasswd.style.background = "#fef0f0"
    confirmPasswd.style.borderColor = "#de071c"
    err.style.display = "block"
    document.getElementById("button").disabled = true
}

function noError(err) {
    passwd.style.background = "#fff"
    passwd.style.borderColor = "#d6d6d6"
    confirmPasswd.style.background = "#fff"
    confirmPasswd.style.borderColor = "#d6d6d6"
    err.style.display = "none"
    document.getElementById("button").disabled = false
}

// Minimum password length

function passwordLength(event) {
    if (passwd.value.length < 8) {
        event.target.classList.add("invalid")
        error(passLen)
    } else {
        passwd.classList.remove("invalid")
        noError(passLen)
    }
}

// Check if all fields are filled

function validate() {}
