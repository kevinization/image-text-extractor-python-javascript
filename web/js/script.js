var imageName = "";

function getImageName() {
    imageName = document.getElementById("text-image").files[0].name;
    console.log("image name: " + imageName);
}

document.getElementById("btn-text-from-image").addEventListener("click", () => {
    eel.getText(imageName)(function (imageText) {
        document.getElementById("image-text").innerHTML = imageText;
    })
}, false);