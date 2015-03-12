var ACTIVE_LIST;
var Todo = can.Model.extend({
  findAll: function(attrs) { return $.get("/list/"+ACTIVE_LIST+"/tasks/",attrs,undefined,"json"); },
  findOne: 'GET /task/{id}/',
  update: 'POST /task/{id}/',
  destroy: 'POST /task/delete/{id}/',
  create: function(attrs) { return $.get("/list/"+ACTIVE_LIST+"/new/",attrs,undefined,"json"); },
}, {});

var TaskList = can.Model.extend({
  findAll: 'GET /list/',
  findOne: 'GET /list/{id}/',
  update: 'POST /list/{id}/',
  destroy: 'POST /list/delete/{id}/',
  create: 'POST /list/new/',
}, {});

can.Component.extend({
  tag: 'tasklists',
  template: can.view("/static/can/tasklist.html"),
  scope: function() { return {
    selectedList: null,
    lists: new TaskList.List({}),
    select: function(list) {
      ACTIVE_LIST = list.id;
      $("#todo-wrapper").append(can.mustache("<list list_id='1'></list>")({}));
    },
    newList: function() {
      var that = this;
      new TaskList({}).save(function(l) {
        that.attr('lists').push(l);
        that.attr('selectedList', l);
        $("#list-edit").select()
      });
    }
  } }
});

$(function() {
  $("#todo-wrapper").append(can.mustache("<tasklists></tasklists>")({}));
});

can.Component.extend({
  tag: 'list',
  template: can.view("/static/can/todo_list.html"),
  scope: function() { return {
    selectedTodo: null,
    todos: new Todo.List({}),
    select: function(todo){
      this.attr('selectedTodo', todo);
      $("#todo-edit").focus();
    },
    check: function(todo) {
      todo.attr("complete",!todo.attr("complete"));
      todo.save();
    },
    saveTodo: function(todo) {
      todo.save();
      this.removeAttr('selectedTodo');
    },
    newTodo: function() {
      var that = this;
      console.log(this);
      new Todo({}).save(function(t) {
        that.attr("todos").push(t);
        that.attr('selectedTodo', t);
        $("#todo-edit").select();
      });
    },
    destroyTodo: function(todo) {
      this.todos.removeAttr(this.todos.indexOf(todo));
      todo.destroy();
    },
  }}
})

