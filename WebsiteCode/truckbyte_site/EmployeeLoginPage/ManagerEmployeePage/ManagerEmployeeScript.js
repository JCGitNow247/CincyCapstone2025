async function fetchPaidOrders() {
    try {
        const response = await fetch(GetSiteHost() + '/api/paid-orders');
        const orders = await response.json();
        displayOrders(orders);
    } catch (err) {
        console.error("Failed to fetch orders:", err);
    }
}


async function completeOrder(orderId) {
    try {
        const response = await fetch(GetSiteHost() + '/api/complete-order', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ orderId: orderId }),
        });

        if (response.ok) {
            console.log(`Order ${orderId} marked as completed`);
            fetchPaidOrders(); // Refresh the orders
        } else {
            const errText = await response.text();
            console.error(`Failed to complete order:`, errText);
        }
    } catch (error) {
        console.error("Error completing order:", error);
    }
}

setInterval(fetchPaidOrders, 5000);
fetchPaidOrders();