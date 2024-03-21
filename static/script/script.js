document.getElementById('imageUpload').addEventListener('change', function() {
    if (this.files && this.files[0]) {
        var img = document.getElementById('profilePic');  // Find the image element
        img.src = URL.createObjectURL(this.files[0]); // Set the image source to the selected file
    }
});
