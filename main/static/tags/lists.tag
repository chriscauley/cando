<lists>
  <h4>Choose a Task List <i class="fa fa-edit right-icon click" onclick={ toggleEdit }></i></h4>
  <ul class="list-group">
    <li class="list-group-item" each={ items }>
      <div if={ !parent.editMode } class="name click" onclick={ parent.select }>{ name }</div>
      <div if={ parent.editMode }>
        <div class="name" onkeypress={ parent.edit } onblur={ parent.blur } contenteditable="true">{ name }</div>
        <i class="fa fa-close right-icon click" onclick={ parent.destroy }></i>
      </div>
    </li>
    <li class="list-group-item click" onclick={ add }>
      <i class="fa fa-plus"></i> Add Another List</li>
  </ul>
  <script>
    this.items = opts.items
    var that = this;
    that.editMode = false;
    var submit_timer;
    toggleEdit(e) {
      this.editMode = !this.editMode;
    }

    destroy(e) {
      destroyItem(e,that,"list");
    }

    edit(e) {
      return ifPressEnter(e,function(e) { window.saveList(e,that) });
    }


    blur(e) {
      window.saveList(e,that)
    }

    select(e) {
      $.get(
        "/list/"+e.item.id+"/",
        function(data) {
          $("#content").append("<tasks></tasks>");
          $("lists").hide();
          var t = riot.mount('tasks',data);
        },
        "json"
      );
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

    // an example how to filter items on the list
    filter(item) {
      return !item.hidden
    }

    toggle(e) {
      var item = e.item
      item.done = !item.done
      return true
    }
  </script>

</lists>
