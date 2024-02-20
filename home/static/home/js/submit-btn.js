document.addEventListener("DOMContentLoaded", () =>{
    const btn = document.getElementById("send")
    // background-color: transparent; outline: 1px solid black; color: black; text-shadow: initial;
    const propsValues = [{background: "white",
                         outline: "1px solid black",
                         color: "black",
                         textShadow: "initial"},

                         {background: "black",
                         color: "white",
                         outline: "1px solid transparent"}]
    
    const propsAnimations = {
        duration: 1900,
        fill: "backwards",
        direction: "alternate"
    }

    btn.addEventListener("click", () =>{
        btn.animate(propsValues, propsAnimations)
    })
})