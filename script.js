function keydown(event) {
  if(event.code == 'ArrowRight') {
    let mains = document.querySelectorAll(".main");
    mains[0].style.display = "none";
    mains[1].style.display = "flex";
  }
  if(event.code == 'ArrowLeft') {
    let mains = document.querySelectorAll(".main");
    mains[1].style.display = "none";
    mains[0].style.display = "flex";
  }
}
document.addEventListener("keydown",keydown);
