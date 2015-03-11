var Todo = can.Model.extend({
  findAll: 'GET /todo/',
  findOne: 'GET /todo/{id}/',
  update: 'POST /todo/{id}/',
  destroy: 'POST /todo/delete/{id}/',
  create: 'POST /todo/new/',
}, {});

can.Component.extend({
  tag: 'todolist',
  template: can.view("/static/can/todo_list.html"),
  scope: {
    selectedTodo: null,
    todos: new Todo.List({}),
    select: function(todo){
      this.attr('selectedTodo', todo);
      $("#todo-edit").focus();
    },
    saveTodo: function(todo) {
      todo.save();
      this.removeAttr('selectedTodo');
    },
    newTodo: function() {
      var that = this;
      new Todo({}).save(function(t) {
        todos = that.attr("todos").push(t);
        that.attr("selectedTodo",t);
      });
    },
    destroyTodo: function(todo) {
      this.todos.removeAttr(this.todos.indexOf(todo));
      todo.destroy();
    },
  }
})
$(function() {
  $("#todo-wrapper").append(can.mustache("<todolist></todolist>")({}));
});
