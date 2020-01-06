function animate() {
    var popup = document.getElementById("popup")
    popup.classList.toggle("show")
}

function openNav() {
    document.getElementById("sideNav").style.width = "250px"
}

function closeNav() {
    document.getElementById("sideNav").style.width = "0"
}

function openModal() {
    document.getElementById("loginModal").style.display = "block"
}

function closeModal() {
    document.getElementById("loginModal").style.display = "none"
}
