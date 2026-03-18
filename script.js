// Add secondary-border-color class on li hover
const listItems = document.querySelectorAll("ul.link-list li");
const fullscreenContainer = document.querySelector(".fullscreen-container");

listItems.forEach(function(li) {
    li.addEventListener("mouseenter", function() {
        fullscreenContainer.classList.add("secondary-border-color");
    });

    li.addEventListener("mouseleave", function() {
        fullscreenContainer.classList.remove("secondary-border-color");
    });
});


// Handle image hover for ascii-art swap
const asciiImage = document.querySelector(".ascii-image");
if (asciiImage) {
    const originalSrc = asciiImage.src;
    const hoverSrc = asciiImage.getAttribute("data-hover-src");

    asciiImage.addEventListener("mouseenter", function() {
        fullscreenContainer.classList.add("secondary-border-color");
        if (hoverSrc) {
            this.src = hoverSrc;
        }
    });

    asciiImage.addEventListener("mouseleave", function() {
        fullscreenContainer.classList.remove("secondary-border-color");
        this.src = originalSrc;
    });
}
