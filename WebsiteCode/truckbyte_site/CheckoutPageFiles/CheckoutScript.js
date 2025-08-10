


// Handles the final checkout process:
// - Validates input fields and drink selection
// - Calculates final total including tip
// - Sends the order data to the backend
// - Redirects to summary page if successful
function handleCheckout(event) {
    event.preventDefault(); // Prevent form refresh

    const drinkSelect = document.getElementById('freeDrinkSelect');
    if (drinkSelect && drinkSelect.offsetParent !== null) {
        if (drinkSelect.value === "") {
            alert("Please select a free drink to proceed.");
            return;
        }
        localStorage.setItem("freeDrink", drinkSelect.value); // Save selected drink
    }

    const inputs = document.querySelectorAll('#CheckoutForm input[type="text"]');
    for (let input of inputs) {
        if (input.value.trim() === "") {
            alert("Please fill out all required fields.");
            return;
        }
    }

    // Get the discounted subtotal from the displayed label
    const displayedTotalText = document.querySelector('#CheckoutForm .Total label')?.textContent;
    let discountedSubtotal = parseFloat(localStorage.getItem("cartTotal")) || 0;

    if (displayedTotalText) {
        const match = displayedTotalText.match(/\$([\d.]+)/);
        if (match) {
            discountedSubtotal = parseFloat(match[1]);
        }
    }

    // Apply tip to the discounted subtotal
    const tipAmount = handleTip(discountedSubtotal);
    const finalTotal = (discountedSubtotal + tipAmount).toFixed(2);

    localStorage.setItem("finalTotal", finalTotal);
    localStorage.setItem("orderConfirmed", "true");


    // New section: post order to backend
    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const freeDrink = localStorage.getItem('freeDrink') || null;
    const customerID = localStorage.getItem('customerID') || null;

    const orderPayload = {
        customerID: customerID,
        total: finalTotal, // finalTotal is already calculated
        freeDrink: freeDrink,
        items: cartItems.map(item => ({
            name: item.name || "Unnamed Item",
            modifiers: item.modifiers || [],
            html: item.html || ""
        }))
    };

    console.log("Cart being sent:", JSON.stringify(cartItems, null, 2));

    fetch(GetSiteHost() + "/submit-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(orderPayload)
    })
    .then(res => res.json())
    .then(data => {
        console.log("Order submission result:", data);
        window.location.href = "summary.html"; // redirect AFTER inserting
    })
    .catch(err => {
        alert("There was an issue submitting your order.");
        console.error("Error:", err);
    });
}

// Calculates and returns the tip amount based on selected radio option
function handleTip(baseTotal) {
    // Tip handling
    let tipAmount = 0;
    
    const selectedTip = document.querySelector('input[name="TipOption"]:checked');
    if (selectedTip && selectedTip.value) {
        const percentage = parseFloat(selectedTip.value);
        tipAmount = baseTotal * percentage;
    }

    localStorage.setItem("tipAmount", tipAmount.toFixed(2));
    //console.log("the tip amount is: ", tipAmount)

    return tipAmount
}

// Displays a summary of the order on the summary page using data from localStorage
function showOrderSummary() {
    const summaryDiv = document.getElementById('orderSummary')
    if (!summaryDiv) return; // Only run this on the summary page

    const cartItems = JSON.parse(localStorage.getItem('cartItems')) || [];
    const finalTotal = localStorage.getItem('finalTotal') || "0.00";

    let summaryHTML = "<h2>Order Summary</h2><ul>";
    cartItems.forEach(item => {
        summaryHTML += `<li style="margin-bottom: 5px;">${item.html || item}</li>`;
    });

    const freeDrink = localStorage.getItem("freeDrink");
    if (freeDrink != '') {
        summaryHTML += `<li style="margin-bottom: 5px;"><em>Free Drink: ${freeDrink}</em></li>`;
    }
    summaryHTML += `</ul><p><strong>Total Paid:</strong> $${finalTotal}</p>`;

    summaryDiv.innerHTML = summaryHTML;

    localStorage.removeItem("cartItems");
}

