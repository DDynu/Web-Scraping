
console.log("helloThere");
let span = document.querySelectorAll("span")
let div = document.querySelectorAll("div")
let img= document.querySelectorAll("img")

for (let i = 0; i < span.length; i++) {
  span[i].style.color = "";
  span[i].style.removeProperty("left");
  span[i].style.removeProperty("top");
  span[i].style.removeProperty("word-spacing");
}

for (let i = 0; i< div.length; i++) {
  div[i].style.removeProperty("color");
  div[i].style.removeProperty("textShadow");
  div[i].style.boxShadow='';
  div[i].style.fontSize='20px';
}

for (let i = 0; i< img.length; i++) {
  img[i].style.opacity = 1;
}
