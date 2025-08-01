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
        items: cartItems,
        total: finalTotal,
        customerID,
        freeDrink
    };

    fetch("http://localhost:5000/submit-order", {
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
    if (freeDrink) {
        summaryHTML += `<li style="margin-bottom: 5px;"><em>Free Drink: ${freeDrink}</em></li>`;
    }
    summaryHTML += `</ul><p><strong>Total Paid:</strong> $${finalTotal}</p>`;

    summaryDiv.innerHTML = summaryHTML;

    localStorage.removeItem("cartItems");
}

function validateLoyalty() {

    const customerInformation = GetCustomerInformation();

    if (!customerInformation) {
        return false;
    }  

    return true
}

async function checkLoyalty() {
    let validation = validateLoyalty();
    if (!validation) return;

    const customerInformation = GetCustomerInformation();
    

    const res = await fetch('http://localhost:5000/check-customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(customerInformation)
    });

    const data = await res.json();

    if (data.exists) {
        ToggleMenu('#Login', 'LoginBlock-overlay');
    } else {
        if (confirm("Would you like to sign up?")) {
            ToggleMenu('#Register', 'RegisterBlock-overlay');            
        } else {
            return;
        }
        
    }
}


async function submitRegistration() {
    const info = GetCustomerInformation();
    const username = document.getElementById('newUsername').value.trim();
    const password = document.getElementById('newPassword').value.trim();

    if (!username || !password) {
        alert("Username and password are required.");
        return;
    }

    const payload = {
        ...info,
        username,
        password
    };

    const res = await fetch('http://localhost:5000/register-customer', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });

    const result = await res.json();

    if (result.success) {
        alert("Account created successfully!");
        ToggleMenu('#Register', 'RegisterBlock-overlay');
    } else {
        alert("Failed to create account.");
    }
}

async function submitLogin() {
    const username = document.getElementById('loginUsername').value.trim();
    const password = document.getElementById('loginPassword').value.trim();

    if (!username || !password) {
        alert("Please enter your login credentials.");
        return;
    }

    const res = await fetch("http://localhost:5000/login-customer", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.success) {
        alert("Login successful!");
        ToggleMenu('#Login', 'LoginBlock-overlay');
        localStorage.setItem("customerID", data.customerID);
        localStorage.setItem("loyaltyReward", data.reward || "None");

        const reward = data.reward || "None";
        const rewardDiv = document.getElementById('loyaltyRewardInfo');
        rewardDiv.style.display = 'block';

        if (reward.includes('%')) {
            rewardDiv.innerHTML = `<div style="text-align: center;"><em>Loyalty Reward: ${reward} discount applied.</em></div>`;
            applyPercentageDiscount(reward);
        } else if (reward.toLowerCase().includes('drink')) {
            rewardDiv.innerHTML = `
                <div class="loyaltyBlock" style="text-align: center; margin-bottom: 30px;">
                    <p><strong>Loyalty Reward:</strong> Free Drink</p>
                    <select id="freeDrinkSelect" required>
                        <option value="" disabled selected>Select a drink</option>
                    </select>
                </div>
            `;
        }
        populateDrinkDropdown();  // Fetch drinks from backend
    } else {
        alert("Login failed. Invalid username or password.");
    }
}

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

function populateDrinkDropdown() {
    const select = document.getElementById("freeDrinkSelect");
    if (!select) {
        console.warn("Dropdown not found. Skipping drink population.");
        return;
    }

    fetch("http://localhost:5000/get-drinks")
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

window.addEventListener('DOMContentLoaded', () => {
    showOrderSummary();
});