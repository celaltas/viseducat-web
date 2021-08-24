// Nav elements

//const navToggle = document.querySelector(".nav-toggle");
//const links = document.querySelector("#wrapper-nav-ul");

// Tab elements

const btns = document.querySelectorAll(".tab-btn");
const articles = document.querySelectorAll(".cd-content");
const courseDetails = document.querySelector("#course-details-article");




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



courseDetails.addEventListener("click", function (e) {
  const id = e.target.dataset.id;

  if (id) {

    // remove active from other buttons

    btns.forEach(function (btn) {
      btn.classList.remove("active");
      e.target.classList.add("active");
    })

    // hide other articles

    articles.forEach(function (article) {
      article.classList.remove("active");
    })
    const element = document.getElementById(id);
    element.classList.add("active");
  }
})

// Course Content

const allContent = document.querySelector("#course-content-schedule")

const childrenList = allContent.children






for (let i = 0; i < childrenList.length; i++) {


  if (i % 2 === 0) {


    childrenList[i].addEventListener("click", function () {

      childrenList[i + 1].classList.toggle("active-table")

      const plus = childrenList[i].firstElementChild.firstElementChild
      const minus = childrenList[i].firstElementChild.firstElementChild.nextSibling.nextSibling



      plus.classList.toggle("deactive-plus")
      minus.classList.toggle("active-minus")










    })


  }
}

// Visible and Employee Only

const vebtns = document.querySelectorAll(".visible")


vebtns.forEach(function (vebtn) {

  vebtn.addEventListener("click", function () {



    if (vebtn.style.backgroundColor != "red") {
      vebtn.style.backgroundColor = "red"
      vebtn.style.width = "auto"
      vebtn.textContent = "Employees Only"
    }



    else {
      vebtn.textContent = "Visible"
      vebtn.style.backgroundColor = "green"


    }



  })



})


// Reply Comment


const replyButtons = document.querySelectorAll(".reply-comment")
const cancelButtons = document.querySelectorAll(".cancel-cmnt")
const ellipsisButtons = document.querySelectorAll(".ellipsis")
const editDelete = document.querySelectorAll(".delete-edit")



for (let i = 0; i < replyButtons.length; i++) {





  const replyTextAreas = replyButtons[i].parentElement.parentElement.nextElementSibling


  if (replyTextAreas.classList[1] === "answered-comment") {
    replyButtons[i].style.display = "none"
  }

  replyButtons[i].addEventListener("click", function (event) {

    identify = event.target.id

    if (identify === replyTextAreas.id) {
      replyTextAreas.classList.toggle("active")
    }






    cancelButtons[i].addEventListener("click", function () {

      replyTextAreas.classList.toggle("active")

    })
  })
  if (replyTextAreas.classList[1] === "answered-comment")
    ellipsisButtons[i].addEventListener("click", function () {

      editDelete[i].classList.toggle("active-flex")

    })



}








odoo.define('web_viseducat', function (require) {
  "use strict";

  const ajax = require('web.ajax');
  const deleteBtn = document.querySelector(".delete")
  const editBtn = document.querySelector(".edit")
  const replyID = deleteBtn.getAttribute('data-id').split('/')[1]
  deleteBtn.addEventListener('click', deleteByAjax)
  editBtn.addEventListener('click', editByAjax)
  


  function deleteByAjax() {
    console.log("delete butonu tıklandı")
    const params = {
      'id': replyID
    }
    
    const url = '/delete'
  
    ajax.jsonRpc(url, 'call', params).then(function (data) {
      
      console.log("çağrı yapıldı")
      console.log("data" + data.result)

      if (data.result){
        alert("Divi kapa")
      }
      else{
        alert("Hata")
      }
  
    }).catch(function (ex) {
  
      console.log("ex: " + ex)
  
  
    });
  }

  function editByAjax() {
    console.log("edit butonu tıklandı")
    const params = {
      'id': replyID
    }
    
    const url = '/edit'
  
    ajax.jsonRpc(url, 'call', params).then(function (data) {
      
      console.log("edit çağrı yapıldı")
      console.log("data" + data.content)


    }).catch(function (ex) {
  
      console.log("ex: " + ex)
  
  
    });
  }


});
