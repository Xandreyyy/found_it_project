document.addEventListener("DOMContentLoaded", () =>{
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

    const root = document.querySelector(":root")
    const headerHeight = document.querySelector("body > header").offsetHeight
    root.style.setProperty("--header-height", `${headerHeight}px`)
})