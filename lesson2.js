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
function parse_response(resope) {
  //
  let hobo = JSON.parse(resope);
  //
  for(let ho of hobo) {
    if(false) {
      console.log();
    } else if(ho.command == "alert") {
      //alert(ho.message);
      hanema();
    } else if(ho.command == "append") {
      console.log("append");
      append_ho(ho);
    }
    console.log(ho);
  }
  //
}
//
function hanema() {
  body.classList.remove("hanema");
  body.classList.add("hanema");
}
//
function append_ho(ho) {
  //
  let tname = null;
  let dale = null;
  //
  let hidden_input = document.createElement('input');
  hidden_input.setAttribute("type","hidden");
  hidden_input.classList.add("update");
  hidden_input.classList.add("delete");
  hidden_input.setAttribute("value",ho.lesson_id);
  //
  let day_input = document.createElement('input');
  day_input.setAttribute("type","date");
  day_input.classList.add("day");
  day_input.classList.add("update");
  day_input.classList.add("delete");
  let ho_re = ho.day_name;
  ho_re = ho_re.replace(/[.]/g,"-");
  day_input.setAttribute("value",ho_re);
  //
  tname = "class";
  let class_input = document.createElement('select');
  class_input.classList.add(tname);
  class_input.classList.add("update");
  class_input.classList.add("delete");
  dale = document.querySelector("datalist#"+tname);
  class_input.innerHTML = dale.innerHTML;
  class_input.value = ho.class_name;
  //
  tname = "lapse";
  let lapse_input = document.createElement('select');
  lapse_input.classList.add(tname);
  lapse_input.classList.add("update");
  lapse_input.classList.add("delete");
  dale = document.querySelector("datalist#"+tname);
  lapse_input.innerHTML = dale.innerHTML;
  lapse_input.value = ho.lapse_name;
  //
  tname = "subject";
  let subject_input = document.createElement('select');
  subject_input.classList.add(tname);
  subject_input.classList.add("update");
  subject_input.classList.add("delete");
  dale = document.querySelector("datalist#"+tname);
  subject_input.innerHTML = dale.innerHTML;
  subject_input.value = ho.subject_name;
  //
  tname = "teacher";
  let teacher_input = document.createElement('select');
  teacher_input.classList.add(tname);
  teacher_input.classList.add("update");
  teacher_input.classList.add("delete");
  dale = document.querySelector("datalist#"+tname);
  teacher_input.innerHTML = dale.innerHTML;
  teacher_input.value = ho.teacher_name;
  //
  tname = "cabinet";
  let cabinet_input = document.createElement('select');
  cabinet_input.classList.add(tname);
  cabinet_input.classList.add("update");
  cabinet_input.classList.add("delete");
  dale = document.querySelector("datalist#"+tname);
  cabinet_input.innerHTML = dale.innerHTML;
  cabinet_input.value = ho.cabinet_name;
  //
  let update_button = document.createElement('button');
  update_button.classList.add("update");
  update_button.addEventListener("click",update_button_click);
  update_button.innerHTML = "Изменить";
  //
  let delete_button = document.createElement('button');
  delete_button.classList.add("delete");
  delete_button.addEventListener("click",delete_button_click);
  delete_button.innerHTML = "Удалить";
  //
  let rovo_div = document.createElement('div');
  rovo_div.classList.add("rovo");
  rovo_div.append(hidden_input);
  rovo_div.append(day_input);
  rovo_div.append(class_input);
  rovo_div.append(lapse_input);
  rovo_div.append(subject_input);
  rovo_div.append(teacher_input);
  rovo_div.append(cabinet_input);
  rovo_div.append(update_button);
  rovo_div.append(delete_button);
  //
  let sc = document.body.querySelector("script");
  let rovo_in = document.body.insertBefore(rovo_div,sc);
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
function get_value_of_date_input(daluhe,pa) {
  //
  let seleko = "."+daluhe;
  let daluheva = pa.querySelector(seleko).value;
  daluheva = daluheva.replace(/-/g,".");
  //
  //console.log(daluheva);
  //
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
  /*
  if(daluheha == null) {
    alert("Даты "+daluheva+" нет в базе данных!");
  }
  */
  return(daluheha);
  //
}
//
function get_value_of_select(daluhe,pa) {
  //
  let seleko = "select."+daluhe;
  let daluheva = pa.querySelector(seleko);
  let daluheme = daluheva.options[daluheva.selectedIndex];
  let daluheha = daluheme.dataset.id;
  //
  //console.log(daluheme.text);
  //console.log(daluheha);
  //
  if(daluheha == 0) {
    return(null);
  } else {
    return(daluheha);
  }
}
//
function delete_excess_rovos() {
  let rovos = document.querySelectorAll(".rovo");
  for(let rovo of rovos) {
    if(!rovo.classList.contains("first")) {
      rovo.remove();
    }
  }
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
  let day_id = get_value_of_date_input("day",pa);
  let class_id = get_value_of_select("class",pa);
  let lapse_id = get_value_of_select("lapse",pa);
  let subject_id = get_value_of_select("subject",pa);
  let teacher_id = get_value_of_select("teacher",pa);
  let cabinet_id = get_value_of_select("cabinet",pa);
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
    send_post_query(hobo,"/ipott/lesson.py",parse_response);
  }
  //
  delete_excess_rovos();
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
  let day_id = get_value_of_date_input("day",pa);
  let class_id = get_value_of_select("class",pa);
  let lapse_id = get_value_of_select("lapse",pa);
  let subject_id = get_value_of_select("subject",pa);
  let teacher_id = get_value_of_select("teacher",pa);
  let cabinet_id = get_value_of_select("cabinet",pa);
  //
  let z = 0;
  mapa.set("command",command);
  mapa.set("lesson_id",lesson_id);
  if(day_id!=null){mapa.set("day_id",day_id);z++;}
  if(class_id!=null){mapa.set("class_id",class_id);z++;}
  if(lapse_id!=null){mapa.set("lapse_id",lapse_id);z++;}
  if(subject_id!=null){mapa.set("subject_id",subject_id);z++;}
  if(teacher_id!=null){mapa.set("teacher_id",teacher_id);z++;}
  if(cabinet_id!=null){mapa.set("cabinet_id",cabinet_id);z++;}
  //
  if(z == 6) {
    let hobo = Object.fromEntries(mapa);
    //
    console.log(hobo);
    //
    send_post_query(hobo,"/ipott/lesson.py",parse_response);
    //
  } else {
    alert("Одно из полей заполнено неверно!");
  }
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
  let day_id = get_value_of_date_input("day",pa);
  let class_id = get_value_of_select("class",pa);
  let lapse_id = get_value_of_select("lapse",pa);
  let subject_id = get_value_of_select("subject",pa);
  let teacher_id = get_value_of_select("teacher",pa);
  let cabinet_id = get_value_of_select("cabinet",pa);
  //
  let z = 0;
  mapa.set("command",command);
  mapa.set("lesson_id",lesson_id);
  if(day_id!=null){mapa.set("day_id",day_id);z++;}
  if(class_id!=null){mapa.set("class_id",class_id);z++;}
  if(lapse_id!=null){mapa.set("lapse_id",lapse_id);z++;}
  if(subject_id!=null){mapa.set("subject_id",subject_id);z++;}
  if(teacher_id!=null){mapa.set("teacher_id",teacher_id);z++;}
  if(cabinet_id!=null){mapa.set("cabinet_id",cabinet_id);z++;}
  //
  if(z == 6) {
    let hobo = Object.fromEntries(mapa);
    //
    console.log(hobo);
    //
    send_post_query(hobo,"/ipott/lesson.py",parse_response);
  }
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
  //
  pa.remove();
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
