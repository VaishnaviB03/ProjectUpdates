const username = document.getElementById('name')
const pass = document.getElementById('password')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (l) => {
    let messages = []
    if (username.value === '' || username.value == null) {
        messages.push('Name is required')
    }
    if (pass.value === '' || pass.value == null) {
        messages.push('Password is required')
    }
    if (pass.value == null && username.value == null) {
        messages.push('Enter Your Credentials')
    }
    if (messages.length > 0) {
        l.preventDefault()
        errorElement.innerText = messages.join(' , ')
    }
})

function Alert() {
    let name = document.getElementById("c_name").value
    if (name == "") {
        alert(`enter your name`)
    } else {
        alert(`Thanks ${name}! Your response has been recorded`);
    }

}