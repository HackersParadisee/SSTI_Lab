document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form && form.action.endsWith("/event")) {
        form.addEventListener("submit", () => {
            alert("🎉 Event submitted successfully!");
        });
    }
});
