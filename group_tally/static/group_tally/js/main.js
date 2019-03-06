$(function() {
  console.log("start");

  function loadTable() {
    $("#record_table").bootstrapTable("refresh", {
      silent: true
    });
  }

  function syncExpense() {
    var url = "/get_expense";
    $.get(url, function(res) {
      if (res.success) {
        $.each(res.items, function(index, item) {
          expense_id = "#" + item.id + "_expense";
          $(expense_id).text(item.expense);
        });
      }
    });
  }

  // submit record
  $("#submit_btn").click(function() {
    var url = "/add_record";
    var name = $("#name_input").val();
    var cost = $("#cost_input").val();
    var members = $("#members").val();

    console.log("in");

    if (members == null) {
      alert("请选择参与人员");
    } else {
      var param = {
        name: name,
        cost: cost,
        members: members
      };

      console.log(param);

      $.post(url, param, function(res) {
        if (res.success) {
          $("#name_input").val("");
          $("#cost_input").val("");
          syncExpense();
          loadTable();
        }
      });
    }
  });

  $("#datetimepicker1").datetimepicker({
    format: "YYYY-MM-DD"
  });
});
