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

// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}

window.GetCustomerInformation = GetCustomerInformation;
window.BuildTruckList = BuildTruckList;