const form = document.getElementById('image-form');
const outputImage = document.getElementById('output-image');
const inputImageButton = document.getElementById('input-image-button');
const inputImagecontainer = document.getElementById('input-container');
const inputImage = document.getElementById('input-image');
const prediction = document.getElementById('prediction');
const custom_upload_btn = document.getElementById('custom_btn')




inputImageButton.addEventListener('change', async (event) => {
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