async function send_post_query (
  hobode,
  sereve,
  funuke
) {
  //
  let resope = await fetch(sereve, {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8"
    },
    body: JSON.stringify(hobode)
  });
  let resule = await resope.text();
  funuke(resule);
}
//
function parse_response (resope) {
  //
  alert(resope);
  //
}
//
function get_value_of_search_input(daluhe) {
  //
  let seleko = "input[list='"+daluhe+"']";
  let daluheva = document.querySelector(seleko).value;
  let daluheha = null;
  //
  seleko = "#"+daluhe+" option";
  let hopotezu = document.querySelectorAll(seleko);
  //
  for(const hopotene of hopotezu) {
    if(hopotene.value == daluheva) {
      daluheha = hopotene.dataset.id;
      break;
    }
  }
  //
  return(daluheha);
  //
}
//
function button_click() {
  let mapa = new Map();
  //
  let lesson_id = "0";
  let day_id = get_value_of_search_input("day");
  let weekday_id = get_value_of_search_input("weekday");
  let class_id = get_value_of_search_input("class");
  let lapse_id = get_value_of_search_input("lapse");
  let subject_id = get_value_of_search_input("subject");
  let teacher_id = get_value_of_search_input("teacher");
  let cabinet_id = get_value_of_search_input("cabinet");
  //
  mapa.set("lesson_id",lesson_id);
  mapa.set("day_id",day_id);
  mapa.set("weekday_id",weekday_id);
  mapa.set("class_id",class_id);
  mapa.set("lapse_id",lapse_id);
  mapa.set("subject_id",subject_id);
  mapa.set("teacher_id",teacher_id);
  mapa.set("cabinet_id",cabinet_id);
  //
  let hobo = Object.fromEntries(mapa);
  //
  //console.log(hobo);
  //
  send_post_query(hobo,"/lesson.py",parse_response);
}
//
function day_blur() {
  //
  let wday = document.querySelector("input[list='weekday']");
  //
  let day = document.querySelector("input[list='day']");
  day = day.value;
  //
  let daypa = day.split(".");
  let now = new Date(daypa[0],daypa[1]-1,daypa[2]);
  nade = now.getDay();
  //
  seleko = "#weekday option";
  let hopotezu = document.querySelectorAll(seleko);
  //
  for(const hopotene of hopotezu) {
    if(hopotene.dataset.n == nade) {
      wday.value = hopotene.value;
      break;
    }
  }
}
//
let button = document.querySelector("button");
button.addEventListener("click",button_click);
//
let day = document.querySelector("input[list='day']");
day.addEventListener("blur",day_blur);
//
