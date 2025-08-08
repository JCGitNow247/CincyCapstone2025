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

// Adds the selected truck name from localStorage to the page header.
// If the label doesn't exist yet, it creates and appends it to the .Top-Buttons div.
function AddFoodTruckTitleName() {
    const name = localStorage.getItem("selectedTruckName");
    if (name) {
        let label = document.getElementById("foodTruckNameLabel");
        if (!label) {
            label = document.createElement("label");
            label.id = "foodTruckNameLabel";
            document.querySelector(".Top-Buttons")?.appendChild(label);
        }
        label.textContent = name;
    }
}

// Fetches the list of available food trucks from the backend and populates the dropdown menu.
function BuildTruckList() {
    fetch('http://localhost:5000/get-trucks')
        .then(response => response.json())
        .then(trucks => {
            const dropdown = document.getElementById('foodTruckDropdown');
            if (!dropdown) return;

            trucks.forEach(truck => {
                const option = document.createElement('option');
                option.value = truck.id;
                option.textContent = truck.name;
                dropdown.appendChild(option);
            });
        })
        .catch(err => console.error("Error loading trucks:", err));
}

// Retrieves the customer's phone number and email from the checkout form.
// If either field is empty, it shows an alert and returns null.
// Otherwise, it returns an object containing the phone and email.
function GetCustomerInformation() {
    const phone = document.getElementById("phone")?.value.trim();
    const email = document.getElementById("email")?.value.trim();

    if (!phone || !email) {
        alert("Phone number and email are required.");
        return null;
    }

    return { phone, email };
}

// Loads the active orders from the backend and displays them on the screen.
// Orders already marked as "completed" in localStorage will be skipped.
function LoadActiveOrders() {
    fetch('http://localhost:5000/get-active-orders')
        .then(res => res.json())
        .then(orders => {
            const completed = JSON.parse(localStorage.getItem("completedOrders") || "[]");
            const container = document.querySelector('.active-order-container');
            if (!container) return;

            container.innerHTML = '';

            orders.forEach(order => {
                if (completed.includes(order.id)) return; // Skip completed

                const card = document.createElement('div');
                card.className = 'order-card';

                const timeText = order.time ? `<p>Placed: ${new Date(order.time).toLocaleTimeString()}</p>` : '';

                card.innerHTML = `
                    <h2> #${order.id} </h2>
                    <p>${order.description || ''}</p>
                    <p>${timeText}</p>
                `;

                const completeBtn = document.createElement('button');
                completeBtn.textContent = 'Complete Order';
                completeBtn.addEventListener('click', () => {
                    card.remove();
                    const updatedCompleted = [...completed, order.id];
                    localStorage.setItem("completedOrders", JSON.stringify(updatedCompleted));
                });

                card.appendChild(completeBtn);
                container.appendChild(card);
            });
        })
        .catch(err => console.error("Failed to load active orders:", err));
}


function displayOrders(orders) {
    const container = document.querySelector('.active-order-container');
    container.innerHTML = ""; // Clear previous orders

    orders.forEach(order => {
        const orderDiv = document.createElement('div');
        orderDiv.className = 'order-card';

        // Start building order HTML
        let orderHTML = `<h3>Order #${order.order_id}</h3>`;

        // Render each item individually — no grouping!
        order.items.forEach(item => {
            orderHTML += `<p><strong>${item.item_name}</strong></p>`;
            if (item.foods.length > 0) {
                orderHTML += `<ul>`;
                item.foods.forEach(food => {
                    orderHTML += `<li>${food}</li>`;
                });
                orderHTML += `</ul>`;
            }
        });

        orderDiv.innerHTML = orderHTML;

        // Add Complete Order button
        const button = document.createElement('button');
        button.innerText = 'Complete Order';
        button.onclick = () => completeOrder(order.order_id);
        orderDiv.appendChild(button);

        container.appendChild(orderDiv);
    });
}

// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

// Makes GetCustomerInformation and BuildTruckList available globally for inline HTML scripts.
window.GetCustomerInformation = GetCustomerInformation;
window.BuildTruckList = BuildTruckList;