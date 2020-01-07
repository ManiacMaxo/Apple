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

function openModal() {
    document.getElementById("loginModal").style.display = "block"
}

function closeModal() {
    document.getElementById("loginModal").style.display = "none"
}

// function check
