const closetItems = [
    "assets/output.webp", // You’ll add more image paths here
  ];
  
  const closetDiv = document.getElementById("closet");
  const clothingLayer = document.getElementById("clothing-layer");
  
  closetItems.forEach(src => {
    const img = document.createElement("img");
    img.src = src;
    img.className = "clothing-item";
    img.onclick = () => {
      clothingLayer.innerHTML = "";
      const worn = document.createElement("img");
      worn.src = src;
      worn.style.width = "100%";
      clothingLayer.appendChild(worn);
    };
    closetDiv.appendChild(img);
  });
  