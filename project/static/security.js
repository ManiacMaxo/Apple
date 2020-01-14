// Sign in with Google

function onSignIn(googleUser) {
    // Useful data for your client-side scripts:
    var profile = googleUser.getBasicProfile()
    console.log("ID: " + profile.getId()) // Don't send this directly to your server!
    console.log("Full Name: " + profile.getName())
    console.log("Given Name: " + profile.getGivenName())
    console.log("Family Name: " + profile.getFamilyName())
    console.log("Image URL: " + profile.getImageUrl())
    console.log("Email: " + profile.getEmail())

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token
    console.log("ID Token: " + id_token)
}

// Verify that passwords match

let passwd = document.getElementById("password")
let confirmPasswd = document.getElementById("confirm-password")
let errMsg = document.getElementById("error-message")

function onPasswordInput(event) {
    if (passwd.value !== confirmPasswd.value) {
        event.target.classList.add("invalid")
        errMsg.style.display = "block"
        // document.getElementsByName("login-input")
    } else {
        passwd.classList.remove("invalid")
        confirmPasswd.classList.remove("invalid")
        errMsg.style.display = "none"
    }
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
