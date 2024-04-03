$(document).ready(function() {
  $('#btn_translate').click(fetchTranslation); // Trigger translation fetch on button click
  $('#language_code').keypress(function(e) {
    if (e.which === 13) { // If Enter key is pressed
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    var languageCode = $('#language_code').val(); // Get the language code entered by the user
    var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.ajax({
      url: apiUrl,
      method: 'GET',
      success: function(data) {
        $('#hello').text(data.hello); // Display the translation in the #hello div
      },
      error: function(error) {
        console.log('Error fetching translation:', error);
      }
    });
  }
});
