// Toggles the modification menu on and off
function ToggleMenu(menuSelector, overlayId) {
    const menu = document.querySelector(menuSelector);
    const overlay = document.getElementById(overlayId);
    if (!menu || !overlay) return;

    const isHidden = getComputedStyle(menu).display === 'none'

    //Toggle display
    menu.style.display = isHidden ? 'flex' : 'none';
    overlay.style.display = isHidden ? 'block' : 'none';
}

// This function will add items to a cart, add an item to a cart once someone has clicked the add button
function AddToCart(ItemText = "Item In Cart") {
    
    const cartGrid = document.querySelector('.Cart-Item-Grid')

    // Create the outer container
    const cartItem = document.createElement('div');
    cartItem.className = 'Cart-Item';

    // Create the delete button
    const button = document.createElement('button')
    const img = document.createElement('img');
    img.src = "../Images/TrashIcon.png";
    img.alt = 'TrashIcon';
    button.appendChild(img);

    //Add delete functionality
    button.addEventListener('click', () => {
        //console.log("Clicked")
        cartItem.remove();
        updateCartCount();

    });

    // Create the item label
    const span = document.createElement('span');
    span.textContent = ItemText;

    // Append everything together
    cartItem.appendChild(button);
    cartItem.appendChild(span);
    cartGrid.appendChild(cartItem);

    updateCartCount();
    SaveCartToStorage();

};

// This function updates the count for how many items are currently inside the cart.
function updateCartCount() {
    const headerCartButton = document.querySelector('#headerCartButton');
    const cartItem = document.querySelectorAll('.Cart-Item');
    const itemCount = cartItem.length;

    if (headerCartButton) {
        //console.log("Updated")
        headerCartButton.textContent = `Cart (${itemCount})`;
    }
}

// This function will make an array, items that will store the cart data for the user to persist across pages.
function SaveCartToStorage() {
    const items = Array.from(document.querySelectorAll('.Cart-Item span')).map(span => span.textContent);
    localStorage.setItem('cart', JSON.stringify(items));
}

// This is a setup function for if someone already has something inside their cart that they want saved.
function SetupCartItemDeletion() {
    const cartItem = document.querySelectorAll('.Cart-Item');
    const headerCartButton = document.querySelector('#headerCartButton');

    if (cartItem.length === 0) {
        console.log("Cart is empty");
        return;
    }

    document.querySelectorAll('.Cart-Item button').forEach(button => {
        button.addEventListener('click', function () {
            console.log("Clicked")
            const cartItem = this.closest('.Cart-Item');
            if (cartItem) {
                cartItem.remove();
                updateCartCount();
                SaveCartToStorage();
            }
        });
    });

    updateCartCount();
}

// Restores the cart data for the user so they see it in their cart. 
function restoreCartFromStorage() {
    const savedItems = JSON.parse(localStorage.getItem('cart')) || [];
    savedItems.forEach(name => AddToCart(name));
}

// Loadts the menu cards for the specified food truck.
function LoadMenuCards() {
    fetch('http://localhost:5000/get-menu')
    .then(response => response.json())
    .then(menuItems => {
        const container = document.querySelector('.menu-container');

        menuItems.forEach(item => {
            const card = document.createElement('div');
            card.className = 'menu-card';

            card.innerHTML = `
                <h2> ${item.name} </h2>
                <p>
                    ${item.description}
                </p>
                <p> $${item.price} </p>
                <button onclick="ToggleMenu('.Modification-Menu', 'Modification-overlay')">Modify Item</button><br>
                <button onclick="AddToCart('${item.name}')">Add To Cart</button>
            `;

            container.appendChild(card);
        });
    })
    .catch(err => {
        console.error("Error fetching menu data", err)
    });
}

// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

if (document.querySelector('.menu-container')){
    LoadMenuCards();
}
restoreCartFromStorage();
SetupCartItemDeletion();