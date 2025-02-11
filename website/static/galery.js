let left = document.getElementById("arrowleft");
let right = document.getElementById("arrowright");
let carousel = document.getElementById("carousel");

for (let i = 1; i <= 13; i++){
    let img = document.createElement("img");
    img.src = "/static/src/image" + i + ".jpg"
    carousel.appendChild(img);
}

left.addEventListener('click', clickLeft);
right.addEventListener('click', clickRight);

const carouselElem = 2;
const width = 300 / carouselElem;
const item = carousel.children.length - carouselElem;
let current = 0;

for (let i=0; i < carousel.childElementCount; i++){
    carousel.children[i].style.width = width + '%';
    carousel.children[i].style.maxWidth = width + '%';
}

function clickLeft(){
    current--;
    if (current >= 0){
        carousel.style.transform = `translateX(-${width * current}%)`;
    }
    else{
        current = 0;
    }
}
function clickRight(){
    current++;
    if (current <= item){
        carousel.style.transform = `translateX(-${width * current}%)`;
    }
    else{
        current = item;
    }
}