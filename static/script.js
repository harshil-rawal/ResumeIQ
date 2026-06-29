const fileInput = document.getElementById("resume");
const dropArea = document.getElementById("drop-area");
const fileName = document.getElementById("file-name");
const fileSize = document.getElementById("file-size");
const filePreview = document.getElementById("file-preview");
const fileIcon = document.getElementById("file-icon");
const removeButton = document.getElementById("remove-file");
const uploadButton = document.getElementById("upload-btn");

const buttonText = document.getElementById("button-text");

const loader = document.getElementById("loader");

function updateFile(file) {

    fileName.textContent = file.name;

    fileSize.textContent =
        (file.size / 1024).toFixed(1) + " KB";

    const extension =
        file.name.split(".").pop().toLowerCase();

    if (extension === "pdf") {

        fileIcon.textContent = "📕";

    }

    else if (extension === "doc" || extension === "docx") {

        fileIcon.textContent = "📝";

    }

    else {

        fileIcon.textContent = "📄";

    }

    filePreview.style.display = "flex";

}

fileInput.addEventListener("change", function () {

    if (this.files.length > 0) {

        updateFile(this.files[0]);

    }

});

dropArea.addEventListener("dragover", function (e) {

    e.preventDefault();

    dropArea.classList.add("dragging");

});

dropArea.addEventListener("dragleave", function () {

    dropArea.classList.remove("dragging");

});

dropArea.addEventListener("drop", function (e) {

    e.preventDefault();

    dropArea.classList.remove("dragging");

    const files = e.dataTransfer.files;

    if (files.length > 0) {

        fileInput.files = files;

        updateFile(files[0]);

    }

});

removeButton.addEventListener("click", function () {

    fileInput.value = "";

    filePreview.style.display = "none";

    fileName.textContent = "No file selected";

    fileSize.textContent = "";

    fileIcon.textContent = "📄";

});

document.querySelector("form").addEventListener("submit", function () {

    uploadButton.disabled = true;

    buttonText.textContent = "Analyzing Resume...";

    loader.style.display = "inline-block";

});