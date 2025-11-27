const fileInput = document.getElementById("fileInput");
const dropzoneWrapper = document.getElementById("dropzone-wrapper");
const preview = document.getElementById("preview");
const changeBtn = document.getElementById("changeBtn");
const generateBtn = document.getElementById("generateBtn");
const form = document.querySelector("form");

function loadFile(file) {
    const reader = new FileReader();
    reader.onload = () => {
        preview.src = reader.result;
        preview.style.display = "block";
        dropzoneWrapper.style.display = "none";

        changeBtn.childNodes[0].textContent = "Change image";
        generateBtn.style.display = "inline-block";
        document.getElementById("textInputs").style.display = "flex";
    };
    reader.readAsDataURL(file);
}

fileInput.addEventListener("change", () => {
    const file = fileInput.files[0];
    if (!file) return;
    loadFile(file);
});

dropzoneWrapper.addEventListener("click", () => {
    fileInput.click();
});

dropzoneWrapper.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropzoneWrapper.classList.add("dragover");
});

dropzoneWrapper.addEventListener("dragleave", () => {
    dropzoneWrapper.classList.remove("dragover");
});

dropzoneWrapper.addEventListener("drop", (e) => {
    e.preventDefault();
    dropzoneWrapper.classList.remove("dragover");
    const file = e.dataTransfer.files[0];
    if (file) loadFile(file);
});

form.addEventListener("submit", (e) => {
    const top = document.getElementById("topText").value.trim();
    const bottom = document.getElementById("bottomText").value.trim();

    if (!top || !bottom) {
        e.preventDefault();
        alert("Please fill both Top and Bottom text!");
    }
});
