var inputText = document.querySelector("#username")
var passText = document.querySelector("#password")
var btnSubmit = document.querySelector("#submitBtn")

inputText.addEventListener('change', () => {
    if ((inputText.value === "") && (passText.value === "")) {
        btnSubmit.disabled = true
    } else {
        btnSubmit.disabled = false
    }
})
passText.addEventListener('change', () => {
    if ((inputText.value === "") && (passText.value === "")) {
        btnSubmit.disabled = true
    } else {
        btnSubmit.disabled = false
    }
})
btnSubmit.addEventListener('click', () => {
    if ((inputText.value === "") && (passText.value === "")) {
        window.location.href("../templates/login.html")
        alert("here")
    }
})