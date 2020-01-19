let isNavShown = false

function nav() {
    document.getElementById("sideNav").classList.toggle("move")
    // if (isNavShown) {
    //     isNavShown = false
    //     navbar.style.transform = "translateX(-250px)"
    // } else {
    //     isNavShown = true
    //     navbar.style.transform = "translateX(0)"
    // }
}

function dropdown() {
    document.getElementById("dropdown").classList.toggle("show")
}

// window.onclick = function(event) {
//     if (!event.target.matches(".name")) {
//         let dropdowns = document.getElementsByClassName("dropdown-content")
//         for (let i = 0; i < dropdowns.length; i++) {
//             let openDropdown = dropdowns[i]
//             if (openDropdown.classList.contains("show")) {
//                 openDropdown.classList.remove("show")
//             }
//         }
//     }
// }

// puts placeholders and sets margins
if (document.getElementsByName("username")[0] !== undefined) {
    document.getElementsByName("username")[0].placeholder = "Username"
}
if (document.getElementsByName("email")[0] !== undefined) {
    document.getElementsByName("email")[0].placeholder = "Email"
}
if (document.getElementsByName("password")[0] !== undefined) {
    document.getElementsByName("password")[0].placeholder = "Password"
}
if (document.getElementsByName("confirm")[0] !== undefined) {
    document.getElementsByName("confirm")[0].placeholder = "Confirm Password"
}
if (document.getElementsByName("title")[0] !== undefined) {
    document.getElementsByName("title")[0].placeholder = "Title"
}
if (document.getElementsByName("deadline")[0] !== undefined) {
    document.getElementsByName("deadline")[0].placeholder = "Deadline"
}
if (document.getElementsByName("description")[0] !== undefined) {
    document.getElementsByName("description")[0].placeholder = "Description"
}
