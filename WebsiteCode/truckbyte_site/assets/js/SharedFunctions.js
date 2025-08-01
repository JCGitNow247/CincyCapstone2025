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

function GetCustomerInformation() {
    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastName').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();


    if (!firstName) console.error("Missing input: #firstName");
    if (!lastName) console.error("Missing input: #lastName");
    if (!email) console.error("Missing input: #email");   
    if (!phone) console.error("Missing input: #phone");

    if (!firstName || !lastName || !phone || !email) {
        return null;
    }

    return {
        firstName,
        lastName,
        email,
        phone
    };
}

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



// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

window.GetCustomerInformation = GetCustomerInformation;
window.BuildTruckList = BuildTruckList;