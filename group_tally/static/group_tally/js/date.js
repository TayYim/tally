// ref:http://ghmagical.com/article/page/id/unacjkHzT3W0
$(function() {
  Date.prototype.toDateInputValue = function() {
    var local = new Date(this);
    local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
    return local.toJSON().slice(0, 10);
  };

  $("#date_input").val(new Date().toDateInputValue());
});
