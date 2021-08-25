var ajax;

odoo.define('web_viseducat', function (require) {
  "use strict";
  ajax = require('web.ajax');
  
});








// Nav elements

//const navToggle = document.querySelector(".nav-toggle");
//const links = document.querySelector("#wrapper-nav-ul");

// Tab elements

const btns = document.querySelectorAll(".tab-btn");
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

const tabList = document.querySelectorAll(".tab-btn")
const articles = document.querySelectorAll(".cd-content");
var currentIndex = 0
tabList.forEach(function(button, index){

  button.addEventListener('click', (event)=>{
    tabList[currentIndex].classList.remove('active')
    articles[currentIndex].classList.remove('active')
    event.target.classList.toggle("active")
    articles[index].classList.add("active")
    currentIndex = index
      

    
    
  })
  
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



const replyButtons = document.querySelectorAll(".reply-comment")
const wrapperComment = document.querySelectorAll(".wrapper-comment")
const ellipsisButtons = document.querySelectorAll(".ellipsis")
const editDeleteMenu = document.querySelectorAll(".delete-edit")
const editBtn = document.querySelectorAll(".edit")
const updateForm = document.querySelectorAll(".update-answer")
const responseForm = document.querySelectorAll(".answered-comment")
const cancelButton = document.querySelectorAll(".cancel-cmnt")
const replyTextAreas = document.querySelectorAll(".answer-reply-cont")
const updatePostBtn = document.querySelectorAll(".update-post-btn")
const updatedTextArea = document.querySelectorAll("#update-textarea")
const updateCancelBtn = document.querySelectorAll(".update-cancel-btn")
const deleteBtn = document.querySelectorAll(".delete")






for (let i = 0; i < wrapperComment.length; i++) {

  replyButtons[i].addEventListener('click', ()=>{
    replyTextAreas[i].classList.toggle("active")
  })

  cancelButton[i].addEventListener('click', ()=>{
    replyTextAreas[i].classList.toggle("active")
  })

  const siblingList = wrapperComment[i].nextElementSibling
  if (siblingList.classList.contains("answered-comment")){
    replyButtons[i].style.display = "none"
  }

}

// these for comment-reply events

for (let index = 0; index < editBtn.length; index++) {

  ellipsisButtons[index].addEventListener('click', ()=>{
    editDeleteMenu[index].classList.toggle("active")
  })

  editBtn[index].addEventListener('click', ()=>{
    updateForm[index].classList.toggle("active")
    responseForm[index].classList.toggle("deactive")
  })

  updateCancelBtn[index].addEventListener('click', ()=>{
    updateForm[index].classList.remove("active")
    responseForm[index].classList.toggle("active")
    editDeleteMenu[index].classList.remove("active")

  })
  deleteBtn[index].addEventListener('click', ()=>{
    const commentID = deleteBtn[index].getAttribute('data-id').split('/')[1]
    deleteByAjax(commentID, index)
  })

  updatePostBtn[index].addEventListener('click', ()=>{
    const commentID = deleteBtn[index].getAttribute('data-id').split('/')[1]
    const updateText = updatedTextArea[index].value
    editByAjax(commentID, updateText, index)

  })
  
}





















function deleteByAjax(id,index) {
  const params = {
    'id': id
  }

  const url = '/delete'

  ajax.jsonRpc(url, 'call', params).then(function (data) {

    if (data.result){
      responseForm[index].classList.toggle("deactive")
      replyButtons[index].style.display = "block"
    }
    else{
      console.log("An error occured!!!")
    }

  }).catch(function (ex) {

    console.log("ex: " + ex)


  });
}


function editByAjax(id,text, index) {
  const params = {
    'id': id,
    'text': text,
  }

  const url = '/edit'

  ajax.jsonRpc(url, 'call', params).then(function (data) {

    if (data.result){
      console.log("successful!!!")
      const updateDate = new Date()
      responseForm[index].getElementsByClassName("published-time")[0].textContent = "Updated on " +updateDate.toLocaleString()
      responseForm[index].getElementsByClassName("comment-area")[0].textContent = text
      updateForm[index].classList.remove("active")
      responseForm[index].classList.toggle("active")
      editDeleteMenu[index].classList.remove("active")
    }
    else{
      console.log("An error occured!!!")
    }

  }).catch(function (ex) {

    console.log("ex: " + ex)


  });
}


