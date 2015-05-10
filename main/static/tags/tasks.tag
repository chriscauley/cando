<tasks>
  <a onclick={ back } class="back click"><i class="fa fa-caret-square-o-left"></i> Back to lists</a>
  <h2>
    { opts.name }
    <div class="list-name" contenteditable="true" onkeypress={ pressList } onblur={ blurList }></div>
  </h2>
  <ul class="list-group">
    <li class="list-group-item" each={ items }>
      <div onclick={ check } class="check">
        <i class="fa fa-square" if={ !complete }></i>
        <i class="fa fa-check-square" if={ complete }></i>
      </div>
      <div class={ description: true, done: complete } contenteditable="true" onkeypress={ press } onblur={ save }>
        {{description}}</div>
      <i class="fa fa-close right-icon" onclick={ destroy }></i>
      <i class="fa fa-check right-icon"></i>
    </li>
    <li class="list-group-item-primary list-group-item" onclick={ add }>
      <i class="fa fa-plus"></i> Add Another Task</li>
  </ul>

  <script>
    this.items = opts.tasks;
    var that = this;

    check(e) {
      $.post(
        "/task/"+e.item.id+"/",
        {"complete": true},
        function(data) { console.log(data) },
        "json"
      );
    }

    pressList(e) {
      return ifPressEnter(e,function(e) { window.saveList(e,that) });
    }

    blurList(e) {
      window.saveList(e,that);
    }

    back(e) {
      $("lists").show();
      $("tasks").remove();
    }

    function saveTask(e,that) {
      
    }

    pressTask(e) {
      return ifPressEnter(e,function(e) { saveTask(e,that) });
    }

    blurTask(e) {
      saveTask(e,that);
    }

    destroy(e) {
      destroyItem(e,that,"task");
    }

    add(e) {
      $.post(
        "/list/new/",
        function(data) {
          that.items.push(data);
          that.update();
        },
        "json"
      )
    }

  </script>

</tasks>
