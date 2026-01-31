//  Log viewport dimensions
window.addEventListener("load", function() {
    console.log(`Viewport ${window.innerWidth}x${window.innerHeight}`);
});

// Handle window resize
window.addEventListener("resize", function() {
    console.log(`Resize: Viewport ${window.innerWidth}x${window.innerHeight}`);
});

// Handle image hover for ascii-art swap
const asciiImage = document.querySelector(".ascii-image");
if (asciiImage) {
    const originalSrc = asciiImage.src;
    const hoverSrc = asciiImage.getAttribute("data-hover-src");

    asciiImage.addEventListener("mouseenter", function() {
        if (hoverSrc) {
            this.src = hoverSrc;
        }
    });

    asciiImage.addEventListener("mouseleave", function() {
        this.src = originalSrc;
    });
}
