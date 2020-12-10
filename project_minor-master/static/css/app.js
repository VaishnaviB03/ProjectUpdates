var inputText = document.getElementById("username");

var passText = document.querySelector("#password");
var submitBtn = document.querySelector("#submitBtn");
var ErrorSpan = document.querySelector("#error")

inputText.addEventListener("change", () => {
    if ((inputText.value === "") && (passText.value === "")) {
        // submitBtn.disabled = true
        alert("enter username ")

    } else {
        submitBtn.disabled = false

    }
})
passText.addEventListener("change", () => {
    if ((inputText.value === "") || (passText.value === "")) {
        submitBtn.disabled = true

    } else {
        submitBtn.disabled = false

    }
})