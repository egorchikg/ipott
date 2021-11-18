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
function get_value_of_hidden_input(pa) {
  //
  let seleko = "input[type='hidden']";
  let daluheva = pa.querySelector(seleko).value;
  //
  return(daluheva);
}
//
function get_value_of_search_input(daluhe,pa) {
  //
  let seleko = "input[list='"+daluhe+"']";
  let daluheva = pa.querySelector(seleko).value;
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
function select_button_click(event) {
  let button = event.currentTarget;
  let pa = button.parentNode;
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "select";
  //alert(ka);
  //
  let command = ka;
  let day_id = get_value_of_search_input("day",pa);
  let class_id = get_value_of_search_input("class",pa);
  let lapse_id = get_value_of_search_input("lapse",pa);
  let subject_id = get_value_of_search_input("subject",pa);
  let teacher_id = get_value_of_search_input("teacher",pa);
  let cabinet_id = get_value_of_search_input("cabinet",pa);
  //
  let z = 0;
  mapa.set("command",command);
  if(day_id!=null){mapa.set("day_id",day_id);z++;}
  if(class_id!=null){mapa.set("class_id",class_id);z++;}
  if(lapse_id!=null){mapa.set("lapse_id",lapse_id);z++;}
  if(subject_id!=null){mapa.set("subject_id",subject_id);z++;}
  if(teacher_id!=null){mapa.set("teacher_id",teacher_id);z++;}
  if(cabinet_id!=null){mapa.set("cabinet_id",cabinet_id);z++;}
  //
  if(z > 0) {
    let hobo = Object.fromEntries(mapa);
    //
    console.log(hobo);
    //
    //send_post_query(hobo,"/ipott/lesson.py",parse_response);
  }
}
//
function insert_button_click(event) {
  let button = event.currentTarget;
  let pa = button.parentNode;
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "insert";
  //alert(ka);
  //
  let command = ka;
  let lesson_id = "0";
  let day_id = get_value_of_search_input("day",pa);
  let class_id = get_value_of_search_input("class",pa);
  let lapse_id = get_value_of_search_input("lapse",pa);
  let subject_id = get_value_of_search_input("subject",pa);
  let teacher_id = get_value_of_search_input("teacher",pa);
  let cabinet_id = get_value_of_search_input("cabinet",pa);
  //
  mapa.set("command",command);
  mapa.set("lesson_id",lesson_id);
  mapa.set("day_id",day_id);
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
function update_button_click(event) {
  let button = event.currentTarget;
  let pa = button.parentNode;
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "update";
  //alert(ka);
  //
  let command = ka;
  let lesson_id = get_value_of_hidden_input(pa);
  let day_id = get_value_of_search_input("day",pa);
  let class_id = get_value_of_search_input("class",pa);
  let lapse_id = get_value_of_search_input("lapse",pa);
  let subject_id = get_value_of_search_input("subject",pa);
  let teacher_id = get_value_of_search_input("teacher",pa);
  let cabinet_id = get_value_of_search_input("cabinet",pa);
  //
  mapa.set("command",command);
  mapa.set("lesson_id",lesson_id);
  mapa.set("day_id",day_id);
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
function delete_button_click(event) {
  let button = event.currentTarget;
  let pa = button.parentNode;
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "delete";
  //alert(ka);
  //
  let command = ka;
  let lesson_id = get_value_of_hidden_input(pa);
  //
  mapa.set("command",command);
  mapa.set("lesson_id",lesson_id);
  //
  let hobo = Object.fromEntries(mapa);
  //
  console.log(hobo);
  //
  send_post_query(hobo,"/ipott/lesson.py",parse_response);
}
//
/*
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
*/
//
/*
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
*/
//
let ins_buttons = document.querySelectorAll("button.insert");
for(const ins_button of ins_buttons) {
  ins_button.addEventListener("click",insert_button_click);
}
//
let del_buttons = document.querySelectorAll("button.delete");
for(const del_button of del_buttons) {
  del_button.addEventListener("click",delete_button_click);
}
//
let upd_buttons = document.querySelectorAll("button.update");
for(const upd_button of upd_buttons) {
  upd_button.addEventListener("click",update_button_click);
}
//
let sel_buttons = document.querySelectorAll("button.select");
for(const sel_button of sel_buttons) {
  sel_button.addEventListener("click",select_button_click);
}
//
/*
let i_day = document.querySelector("input[list='day'].insert");
i_day.addEventListener("blur",insert_day_blur);
*/
//
/*
let d_day = document.querySelector("input[list='day'].delete");
d_day.addEventListener("blur",delete_day_blur);
*/
//
