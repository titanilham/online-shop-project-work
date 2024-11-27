tippy('[data-tippy-content]', {
    theme: 'custom', // Указывает тему из CSS
    animation: 'fade', // Эффект появления
    duration: [300, 200], // Длительность появления и скрытия
    
    
  });


  document.addEventListener("DOMContentLoaded", function() {
    // Обработчик для добавления товара в корзину
    document.querySelectorAll('.add-to-cart-btn').forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault(); 
            const productId = button.getAttribute('data-product-id');  // Получение ID товара
            fetch(`/add-to-cart/${productId}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,  // Получение CSRF-токена
                },
                body: JSON.stringify({ 'product_id': productId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Обновление количества товаров в корзине
                    document.getElementById('cart-count').textContent = data.cart_count;
                }
            });
        });
    });
});
