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
    const companyName = localStorage.getItem("selectedCompanyName");
    const label = document.getElementById("foodTruckNameLabel"); // must already exist on page
    if (companyName && label) {
        label.textContent = companyName;
    }
}


// Fetch location from backend-served config.json and populate dropdown (1 entry)
function BuildTruckList() {
    const dropdown = document.getElementById('foodTruckDropdown');
    if (!dropdown) return;

    dropdown.innerHTML = '<option value="" disabled selected>Select a Location</option>';

    fetch(GetSiteHost() + '/config', { cache: 'no-cache' })
        .then(r => { if (!r.ok) throw new Error(`config endpoint failed (${r.status})`); return r.json(); })
        .then(cfg => {
            const company  = cfg?.CompanyPlaceholder || '';
            const location = cfg?.LocationPlaceholder || '';

            localStorage.setItem("selectedCompanyName", company);
            localStorage.setItem("selectedLocationName", location);

            if (location) {
                const opt = document.createElement('option');
                opt.value = location;
                opt.textContent = location;
                dropdown.appendChild(opt);
            }
            // NOTE: no AddFoodTruckTitleName() here
        })
        .catch(err => console.error("Error loading location from config:", err));

        dropdown.onchange = () => {
        const text = dropdown.options[dropdown.selectedIndex]?.textContent || '';
        localStorage.setItem("selectedLocationName", text);
        localStorage.setItem("selectedTruckValue", dropdown.value);
    };
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
    fetch(GetSiteHost() + '/get-active-orders')
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
    const freeDrink = localStorage.getItem('freeDrink') || null;
    
    orders.forEach(order => {
        const orderDiv = document.createElement('div');
        orderDiv.className = 'order-card';
        console.log(freeDrink)

        // Start building order HTML
        let orderHTML = `<h3>Order #${order.order_id}</h3>`;

        // Render each item individually — no grouping!
        order.items.forEach(item => {

            if (item.item_name.toLowerCase() === 'free drink') {
                orderHTML += `<p style="color: green;"><strong>${item.item_name}</strong></p>`;
            } else {
                orderHTML += `<p><strong>${item.item_name}</strong></p>`;
            }

            if (item.foods.length > 0) {
                orderHTML += `<ul>`;
                item.foods.forEach(food => {
                    if (item.item_name.toLowerCase() === 'free drink') {
                        orderHTML += `<li style="color: green;">${food}</li>`;
                    } else {
                        orderHTML += `<li>${food}</li>`;
                    }
                    
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

function GetSiteHost() {
    return 'http://localhost:5000'
}

// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

// Makes GetCustomerInformation and BuildTruckList available globally for inline HTML scripts.
window.GetCustomerInformation = GetCustomerInformation;
window.BuildTruckList = BuildTruckList;
