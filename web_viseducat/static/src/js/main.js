  

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

// Course Content

const allContent=document.querySelector("#course-content-schedule")

const childrenList=allContent.children






for (let i=0;i<childrenList.length;i++){


  if (i%2===0){
    

    childrenList[i].addEventListener("click",function(){

      childrenList[i+1].classList.toggle("active-table")

      const plus=childrenList[i].firstElementChild.firstElementChild
      const minus=childrenList[i].firstElementChild.firstElementChild.nextSibling.nextSibling



      plus.classList.toggle("deactive-plus")
      minus.classList.toggle("active-minus")










    })


  }
}

// Visible and Employee Only

const vebtns=document.querySelector(".visible")



vebtns.addEventListener("click",function(){

  

    if(vebtns.style.backgroundColor!="red"){   
    vebtns.style.backgroundColor="red"
    vebtns.style.width="auto"
    vebtns.textContent="Employees Only"
  }

 

    else{
      vebtns.textContent="Visible"
      vebtns.style.backgroundColor="green"


    }



})
  

// Reply Comment

const replyButton=document.querySelector(".reply-comment")
const replyTextArea=document.querySelector(".answer-reply-cont")


replyButton.addEventListener("click",function(){

    replyTextArea.classList.toggle("active")




})

// Reply Comment Cancel Button

const cancelButton=document.querySelector(".cancel-cmnt")

cancelButton.addEventListener("click",function(){

  replyTextArea.classList.toggle("active")
})
