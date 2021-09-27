let current = 0;
let mains = document.querySelectorAll(".main");
let mains_len = mains.length;
//
function keydown(event) {
  if(event.code == 'ArrowRight') {
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
  if(event.code == 'ArrowLeft') {
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
}
//
document.addEventListener("keydown",keydown);
