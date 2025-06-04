document.addEventListener("DOMContentLoaded", () => {
  const dropUpButtons = document.querySelectorAll(".drop-up");
  dropUpButtons.forEach((button) => {
    button.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });
});
