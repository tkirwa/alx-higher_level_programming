$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').keypress(function (e) {
    if (e.which === 13) {
      translate();
    }
  });
});

function translate () {
  const url = 'https://hellosalut.stefanbohacek.dev/hello/';
  const langCode = $('INPUT#language_code').val();

  $.get(`${url}?lang=${langCode}`, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
