const inputBox = document.getElementById("inputBox");
const addBtn = document.getElementById("addButton");
const toDoList = document.getElementById("List");

addBtn.addEventListener("click", function() {
    const list = document.createElement("li");

    //리스트 표시 함수
    list.innerText = inputBox.value;
    toDoList.appendChild(list);
   
    //한번 눌렀을때 라인 생기게 하는 함수
    list.addEventListener("click", function() {
        list.style.textDecoration = "line-through";
    })
    //리스트 삭제 함수 더블클릭
    list.addEventListener("dblclick", function() {
        toDoList.removeChild(list);
    })
})