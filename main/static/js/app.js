var Todo = can.Model.extend({
  findAll: 'GET /todo/',
  findOne: 'GET /todo/{id}/',
  update: 'POST /todo/{id}/',
  destroy: 'POST /todo/delete/{id}/'
}, {});

can.Component.extend({
  tag: 'todolist',
  template: can.view("/static/can/todo_list.html"),
  scope: {
    selectedTodo: null,
    todos: new Todo.List({}),
    select: function(todo){
      this.attr('selectedTodo', todo);
    },
    save: function(todo) {
      todo.save();
      this.removeAttr('selectedTodo');
    }
  }
})
$(function() {
  $("#todo-wrapper").append(can.mustache("<todolist></todolist>")({}));
});
