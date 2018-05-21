// Get the modal
var modal = document.getElementById('myModal');
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
onc = function(k) {
        modal.style.display = "block";
        document.getElementsByTagName("iframe")[0].setAttribute("src", 'https://www.youtube.com/embed/' + k);
    }
    // When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    document.getElementsByTagName("iframe")[0].setAttribute("src", ' ');

}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        document.getElementsByTagName("iframe")[0].setAttribute("src", ' ');
    }
}
