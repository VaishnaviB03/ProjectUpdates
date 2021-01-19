const INCREASE_BUTTON = document.querySelectorAll("[data-open]")
const DECREASE_BUTTON = document.querySelectorAll("[data-close]")

for (const INC of INCREASE_BUTTON) {
    INC.addEventListener("click", function() {
        const BUTTON_ID = this.dataset.open; //1
        const TEXT_AREA = document.getElementsByClassName(BUTTON_ID) //1
        TEXT_AREA.value = parseInt(TEXT_AREA.value) + 1
        console.log(BUTTON_ID)
        console.log(TEXT_AREA)
        console.log(TEXT_AREA.value)
    });
}
for (const DEC of DECREASE_BUTTON) {
    DEC.addEventListener("click", function() {
        const BUTTON_ID = this.dataset.open;
        const TEXT_AREA = document.getElementsByClassName(BUTTON_ID)
        TEXT_AREA.value = parseInt(TEXT_AREA.value) - 1
    });
}