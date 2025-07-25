function handleCheckout(event) {
    event.preventDefault(); // Prevent form refresh
    
    const baseTotal = parseFloat(localStorage.getItem("cartTotal")) || 0;
    let tipAmount = handleTip(baseTotal);

    const inputs = document.querySelectorAll('#CheckoutForm input[type="text"]');
    for (let input of inputs) {
        if (input.value.trim() === "") {
            alert("Please fill out all required fields.");
            return;
        }
    }

    const finalTotal = (baseTotal + tipAmount).toFixed(2);
    localStorage.setItem("finalTotal", finalTotal);

    localStorage.setItem("orderConfirmed", "true");

    //console.log("The base total is: ", baseTotal) for testing
    //console.log("The tip amount is: ", tipAmount) for testing

    window.location.href = "summary.html" // Redirect
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
    summaryHTML += `</ul><p><strong>Total Paid:</strong> $${finalTotal}</p>`;

    summaryDiv.innerHTML = summaryHTML;

    localStorage.removeItem("cartItems");
}

window.addEventListener('DOMContentLoaded', () => {
    showOrderSummary();
});