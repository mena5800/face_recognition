const form = document.getElementById('image-form');
const outputImage = document.getElementById('output-image');
const inputImageButton = document.getElementById('input-image-button');
const inputImagecontainer = document.getElementById('input-container');
const inputImage = document.getElementById('input-image');
const prediction = document.getElementById('prediction');
const custom_upload_btn = document.getElementById('custom_btn');
const video = document.getElementById('video');
const video_cont = document.getElementById('video_contaner');
const roc = document.getElementById('ROC');
const roc_cont = document.getElementById('ROC_cont');
const big_cont = document.getElementById('big-image-container');



roc.addEventListener('click', function () {
  big_cont.style.display = "none"
  roc_cont.style.display = "flex"
});


inputImageButton.addEventListener('change', async (event) => {
  video_cont.style.display = "none";
  inputImagecontainer.style.display = "inline"
  big_cont.style.display = "flex"
  roc_cont.style.display = "none"
  capture = document.getElementById('capture');
  capture.style.display = "none"
  // Create a new FileReader object
  var reader = new FileReader();

  // Listen for the load event of the FileReader
  reader.addEventListener('load', function () {

    inputImage.src = reader.result;

  });

  // Read the selected file as a data URL
  reader.readAsDataURL(inputImageButton.files[0]);
  event.preventDefault();

  const formData = new FormData(form);

  try {
    const response = await fetch('/transform', {
      method: 'POST',
      body: formData
    });

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    prediction.innerText = response.statusText
    console.log(url)
    outputImage.src = url;
  } catch (error) {
    console.error(error);
  }
});


custom_upload_btn.addEventListener('click', function () { inputImageButton.click(); })

// Get access to the user's camera
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function (stream) {
    video.srcObject = stream;
    video.play();
  })
  .catch(function (err) {
    console.log("Error: " + err);
  });

// Capture the photo and save as a JPEG image
document.getElementById('capture').addEventListener('click', function () {
  var canvas = document.getElementById('canvas');
  var context = canvas.getContext('2d');
  var video = document.getElementById('video');
  // video.style.display = "none";
  // inputImagecontainer.style.display = "inline"
  // Draw the video frame to the canvas
  context.drawImage(video, 0, 0, canvas.width, canvas.height);


  // Convert the canvas to a blob object
  canvas.toBlob(async function (blob) {
    // Send the image data to Flask server using fetch
    var formData = new FormData();
    formData.append('image-file', blob, 'photo.jpg');
    try {
      const response = await fetch('/transform', {
        method: 'POST',
        body: formData
      });
      const processedImageBlob = await response.blob();
      // Display the processed image in the web app
      outputImage.src = URL.createObjectURL(processedImageBlob);
      prediction.innerText = response.statusText


    } catch (error) {
      console.error(error);
    }
  }, 'image/jpeg');
});


const camera_btn = document.getElementById("camera_btn");

camera_btn.addEventListener('click', function () {
  video_cont.style.display = "inline";
  video.style.display = "inline";
  capture = document.getElementById('capture');
  capture.style.display = "inline"
  inputImagecontainer.style.display = "none"
  big_cont.style.display = "flex"
  roc_cont.style.display = "none"
});

