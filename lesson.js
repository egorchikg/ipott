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
function get_value_of_search_input(daluhe,kalase) {
  //
  let seleko = "input[list='"+daluhe+"']."+kalase;
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
function delete_button_click() {
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "delete";
  //alert(ka);
  //
  let command = ka;
  let day_id = get_value_of_search_input("day",ka);
  let weekday_id = get_value_of_search_input("weekday",ka);
  let class_id = get_value_of_search_input("class",ka);
  let lapse_id = get_value_of_search_input("lapse",ka);
  let subject_id = get_value_of_search_input("subject",ka);
  let teacher_id = get_value_of_search_input("teacher",ka);
  let cabinet_id = get_value_of_search_input("cabinet",ka);
  //
  mapa.set("command",command);
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
  console.log(hobo);
  //
  send_post_query(hobo,"/ipott/lesson.py",parse_response);
}
//
function insert_button_click() {
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "insert";
  //alert(ka);
  //
  let command = ka;
  let lesson_id = "0";
  let day_id = get_value_of_search_input("day",ka);
  let weekday_id = get_value_of_search_input("weekday",ka);
  let class_id = get_value_of_search_input("class",ka);
  let lapse_id = get_value_of_search_input("lapse",ka);
  let subject_id = get_value_of_search_input("subject",ka);
  let teacher_id = get_value_of_search_input("teacher",ka);
  let cabinet_id = get_value_of_search_input("cabinet",ka);
  //
  mapa.set("command",command);
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
  console.log(hobo);
  //
  send_post_query(hobo,"/ipott/lesson.py",parse_response);
}
//
function insert_day_blur() {
  //
  let ka = "insert";
  //
  let wday = document.querySelector("input[list='weekday']."+ka);
  //
  let day = document.querySelector("input[list='day']."+ka);
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
function delete_day_blur() {
  //
  let ka = "delete";
  //
  let wday = document.querySelector("input[list='weekday']."+ka);
  //
  let day = document.querySelector("input[list='day']."+ka);
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
let ins_button = document.querySelector("button.insert");
ins_button.addEventListener("click",insert_button_click);
//
let del_button = document.querySelector("button.delete");
del_button.addEventListener("click",delete_button_click);
//
let i_day = document.querySelector("input[list='day'].insert");
i_day.addEventListener("blur",insert_day_blur);
//
let d_day = document.querySelector("input[list='day'].delete");
d_day.addEventListener("blur",delete_day_blur);
//
