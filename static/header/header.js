const hamburgerMenu = document.getElementById("hamburger")
const navMenu = document.querySelector("header div.container nav")

hamburgerMenu.addEventListener("click", ()=>{

    if(!hamburgerMenu.classList.contains("toggled")){
        navMenu.classList.add("toggled")
        hamburgerMenu.classList.add("toggled")
    }else{
        hamburgerMenu.classList.remove("toggled")
        navMenu.classList.remove("toggled")
    }
})