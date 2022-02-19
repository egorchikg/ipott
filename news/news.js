let pypy = "news.py"

async function send_post_query(
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
      alert(ho.message);
    } else if(ho.command == "append") {
      console.log("append");
      append_ho(ho);
    }
    console.log(ho);
  }
  //
}
//
function append_ho(ho) {
  //
  let hidden_input = document.createElement('input');
  hidden_input.setAttribute("type","hidden");
  hidden_input.classList.add("delete");
  hidden_input.setAttribute("value",ho.id);
  //
  let image = document.createElement('img');
  image.setAttribute("src",ho.image);
  //
  let daka_input = document.createElement('input');
  daka_input.setAttribute("type","text");
  daka_input.classList.add("delete");
  daka_input.setAttribute("value",ho.daka);
  //
  let dade_input = document.createElement('input');
  dade_input.setAttribute("type","text");
  dade_input.classList.add("delete");
  dade_input.setAttribute("value",ho.dade);
  //
  let delete_button = document.createElement('button');
  delete_button.classList.add("delete");
  delete_button.addEventListener("click",delete_button_click);
  delete_button.innerHTML = "Удалить";
  //
  let lala_div = document.createElement('div');
  lala_div.classList.add("lala");
  lala_div.append(hidden_input);
  lala_div.append(image);
  lala_div.append(daka_input);
  lala_div.append(dade_input);
  lala_div.append(delete_button);
  //
  let sc = document.body.querySelector("script");
  let rovo_in = document.body.insertBefore(lala_div,sc);
  //
}
//
function get_value_of_text_input(daluhe) {
  //
  let seleko = "input."+daluhe;
  let daluheva = document.querySelector(seleko).value;
  //
  return(daluheva);
  //
}
//
function getBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => resolve(reader.result);
    reader.onerror = error => reject(error);
  });
}
//
async function get_value_of_file_input(daluhe) {
  //
  let seleko = "input."+daluhe;
  let dalu = document.querySelector(seleko).files[0];
  let halu = await getBase64(dalu);
  //
  return(halu);
  //
}
//
function get_value_of_hidden_input(pa,daluhe) {
  //
  let seleko = "input."+daluhe;
  let daluheva = pa.querySelector(seleko).value;
  //
  return(daluheva);
  //
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
  let id = get_value_of_hidden_input(pa,ka);
  //
  mapa.set("command",command);
  mapa.set("id",id);
  //
  let hobo = Object.fromEntries(mapa);
  //
  console.log(hobo);
  //
  send_post_query(hobo,pypy,parse_response);
  //
  pa.remove();
}
//
function get_daka() {
  let daka = new Date();
  let year = daka.getFullYear();
  let month = daka.getMonth()+1;
  if(month < 10) { month = "0"+month; }
  let day = daka.getDate();
  if(day < 10) { day = "0"+day; }
  let re = year+"."+month+"."+day;
  return(re);
}
//
function get_dade() {
  let daka = new Date();
  daka.setDate(daka.getDate() + 30);
  let year = daka.getFullYear();
  let month = daka.getMonth()+1;
  if(month < 10) { month = "0"+month; }
  let day = daka.getDate();
  if(day < 10) { day = "0"+day; }
  let re = year+"."+month+"."+day;
  return(re);
}
//
async function insert_button_click() {
  let mapa = new Map();
  //
  //alert("hi");
  let ka = "insert";
  //alert(ka);
  //
  let command = ka;
  let id = "0";
  let image = await get_value_of_file_input("image");
  let daka = get_value_of_text_input("daka");
  let dade = get_value_of_text_input("dade");
  //
  mapa.set("command",command);
  mapa.set("id",id);
  mapa.set("image",image);
  mapa.set("daka",daka);
  mapa.set("dade",dade);
  //
  let hobo = Object.fromEntries(mapa);
  //
  console.log(hobo);
  //
  send_post_query(hobo,pypy,parse_response);
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
  //
  mapa.set("command",command);
  //
  let hobo = Object.fromEntries(mapa);
  //
  console.log(hobo);
  //
  send_post_query(hobo,pypy,parse_response);
  //
}
//
function set_dates() {
  let daka = get_daka();
  let dade = get_dade();
  let fa = document.querySelector(".lala.first");
  let dakahe = fa.querySelector(".daka");
  let dadehe = fa.querySelector(".dade");
  dakahe.value = daka;
  dadehe.value = dade;
}
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
let sel_buttons = document.querySelectorAll("button.select");
for(const sel_button of sel_buttons) {
  sel_button.addEventListener("click",select_button_click);
}
//
set_dates();
