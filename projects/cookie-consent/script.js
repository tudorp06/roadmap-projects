
const popup = document.getElementById("popup");
const acceptButton = document.getElementById("accept-btn")
const closeButton = document.getElementById("xbtn");

closeButton.addEventListener("click", () => {
    popup.style.display = "none";
})

acceptButton.addEventListener("click", () =>{
       popup.style.display = "none"; 
       localStorage.setItem("acceptCookies", true);
})


//when the page first loads, we check for saved choice

const cookieChoice = localStorage.getItem("acceptCookies");
if(cookieChoice === "true"){
    popup.style.display = "none";
}