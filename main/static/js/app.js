can.Component.extend({
  tag: 'logentry',
  template: can.view('/static/can/logger.html'),
});

_log = (function() {
  var timeout;
  return function(message,className) {
    var entry = can.mustache("<logentry></logentry>")({message: message, className:className});
    $("#todo-wrapper").append(entry);
    clearTimeout(timeout)
    setTimeout(function(){$("logentry").remove()},2000)
  };
})({});

function logSuccess(message) { return function(){ _log(message,"success"); } }
function logError(message) { return function() { _log(message,"error"); } }

var ACTIVE_LIST;
var Todo = can.Model.extend({
  findAll: function(attrs) { return $.get("/list/"+ACTIVE_LIST.id+"/tasks/",attrs,undefined,"json"); },
  findOne: 'GET /task/{id}/',
  update: 'POST /task/{id}/',
  destroy: 'POST /task/delete/{id}/',
  create: function(attrs) { return $.get("/list/"+ACTIVE_LIST.id+"/new/",attrs,undefined,"json"); },
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
    editMode: false,
    toggleEdit: function() {
      console.log(this);
      this.attr("editMode",!this.attr("editMode"));
    },
    select: function(list) {
      ACTIVE_LIST = list;
      console.log('?');
      $("#todo-wrapper").append(can.mustache("<list></list>")({list:ACTIVE_LIST}));
      $("#todo-wrapper tasklists").hide();
    },
    newList: function() {
      var that = this;
      new TaskList({}).save(function(l) {
        that.attr('lists').push(l);
        $("tasklists .list-group-item span").last().click();
        selectEditable($(".list-name")[0]);
      });
    },
    destroyList: function(list) {
      this.lists.removeAttr(this.lists.indexOf(list));
      list.destroy();
    },
  } }
});

$(function() {
  $("#todo-wrapper").append(can.mustache("<tasklists></tasklists>")({}));
});

// from http://stackoverflow.com/a/3866442
function selectEditable(e) {
  var range,selection;
  range = document.createRange();
  range.selectNodeContents(e);
  range.collapse(false);
  selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
}

can.Component.extend({
  tag: 'list',
  template: can.view("/static/can/todo_list.html"),
  scope: function() { return {
    selectedTodo: null,
    todos: new Todo.List({}),
    list: ACTIVE_LIST,
    saveList: function(todo) {
      this.attr('list').save(logSuccess("List saved"));
    },
    select: function(todo) {
      this.attr('selectedTodo', todo);
      $("#todo-edit").focus();
    },
    check: function(todo) {
      todo.attr("complete",!todo.attr("complete"));
      todo.save(logSuccess("Task Completed"));
    },
    saveTodo: function(todo) {
      todo.save();
      this.removeAttr('selectedTodo');
    },
    newTodo: function() {
      var that = this;
      new Todo({}).save(function(t) {
        that.attr("todos").push(t);
        that.attr('selectedTodo', t);
        $("#todo-edit").select();
        logSuccess("todo added")
      });
    },
    destroyTodo: function(todo) {
      this.todos.removeAttr(this.todos.indexOf(todo));
      todo.destroy();
    },
    back: function(todo) {
      $("#todo-wrapper tasklists").show();
      $("#todo-wrapper list").remove();
    }
  }},
  events: {
    "[contenteditable] keypress": function(element,event) {
      if (event.which == 13) {
        var list = this.scope.attr('list');
        list.attr("name",element.text());
        list.save();
        element.blur();
        window.getSelection().removeAllRanges();
        return false;
      }
      return true;
    }
  }
});
