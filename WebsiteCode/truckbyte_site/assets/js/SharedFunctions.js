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

// proceeds to the checkout page.
function ProceedToCheckout() {
  window.location.href = "../CheckoutPageFiles/CheckoutPage.html"
}