document.addEventListener('DOMContentLoaded', function () {
  console.log('JavaScript подключен');
  tippy('.form-group', {
      content: 'Введите ваши данные для входа',
      placement: 'top',
      animation: 'fade',
  });
});
