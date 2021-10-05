let current = 0;
let mains = document.querySelectorAll(".main");
let mains_len = mains.length;
//
function next() {
  if(current < mains_len-1) {
    mains[current].style.display = "none";
    mains[current+1].style.display = "flex";
    current++;
  } else {
    mains[current].style.display = "none";
    current = 0;
    mains[current].style.display = "flex";
  }
}
function prev() {
  if(current > 0) {
    mains[current].style.display = "none";
    mains[current-1].style.display = "flex";
    current--;
  } else {
    mains[current].style.display = "none";
    current = mains.length-1;
    mains[current].style.display = "flex";
  }
}
function keydown(event) {
  if(event.code == 'ArrowRight') {
    next();
  }
  if(event.code == 'ArrowLeft') {
    prev();
  }
}
//
document.addEventListener("keydown",keydown);
setInterval(next, 15000);
