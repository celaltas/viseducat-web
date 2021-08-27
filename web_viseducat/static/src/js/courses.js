// // Grid and List view

const gridViewButton=document.querySelector("#grid")
const listViewButton=document.querySelector("#bar")
const gridContainer=document.querySelector(".grid-container")
const listContainer=document.querySelector(".list-container")
const courseTitle=document.querySelectorAll(".grid-course-title").firstElementChild

console.log(courseTitle)


console.log(listContainer)
gridViewButton.addEventListener("click",function(){
  gridViewButton.classList.add("clicked")
  listViewButton.classList.remove("clicked")
  gridContainer.style.display="flex"
  listContainer.style.display="none"
  


})
listViewButton.addEventListener("click",function(){
  gridViewButton.firstElementChild.style.backgroundColor="transparent"
  gridViewButton.classList.remove("clicked")
  listViewButton.classList.add("clicked")
  gridContainer.style.display="none"
  listContainer.style.display="block"
})