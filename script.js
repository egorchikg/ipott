let $main = null;
let $book = null;
//
let $current = -1;
let $pages = null;
let $pageslen = null;
//
//
function create_page_in_huhale(huhale) {
  let page = document.createElement('div');
  page.classList.add("page");
  return(huhale.appendChild(page));
}
//
function vorosu(halelu,huhale) {
  let hehuhale = huhale.clientHeight;
  huhale.style.height = "auto";
  let te = 0;
  let tadana = false;
  let vereru = [];
  let halelula = halelu.length;
  while(te<halelula) {
    let kohale = halelu[te].cloneNode(true);
    if(tadana) {
      vereru.push(kohale);
      te++;
    } else {
      kohale = huhale.appendChild(kohale);
      let nehehuhale = huhale.clientHeight;
      if(nehehuhale <= hehuhale) {
        te++;
      } else {
        kohale.remove();
        tadana = true;
      }
    }
  }
  huhale.style.maxHeight = hehuhale+"px";
  huhale.style.minHeight = hehuhale+"px";
  //
  return(vereru);
}
//
function convert_main_to_book() {
  //
  $main = document.querySelector(".main");
  $book = document.querySelector(".book");
  //
  let halelu = $main.querySelectorAll(".info");
  let fesone = true;
  while(fesone) {
    let huhale = create_page_in_huhale($book);
    halelu = vorosu(halelu,huhale);
    if(typeof halelu=='undefined' || halelu.length==0) {
      fesone = false;
    }
  }
  //
  $pages = $book.querySelectorAll(".page");
  $pageslen = $pages.length;
}
//
//
function scroll_to(element) {
  element.scrollIntoView(
      {
       behavior:"smooth",
       block:"end",
       inline:"nearest"
      });
}
//
function scroll_to_next_page() {
  if($current < $pageslen-1) {
    $current++;
  } else {
    $current = 0;
  }
  console.log($current);
  scroll_to($pages[$current]);
}
//
function keydown(event) {
  if(event.code == 'KeyJ') {
    scroll_to_next_page();
  }
}
//
function load_dom() {
  convert_main_to_book();
  scroll_to_next_page();
  //setInterval(scroll_to_next_page, 15000);
}
//
document.addEventListener("keydown",keydown);
//
document.addEventListener("DOMContentLoaded",load_dom);
