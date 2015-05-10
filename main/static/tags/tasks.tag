<tasks>
  <a onclick={ back } class="back click"><i class="fa fa-caret-square-o-left"></i> Back to lists</a>
  <h2>
    <div class="list-name" contenteditable="true" onkeypress={ pressList } onblur={ blurList }>{ opts.name }</div>
  </h2>
  <ul class="list-group">
    <li class="list-group-item" each={ items }>
      <div onclick={ parent.check } class="click check">
        <i class="fa fa-square" if={ !complete }></i>
        <i class="fa fa-check-square" if={ complete }></i>
      </div>
      <div class={ description: true, done: complete } contenteditable="true"
           onkeypress={ parent.pressTask } onblur={ parent.blurTask }>
        {{description}}</div>
      <i class="fa fa-close right-icon click" onclick={ parent.destroy }></i>
      <i class="fa fa-check right-icon click"></i>
    </li>
    <li class="list-group-item-primary list-group-item click" onclick={ add }>
      <i class="fa fa-plus"></i> Add Another Task</li>
  </ul>

  <script>
    this.items = opts.tasks;
    var that = this;

    check(e) {
      $.post(
        "/task/"+e.item.id+"/",
        {"complete": !e.item.complete},
        function(data) {
          for (var i=0;i<that.items.length;i++) {
            if (that.items[i].id == e.item.id) { that.items[i] = data; }
            that.update();
          }
        },
        "json"
      );
    }

    pressList(e) {
      e.item = opts;
      return ifPressEnter(e,function(e) { window.saveList(e,that) });
    }

    blurList(e) {
      e.item = opts;
      window.saveList(e,that);
    }

    back(e) {
      $("lists").show();
      $("tasks").remove();
    }

    function saveTask(e,that) {
      $.post(
        "/task/"+e.item.id+"/",
        {'description': $(e.target).text() },
        function(data)  {
          for (var i=0;i<that.items.length;i++) {
            if (that.items[i].id == e.item.id) { that.items[i] = data; }
            that.update();
          }
        },
        "json"
      )
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
        "/list/"+opts.id+"/new/",
        function(data) {
          that.items.push(data);
          that.update();
        },
        "json"
      )
    }

  </script>

</tasks>
