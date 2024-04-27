const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const captureBtn = document.getElementById("captureBtn");
const resultDiv = document.getElementById("result");

let imageData;

// Function to extract CSRF token from cookies
function getCSRFToken() {
  const cookies = document.cookie.split(";");
  for (let i = 0; i < cookies.length; i++) {
    const cookie = cookies[i].trim();
    if (cookie.startsWith("csrftoken=")) {
      return cookie.substring("csrftoken=".length, cookie.length);
    }
  }
  return null;
}

navigator.mediaDevices
  .getUserMedia({ video: true })
  .then((stream) => {
    video.srcObject = stream;
  })
  .catch((err) => {
    console.error("Error accessing the camera:", err);
  });

captureBtn.addEventListener("click", async () => {
  const canvas1 = document.createElement("canvas");
  const context = canvas1.getContext("2d");
  canvas1.width = video.videoWidth;
  canvas1.height = video.videoHeight;
  context.drawImage(video, 0, 0);

  const blob = await new Promise((resolve) =>
    canvas1.toBlob(resolve, "image/jpeg")
  );
  imageData = canvas1.toDataURL("image/jpg");
  image.src = imageData;

  const formData = new FormData();
  formData.append("image", blob, "image.jpeg");

  console.log(formData);
  const csrftoken = getCSRFToken();
  fetch("classify-captured/", {
    method: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
    },
    body: formData,
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("category").innerText = data.category;
      document.getElementById("accuracy").innerText = data.accuracy;
    })
    .catch((error) => {
        console.error("Error fetching data:", error);
      });;
});
