  

// Nav elements

//const navToggle = document.querySelector(".nav-toggle");
//const links = document.querySelector("#wrapper-nav-ul");

// Tab elements

const btns=document.querySelectorAll(".tab-btn");
const articles=document.querySelectorAll(".cd-content");
const courseDetails=document.querySelector("#course-details-article");




// NavBar

//navToggle.addEventListener("click", function () {
//  links.classList.toggle("show-links");
//  var visibility = links.style.visibility;
// if(visibility==="visible"){
//  links.style.visibility="hidden";
// }else{
//  links.style.visibility="visible";
// }
//
//});

// Tab


console.log(courseDetails)
courseDetails.addEventListener("click",function(e){
  const id=e.target.dataset.id;

  if(id){
    
    // remove active from other buttons

    btns.forEach(function(btn){
      btn.classList.remove("active");
      e.target.classList.add("active");
    })

    // hide other articles

   articles.forEach(function(article){
     article.classList.remove("active");
   }) 
   const element=document.getElementById(id);
   element.classList.add("active");
  }
})