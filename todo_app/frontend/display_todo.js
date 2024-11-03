document.addEventListener("DOMContentLoaded", function() {
  const todoListElement = document.getElementById("todo-list");
  let todoList = JSON.parse(localStorage.getItem("todoList")) || [];

  // デバッグ用
  console.log("Loaded Todo List:", todoList);

  function displayTodoList() {
    todoList = JSON.parse(localStorage.getItem("todoList")) || [];
    todoListElement.innerHTML = "";

    todoList.forEach((todo, index) => {
      const row = document.createElement("tr");

      // No
      const noCell = document.createElement("td");
      noCell.textContent = index + 1;
      row.appendChild(noCell);

      // Task Name
      const taskNameCell = document.createElement("td");
      taskNameCell.textContent = todo.name || "(no name)";
      row.appendChild(taskNameCell);

      // Task Status
      const statusCell = document.createElement("td");
      statusCell.textContent = todo.status || "(no status)";
      row.appendChild(statusCell);

      // Deadline
      const deadlineCell = document.createElement("td");
      deadlineCell.textContent = todo.deadline || "(no deadline)";
      row.appendChild(deadlineCell);

      // Delete Button
      const deleteCell = document.createElement("td");
      const deleteButton = document.createElement("button");
      deleteButton.innerHTML = "✗";
      deleteButton.classList.add("delete-button");
      deleteButton.addEventListener("click", function() {
        deleteTodo(index);
      });
      deleteCell.appendChild(deleteButton);
      row.appendChild(deleteCell);
      todoListElement.appendChild(row);
    });
  }

  //グローバル関数として登録
  window.displayTodoList = displayTodoList;

  displayTodoList();
});
