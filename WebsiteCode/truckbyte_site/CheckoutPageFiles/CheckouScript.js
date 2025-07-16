function loadCartFromStorage() {
    const cartGrid = document.querySelector('.Cart-Item-Grid');
    const savedItems = JSON.parse(localStorage.getItem('cart')) || [];

    savedItems.forEach(itemName => {
        const cartItem = document.createElement('div');
        cartItem.className = 'Cart-Item';

        const span = document.createElement('span');
        span.textContent = itemName;

        cartItem.appendChild(span);
        cartItem.appendChild(cartItem);
    });
}

function restoreCartFromStorage() {
    const savedItems = JSON.parse(localStorage.getItem('cart')) || [];
    savedItems.forEach(name => AddToCart(name));
}

window.addEventListener('DOMContentLoaded', loadCartFromStorage);



restoreCartFromStorage();