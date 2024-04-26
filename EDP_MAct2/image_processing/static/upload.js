function showImage(src, target) {
	const fr = new FileReader();
	// when image is loaded, set the src of the image where you want to display it
	fr.onload = function (e) {
		target.src = this.result;
	};
	src.addEventListener("change", () => {
		// fill fr with image data
		fr.readAsDataURL(src.files[0]);
	});
}

const target = document.getElementById("imageContainer");
const src = document.getElementById("id_docfile");
showImage(src, target);