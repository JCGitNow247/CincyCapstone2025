let selectedBaseItem = null;

// Toggles the modification menu on and off
function ToggleMenu(menuSelector, overlayId) {
    const menu = document.querySelector(menuSelector);
    const overlay = document.getElementById(overlayId);
    if (!menu || !overlay) return;

    const isHidden = getComputedStyle(menu).display === 'none'

    //Toggle display
    menu.style.display = isHidden ? 'flex' : 'none';
    overlay.style.display = isHidden ? 'block' : 'none';

        // If closing the menu, clear selected modifiers
    if (!isHidden) {
        const checkboxes = menu.querySelectorAll('input[type="checkbox"]');
        checkboxes.forEach(cb => cb.checked = false);
    }
}

function OpenModificationMenu(itemName, itemPrice) {

    selectedBaseItem = { name: itemName, price: itemPrice}
    // Open the correct menu
    ToggleMenu('.Modification-Menu', 'Modification-overlay');

    // Load modifiers dynamically
    fetch(`http://localhost:5000/get-modifiers?item=${encodeURIComponent(itemName)}`)
        .then(res => res.json())
        .then(modifiers => {
            console.log("Fetched modifiers:", modifiers)
            
            const optionGrid = document.querySelector('.Modification-Menu .option-grid');
            if (!optionGrid) {
                console.error("Missing .option-grid inside .Modification-Menu!");
                return;
            }

            optionGrid.innerHTML = ''; // Clear old options

            modifiers.forEach(mod => {
                const label = document.createElement('label');
                label.className = 'option-box';
                label.innerHTML = `
                    <input type="checkbox" name="mod" value="${mod}" data-price="${mod.price}"/>
                    <span>${mod.name}</span><br>
                    <small>$${mod.price.toFixed(2)}</small>
                `;
                optionGrid.appendChild(label);
            });

            const bottomButtons = document.querySelector('.Modification-Menu .Bottom-Menu-Buttons');
            if (bottomButtons) {
                bottomButtons.innerHTML = '';

                const closeBtn = document.createElement('button');
                closeBtn.type = 'submit';
                closeBtn.textContent = 'Close';
                closeBtn.onclick = () => ToggleMenu('.Modification-Menu', 'Modification-overlay');

                const addBtn = document.createElement('button');
                addBtn.type = 'submit';
                addBtn.textContent = 'Add To Cart';
                addBtn.onclick = () => {
                    if (selectedBaseItem) {
                        AddToCart(selectedBaseItem.name, selectedBaseItem.price);
                        ToggleMenu('.Modification-Menu', 'Modification-overlay');
                    }
                };

                bottomButtons.appendChild(closeBtn);
                bottomButtons.appendChild(addBtn);
            }         
        })
        .catch(err => console.error("Error loading modifiers:", err));
}

// This function will add items to a cart, add an item to a cart once someone has clicked the add button
function AddToCart(baseName = "Item", basePrice = 0) {
    
    const cartGrid = document.querySelector('.Cart-Item-Grid')
    const selectedMods = Array.from(document.querySelectorAll('.option-grid input[type="checkbox"]:checked'))

    let modsHTML = "";
    let modTotal = 0;

    selectedMods.forEach(input => {
        const label = input.closest('label');
        const span = label?.querySelector('span');
        const text = span ? span.textContent.trim() : '';
        const modCost = parseFloat(input.getAttribute('data-price')) || 0;
        modsHTML += `+ ${text}<br>`;
        modTotal += modCost;
    })

    const itemTotal = basePrice + modTotal;

    //Build display name
    let itemText = selectedBaseItem || "Item";
    if (selectedMods.length > 0) {
        const formattedMods = selectedMods.map(mod => `+ ${mod}`).join('<br>');
        itemText += `<br><small>${formattedMods}</small>`;
    }

    // Create the outer container
    const cartItem = document.createElement('div');
    cartItem.className = 'Cart-Item';
    cartItem.setAttribute('data-price', itemTotal.toFixed(2)); // store price

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
        SaveCartToStorage();
        updateTotalPrice();
    });

    // Create the item label
    const span = document.createElement('span');
    span.innerHTML = `<strong>${baseName}</strong><br><small>${modsHTML}</small>`;

    // Append everything together
    cartItem.appendChild(button);
    cartItem.appendChild(span);
    cartGrid.appendChild(cartItem);

    updateCartCount();
    SaveCartToStorage();
    updateTotalPrice(); // recalculate total
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
                updateTotalPrice();
            }
        });
    });

    updateCartCount();
}

// This function will make an array, items that will store the cart data for the user to persist across pages.
function SaveCartToStorage() {
    const items = document.querySelectorAll('.Cart-Item');
    const savedItems = [];

    items.forEach(item => {
        const span = item.querySelector('span');
        const html = span.innerHTML;
        const price = item.getAttribute('data-price');

        savedItems.push({ html, price }); // store both html and price
    });

    localStorage.setItem('cartItems', JSON.stringify(savedItems));
}

// Restores the cart data for the user so they see it in their cart. 
function restoreCartFromStorage() {
    const savedItems = JSON.parse(localStorage.getItem('cartItems') || "[]");
    const cartGrid = document.querySelector('.Cart-Item-Grid');

    savedItems.forEach(({ html, price }) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'Cart-Item';

        const button = document.createElement('button');
        const img = document.createElement('img');
        img.src = "../Images/TrashIcon.png";
        img.alt = 'TrashIcon';
        button.appendChild(img);

        button.addEventListener('click', () => {
            cartItem.remove();
            updateCartCount();
            SaveCartToStorage();
        });

        const span = document.createElement('span');
        span.innerHTML = html;

        cartItem.setAttribute('data-price', parseFloat(price).toFixed(2)); // use stored price

        cartItem.appendChild(button);
        cartItem.appendChild(span);
        cartGrid.appendChild(cartItem);
    });

    updateCartCount();
    updateTotalPrice(); // Add this line

    
}

// Loads the menu cards for the specified food truck.
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
                <button onclick="OpenModificationMenu('${item.name}', ${item.price})">Modify Item</button><br>
                <button onclick="AddToCart('${item.name}', ${item.price})">Add To Cart</button>
            `;

            container.appendChild(card);
        });
    })
    .catch(err => {
        console.error("Error fetching menu data", err)
    });
}

function updateTotalPrice() {
    const items = document.querySelectorAll('.Cart-Item');
    let total = 0;

    items.forEach(item => {
        const price = parseFloat(item.getAttribute('data-price')) || 0;
        total += price;
    });

    const totalLabel = document.querySelector('.Total label');
    if (totalLabel) {
        totalLabel.textContent = `Total: $${total.toFixed(2)}`;
    }
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