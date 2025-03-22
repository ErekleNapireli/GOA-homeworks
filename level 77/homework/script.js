const image = document.getElementById("image");
const next = document.getElementById("next");
const previous = document.getElementById("previous");

let i = 0;
const images = [
    "./PICS/img1.jpg",
    "./PICS/img2.jpg",
    "./PICS/img3.jpg"
];

// 3) შექმენით Image slider 3 ფოტოთი
// 4) შექმენით image slider 5 ფოტოთი
// უნივერსალური კოდია და სურათის ნებისმიერ რაოდენობაზე მუშაობს

next.addEventListener("click", function(){
    i++;
    if (i == images.length){
        i = 0;
    }
    image.src = images[i];
});

prev.addEventListener("click", function(){
    i--;
    if (i == -1){
        i = images.length -1;
    }
    image.src = images[i];
});