//  Log viewport dimensions
window.addEventListener("load", function () {
  console.log(`Viewport ${window.innerWidth}x${window.innerHeight}`);
});

// Handle window resize
window.addEventListener("resize", function () {
  console.log(`Resize: Viewport ${window.innerWidth}x${window.innerHeight}`);
});
