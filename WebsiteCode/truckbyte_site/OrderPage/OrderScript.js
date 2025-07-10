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

        //Stored Procedures?

    });

    // Create the item label
    const span = document.createElement('span');
    span.textContent = ItemText;



    // Append everything together
    cartItem.appendChild(button);
    cartItem.appendChild(span);
    cartGrid.appendChild(cartItem);

    updateCartCount();

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

// This is a setup function for if someone already has something inside their cart that they want saved.
function SetupCartItemDeletion() {
    const cartItem = document.querySelectorAll('.Cart-Item');

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

                //Stored Procedures?
            }
        });
    });
}

function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

SetupCartItemDeletion();