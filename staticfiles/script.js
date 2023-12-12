
const init = () =>{

let pageloader = document.querySelector('#overlay');

function loader(){
  if (pageloader) {
  pageloader.remove() 
  }};

window.addEventListener('load', loader)


let menu = document.querySelector('.menu-bars');
let menuBar = document.querySelector('.menu-times');
let nav = document.querySelector('.nav')

const Togglemenuopen =()=>{
menu.classList.add('active');
menuBar.classList.add('active');
nav.classList.add('active')
}

menu.addEventListener('click',Togglemenuopen)

const Togglemenuclose=()=>{
menu.classList.remove('active');
menuBar.classList.remove('active');
nav.classList.remove('active')
}

menuBar.addEventListener('click',Togglemenuclose)

function removeNav(){
 if(window.innerWidth >= 768){
    nav.classList.remove('active');
    menuBar.classList.remove('active');
    menu.classList.remove('active');
   
}

};

window.addEventListener('resize', removeNav);

document.querySelectorAll('.nav-links a').forEach((e) => {
  e.addEventListener('click',() => {
    nav.classList.remove('active')
     menu.classList.remove('active');
    menuBar.classList.remove('active');
})
});

}

window.addEventListener('DOMContentLoaded', init)