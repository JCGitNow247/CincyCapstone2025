//window.addEventListener('DOMContentLoaded', LoadActiveOrders);


async function fetchPaidOrders() {
    try {
        const response = await fetch('http://localhost:5000/api/paid-orders');
        const orders = await response.json();
        displayOrders(orders);
    } catch (err) {
        console.error("Failed to fetch orders:", err);
    }
}


async function completeOrder(orderId) {
    try {
        const response = await fetch('http://localhost:5000/api/complete-order', {
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


function displayOrders(orders) {
    const container = document.querySelector('.active-order-container');
    container.innerHTML = ""; // Clear previous orders

    orders.forEach(order => {
        const orderDiv = document.createElement('div');
        orderDiv.className = 'order-card';

        // Start building order HTML
        let orderHTML = `<h3>Order #${order.order_id}</h3>`;

        // Group items by item_name
        const groupedItems = {};

        order.items.forEach(item => {
            if (!groupedItems[item.item_name]) {
                groupedItems[item.item_name] = [];
            }
            groupedItems[item.item_name].push(...item.foods);
        });

        // Render grouped items
        for (const [itemName, foods] of Object.entries(groupedItems)) {
            orderHTML += `<p><strong>${itemName}</strong></p>`;
            if (foods.length > 0) {
                orderHTML += `<ul>`;
                foods.forEach(food => {
                    orderHTML += `<li>${food}</li>`;
                });
                orderHTML += `</ul>`;
            }
        }

        orderDiv.innerHTML = orderHTML;

        // Add Complete Order button
        const button = document.createElement('button');
        button.innerText = 'Complete Order';
        button.onclick = () => completeOrder(order.order_id);
        orderDiv.appendChild(button);

        container.appendChild(orderDiv);
    });
}


setInterval(fetchPaidOrders, 5000);
fetchPaidOrders();