document.addEventListener("DOMContentLoaded", function() {
  const addTodoButton = document.getElementById("add-todo");
  if (addTodoButton) {
    addTodoButton.addEventListener("click", function() {
      const newTodoNameInput = document.getElementById("new-todo-name");
      const newTodoStatusInput = document.getElementById("new-todo-status");
      const newTodoDeadlineInput = document.getElementById("new-todo-deadline");

      const newTodoName = newTodoNameInput.value.trim();
      const newTodoStatus = newTodoStatusInput.value;
      const newTodoDeadline = newTodoDeadlineInput.value;

      if (newTodoName === "") {
        alert("TODOを入力してください");
        return;
      }

      // タスクをオブジェクトとして保存
      let todoList = JSON.parse(localStorage.getItem("todoList")) || [];
      const newTodo = { name: newTodoName, status: newTodoStatus, deadline: newTodoDeadline };
      todoList.push(newTodo);
      localStorage.setItem("todoList", JSON.stringify(todoList));

      // デバッグ用
      console.log("Saved Todo List:", todoList);

      // 入力フィールドをクリア
      newTodoNameInput.value = "";
      newTodoDeadlineInput.value = "";

      //リストを更新
      if (window.displayTodoList) {
        window.displayTodoList();
      }

      alert("TODOが追加されました！");
    });
  } else {
    console.error("Error: Add Todo button not found.");
  }
});