// Checks if the customer already exists in the system and offers to apply loyalty or register
async function checkLoyalty() {
    const customerInformation = GetCustomerInformation();
    if (!customerInformation) return; 

    try {
    const res = await fetch(GetSiteHost() + '/check-customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customerInformation)
    });

    const data = await res.json();

    if (data.exists) {
        if (confirm("Your account is already registered. apply the loyalty reward?")) {
            applyLoyalty();            
        }
    } else {
        if (confirm("Would you like to sign up?")) {
            submitRegistration();        
        }
    }
    } catch (error) {
        console.error("Loyalty check failed:", error);
        alert("Failed to check loyalty status. Please try again later.");
    }
}

// Registers a new customer and immediately applies loyalty if successful
async function submitRegistration() {
    const info = GetCustomerInformation();

    if (!info) {
        alert("Phone number and email are required.");
        return;
    }

    const res = await fetch(GetSiteHost() + '/register-customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(info)
    });

    const result = await res.json();

    if (result.success) {
        alert("Account created successfully!");
        applyLoyalty(); // apply the reward immediately after signup
    } else {
        alert("Failed to create account.");
    }
}

// Retrieves and applies the customer's loyalty reward to the UI and pricing
async function applyLoyalty() {
    const customerInformation = GetCustomerInformation();
    
    if (!customerInformation) return;

    const res = await fetch(GetSiteHost() + "/apply-loyalty", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            strEmail: customerInformation.email,
            strPhoneNumber: customerInformation.phone
        })
    });

    const data = await res.json();

    if (data.success) {
        alert("Loyalty reward applied!");
        localStorage.setItem("customerID", data.customerID);
        localStorage.setItem("loyaltyReward", data.reward || "None");

        const reward = data.reward || "None";
        const rewardDiv = document.getElementById('loyaltyRewardInfo');
        const CheckLoyaltyButton = document.getElementById('LoyaltyButton');
        rewardDiv.style.display = 'block';

        if (reward.includes('%')) {
            rewardDiv.innerHTML = `<div style="text-align: center;"><em>Loyalty Reward: ${reward} discount applied.</em></div>`;
            localStorage.setItem("freeDrink", "")
            applyPercentageDiscount(reward);
            CheckLoyaltyButton.disabled = true;
        } else if (reward.toLowerCase().includes('drink')) {
            rewardDiv.innerHTML = `
                <div class="loyaltyBlock" style="text-align: center; margin-bottom: 30px;">
                    <p><strong>Loyalty Reward:</strong> Free Drink</p>
                    <select id="freeDrinkSelect" required>
                        <option value="" disabled selected>Select a drink</option>
                    </select>
                </div>
            `;
            populateDrinkDropdown();
            CheckLoyaltyButton.disabled = true;
        }
    } else {
        alert("Could not apply loyalty reward.");
    }
}

// Applies a percentage-based discount to the displayed cart total
function applyPercentageDiscount(reward) {
    const percentage = parseFloat(reward.replace('%', ''));

    // Find the label in the checkout form specifically
    const totalLabel = document.querySelector('#CheckoutForm .Total label');

    if (!totalLabel) {
        console.error("Checkout total label not found.");
        return;
    }

    const match = totalLabel.textContent.match(/\$([\d.]+)/);
    if (!match) {
        console.error("Checkout total label format is invalid.");
        return;
    }

    const originalTotal = parseFloat(match[1]);
    const discounted = (originalTotal * (1 - percentage / 100)).toFixed(2);

    totalLabel.textContent = `Total: $${discounted}`;
    localStorage.setItem("finalTotal", discounted);
}

// Fetches available drinks from backend and populates the dropdown for free drink rewards
function populateDrinkDropdown() {
    const select = document.getElementById("freeDrinkSelect");
    if (!select) {
        console.warn("Dropdown not found. Skipping drink population.");
        return;
    }

    fetch(GetSiteHost() + "/get-drinks")
        .then(res => res.json())
        .then(drinks => {
            drinks.forEach(drink => {
                const option = document.createElement("option");
                option.value = drink;
                option.textContent = drink;
                select.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Failed to load drinks:", error);
        });
}

// On page load, show the order summary if on the summary page
window.addEventListener('DOMContentLoaded', () => {
    showOrderSummary();
});