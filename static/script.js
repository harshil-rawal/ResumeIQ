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
    if (!fileName || !fileSize || !fileIcon || !filePreview) {
        return;
    }

    fileName.textContent = file.name;
    fileSize.textContent = (file.size / 1024).toFixed(1) + " KB";

    const extension = file.name.split(".").pop().toLowerCase();
    if (extension === "pdf") {
        fileIcon.textContent = "📕";
    } else if (extension === "doc" || extension === "docx") {
        fileIcon.textContent = "📝";
    } else {
        fileIcon.textContent = "📄";
    }

    filePreview.style.display = "flex";
}

function initUploadInteractions() {
    if (!fileInput || !dropArea || !filePreview || !removeButton || !uploadButton || !buttonText || !loader) {
        return;
    }

    fileInput.addEventListener("change", function () {
        if (this.files.length > 0) {
            updateFile(this.files[0]);
        }
    });

    ["dragenter", "dragover"].forEach((evt) => {
        dropArea.addEventListener(evt, (e) => {
            e.preventDefault();
            dropArea.classList.add("dragging");
        });
    });

    ["dragleave", "dragend", "drop"].forEach((evt) => {
        dropArea.addEventListener(evt, (e) => {
            e.preventDefault();
            dropArea.classList.remove("dragging");
        });
    });

    dropArea.addEventListener("drop", function (e) {
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

    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            uploadButton.disabled = true;
            buttonText.textContent = "Analyzing Resume...";
            loader.style.display = "inline-block";
        });
    }
}

function initRevealAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver(function (entries) {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = "1";
                entry.target.style.transform = "translateY(0)";
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll(".feature-card, .step, .section-header").forEach((el) => {
        el.style.opacity = "0";
        el.style.transform = "translateY(20px)";
        el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
        observer.observe(el);
    });
}

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
        anchor.addEventListener("click", function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    block: "start"
                });
            }
        });
    });
}

function animateCircularRing(circle, textNode, target) {
    const circumference = circle.getTotalLength ? circle.getTotalLength() : 2 * Math.PI * (circle.r ? circle.r.baseVal.value : 50);
    const offset = circumference * (1 - target / 100);

    circle.style.strokeDasharray = `${circumference} ${circumference}`;
    circle.style.strokeDashoffset = `${circumference}`;

    setTimeout(() => {
        circle.style.strokeDashoffset = `${offset}`;
    }, 150);

    if (textNode) {
        let current = 0;
        const step = Math.max(1, Math.round(target / 60));
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            textNode.textContent = `${current}%`;
        }, 18);
    }
}

function animateResultPage() {
    const heroCircle = document.querySelector('.hero-dashboard .ring-progress');
    const heroText = document.querySelector('.hero-dashboard .score-count');
    const heroTarget = heroCircle ? Number(heroCircle.dataset.score || 0) : 0;

    const resultCircle = document.querySelector('.circular-chart .circle');
    const resultText = document.querySelector('.circular-chart .percentage');
    const resultTarget = 92;

    if (heroCircle && heroText && heroTarget) {
        animateCircularRing(heroCircle, heroText, heroTarget);
    }
    if (resultCircle && resultText) {
        animateCircularRing(resultCircle, resultText, resultTarget);
    }

    const resultProgressBars = document.querySelectorAll('.result-progress-fill');
    const suggestionCards = document.querySelectorAll('.suggestion-card');
    const skillChips = document.querySelectorAll('.skill-pill');
    const keywordChips = document.querySelectorAll('.keyword-chip');

    resultProgressBars.forEach((bar, index) => {
        const fill = Number(bar.dataset.fill || 80);
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = `${fill}%`;
        }, 380 + index * 70);
    });

    suggestionCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(18px)';
        card.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 450 + index * 100);
    });

    [...skillChips, ...keywordChips].forEach((chip, index) => {
        chip.style.opacity = '0';
        chip.style.transform = 'translateY(10px)';
        chip.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
        setTimeout(() => {
            chip.style.opacity = '1';
            chip.style.transform = 'translateY(0)';
        }, 520 + index * 60);
    });
}

function initResultAnimation() {
    if (document.querySelector('.hero-dashboard .ring-progress') || document.querySelector('.circular-chart .circle')) {
        window.addEventListener('load', animateResultPage);
    }
}

initUploadInteractions();
initRevealAnimations();
initSmoothScroll();
initResultAnimation();

