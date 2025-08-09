let selectedBaseItem = null;

function OpenModificationMenu(itemName, itemPrice) {
    // Fetch modifiers first (don’t open the menu yet)
    fetch(`http://localhost:5000/get-modifiers?item=${encodeURIComponent(itemName)}`)
        .then(res => res.json())
        .then(modifiers => {
            // No modifiers? Just add item and bail.
            if (!Array.isArray(modifiers) || modifiers.length === 0) {
                AddToCart(itemName, itemPrice);
                // Optional: briefly open/close the cart to make it obvious something was added
                // ToggleMenu('.Cart-Menu', 'Cart-overlay'); setTimeout(() => ToggleMenu('.Cart-Menu','Cart-overlay'), 400);
                return;
            }

            // We have modifiers — build the menu like before
            selectedBaseItem = { name: itemName, price: itemPrice };

            const optionGrid = document.querySelector('.Modification-Menu .option-grid');
            const bottomButtons = document.querySelector('.Modification-Menu .Bottom-Menu-Buttons');

            if (!optionGrid || !bottomButtons) {
                console.error("Missing .option-grid or .Bottom-Menu-Buttons inside .Modification-Menu!");
                return;
            }

            // Clear and render options
            optionGrid.innerHTML = '';
            modifiers.forEach(mod => {
                const label = document.createElement('label');
                label.className = 'option-box';
                label.innerHTML = `
                    <input type="checkbox" name="mod" value="${mod.name}" data-price="${mod.price}"/>
                    <span>${mod.name}</span><br>
                    <small>$${Number(mod.price).toFixed(2)}</small>
                `;
                optionGrid.appendChild(label);
            });

            // Build bottom buttons
            bottomButtons.innerHTML = '';
            const closeBtn = document.createElement('button');
            closeBtn.type = 'button';
            closeBtn.textContent = 'Close';
            closeBtn.onclick = () => ToggleMenu('.Modification-Menu', 'Modification-overlay');

            const addBtn = document.createElement('button');
            addBtn.type = 'button';
            addBtn.textContent = 'Add To Cart';
            addBtn.onclick = () => {
                if (selectedBaseItem) {
                    AddToCart(selectedBaseItem.name, selectedBaseItem.price);
                    ToggleMenu('.Modification-Menu', 'Modification-overlay');
                }
            };

            bottomButtons.appendChild(closeBtn);
            bottomButtons.appendChild(addBtn);

            // Finally open the menu (only when we know there are options)
            ToggleMenu('.Modification-Menu', 'Modification-overlay');
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

    // Create the outer container
    const cartItem = document.createElement('div');
    cartItem.className = 'Cart-Item';
    cartItem.setAttribute('data-price', itemTotal.toFixed(2)); // store price

    // Create the delete button
    const button = document.createElement('button')
    const img = document.createElement('img');
    img.src = "../assets/images/TrashIcon.png";
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

        // Extract item name from <strong>
        const nameMatch = html.match(/<strong>(.*?)<\/strong>/);
        const name = nameMatch ? nameMatch[1] : "Unnamed Item";

        // Extract modifiers from HTML
        const modifierMatches = [...html.matchAll(/\+ (.*?)<br>?/g)];
        const modifiers = modifierMatches.map(m => m[1]);

        savedItems.push({
            name,
            modifiers,
            html,
            price
        });
    });

    localStorage.setItem('cartItems', JSON.stringify(savedItems));
}

// Restores the cart data for the user so they see it in their cart. 
function restoreCartFromStorage() {
    const savedItems = JSON.parse(localStorage.getItem('cartItems') || "[]");
    const cartGrid = document.querySelector('.Cart-Item-Grid');

    if (!cartGrid) {
        console.warn("No .Cart-Item-Grid found - skipping cart restore")
        return;
    }

    savedItems.forEach(({ html, price }) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'Cart-Item';

        const button = document.createElement('button');
        const img = document.createElement('img');
        img.src = "../assets/images/TrashIcon.png";
        img.alt = 'TrashIcon';
        button.appendChild(img);

        button.addEventListener('click', () => {
            cartItem.remove();
            updateCartCount();
            SaveCartToStorage();
            updateTotalPrice();
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
        .then(r => r.json())
        .then(menuItems => {
            const container = document.querySelector('.menu-container');

            menuItems.forEach(item => {
                const card = document.createElement('div');
                card.className = 'menu-card';

                // --- DRINKS: always show "Add Drinks" and skip modifier check (your exception) ---
                if (item.name === "Drinks") {
                    card.innerHTML = `
                        <h2>${item.name}</h2>
                        <p>${item.description}</p>
                        <button type="button" onclick='OpenModificationMenu(${JSON.stringify(item.name)}, ${item.price})'>Add Drinks</button><br>
                    `;
                    container.appendChild(card);
                    return; // done with this card
                }

                // Base content for non-drinks
                let baseHTML = `
                    <h2>${item.name}</h2>
                    <p>${item.description}</p>
                    <p>$${item.price.toFixed(2)}</p>
                `;

                // --- NON-DRINKS: check if the item has modifiers ---
                fetch(`http://localhost:5000/get-modifiers?item=${encodeURIComponent(item.name)}`)
                    .then(res => res.json())
                    .then(modifiers => {
                        // Build the right buttons based on whether modifiers exist
                        if (Array.isArray(modifiers) && modifiers.length > 0) {
                            // Has modifiers → show Modify + Add to Cart

                        baseHTML += `
                            <button type="button" onclick='OpenModificationMenu(${JSON.stringify(item.name)}, ${item.price})'>Modify Item</button><br>
                            <button type="button" onclick='AddToCart(${JSON.stringify(item.name)}, ${item.price})'>Add To Cart</button>
                        `;
                        } else {
                            // No modifiers → only Add to Cart
                            baseHTML += `
                                <button type="button" onclick='AddToCart(${JSON.stringify(item.name)}, ${item.price})'>Add To Cart</button>
                            `;
                        }

                        card.innerHTML = baseHTML;
                        container.appendChild(card);
                    })
                    .catch(err => {
                        console.error(`Error checking modifiers for ${item.name}:`, err);
                        // Fallback: just show Add To Cart
                        baseHTML += `
                            <button type="button" onclick='AddToCart(${JSON.stringify(item.name)}, ${item.price})'>Add To Cart</button>
                        `;
                        card.innerHTML = baseHTML;
                        container.appendChild(card);
                    });
            });
        })
        .catch(err => console.error("Error fetching menu data", err));
}

// Recalculates and updates the total cart price.
// Updates both the displayed price on screen and the value in localStorage.
function updateTotalPrice() {
    const items = document.querySelectorAll('.Cart-Item');
    let total = 0;

     // Sum up all prices stored in the cart item data attributes
    items.forEach(item => {
        const price = parseFloat(item.getAttribute('data-price')) || 0;
        total += price;
    });

    // Save the updated total to localStorage
    localStorage.setItem("cartTotal", total.toFixed(2));

    // Update all elements labeled as .Total with the new price
    const totalLabels = document.querySelectorAll('.Total label');
    totalLabels.forEach(totalLabel => {
        if (totalLabel) {
            totalLabel.textContent = `Total: $${total.toFixed(2)}`;
        }
    })
}

// If on the OrderPage, load the menu cards
if (document.querySelector('.menu-container')){
    LoadMenuCards();
}
// Restore cart items from localStorage if any exist
restoreCartFromStorage();

// Setup delete buttons and logic for all cart items
SetupCartItemDeletion();