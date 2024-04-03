$(document).ready(function() {
  $('body').on('click', '#add_item', function() {
    $('<li>Item</li>').appendTo('.my_list');
  });

  $('body').on('click', '#remove_item', function() {
    $('.my_list li:last-child').remove();
  });

  $('body').on('click', '#clear_list', function() {
    $('.my_list').empty();
  });
});
