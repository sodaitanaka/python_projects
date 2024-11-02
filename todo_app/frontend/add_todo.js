// add_todo.html用のスクリプト
document.addEventListener("DOMContentLoaded", function() {
  // "戻る"ボタンの処理
  const backButton = document.getElementById("back-button");
  if (backButton) {
    backButton.addEventListener("click", function() {
      window.location.href = "index.html";
    });
  } else {
    console.error("Error: back-button element not found.");
  }

  // "追加"ボタンの処理
  const addTodoButton = document.getElementById("add-todo");
  if (addTodoButton) {
    addTodoButton.addEventListener("click", function() {
      const newTodoInput = document.getElementById("new-todo");
      const newTodoText = newTodoInput.value;

      if (newTodoText.trim() === "") {
        alert("TODOを入力してください");
        return;
      }
      let todoList = JSON.parse(localStorage.getItem("todoList")) || [];
      todoList.push(newTodoText);
      localStorage.setItem("todoList", JSON.stringify(todoList));
      newTodoInput.value = "";
      alert("TODOが追加されました！");
    });
  } else {
    console.error("Error: Add Todo button not found.");
  }
});
