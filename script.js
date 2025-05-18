// frontend/script.js
document.querySelectorAll(".clothing-item").forEach(item => {
  item.addEventListener("click", () => {
    const clothingFile = item.getAttribute("data-name");

    fetch("http://localhost:5000/update-avatar", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ clothing: clothingFile })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("avatar-img").src = data.avatar_url + "?t=" + new Date().getTime();
    })
    .catch(err => console.error("Failed to update avatar:", err));
  });
});
