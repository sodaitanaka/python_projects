function deleteTodo(index) {
  let todoList = JSON.parse(localStorage.getItem("todoList")) || [];
  todoList.splice(index, 1);
  localStorage.setItem("todoList", JSON.stringify(todoList));

  //リストを更新
  if (window.displayTodoList) {
    window.displayTodoList();
  }
}
