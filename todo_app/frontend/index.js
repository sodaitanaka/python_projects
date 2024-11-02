// index.html用のスクリプト
document.addEventListener("DOMContentLoaded", function() {
  const addTodoButton = document.getElementById("add-todo-button");

  //TODO追加をするスクリプト
  if (addTodoButton) {
    addTodoButton.addEventListener("click", function() {
      window.location.href = "add_todo.html";
    });
  } else {
    console.error("Error: Add Todo button not found.");
  }

  //TODOを読み込み、表示するスクリプト
  const todoListElement = document.getElementById("todo-list");
  const todoList = JSON.parse(localStorage.getItem("todoList")) || [];

  //TODOリストを表示する
function displayTodoList() {
  todoListElement.innerHTML = "";

  todoList.forEach((todo, index) => {
    const listItem = document.createElement("li");
    listItem.textContent = todo;
    const deleteButton = document.createElement("button");
    deleteButton.innerHTML = "✗";
    deleteButton.classList.add("delete-button");
    deleteButton.addEventListener("click", function() {
      deleteTodo(index);
    });
    listItem.appendChild(deleteButton);
    todoListElement.appendChild(listItem);
  });
}

function deleteTodo(index) {
  todoList.splice(index, 1);
  localStorage.setItem("todoList", JSON.stringify(todoList));
  displayTodoList();
}
displayTodoList();
});
