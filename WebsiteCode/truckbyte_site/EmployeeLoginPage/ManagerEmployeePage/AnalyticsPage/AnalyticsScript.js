window.addEventListener('DOMContentLoaded', loadAnalyticsData);

function loadAnalyticsData() {
    fetch('http://localhost:5000/get-analytics-summary')
        .then(res => res.json())
        .then(data => {
            const wrapper = document.querySelector('.analytics-wrapper');
            if (!wrapper) return;

            wrapper.innerHTML = `
                <h2>Total Sales: $${Number(data.total_sales || 0).toFixed(2)}</h2>
                <div class="analytics-grid>
                    <div>
                        <h3>Sales by Day</h3>
                        <div class="analytics-inner-box">
                            ${data.sales_by_day.map(row => `
                                <p>${row.sale_date}: $${Number(row.amount || 0).toFixed(2)}</p>
                            `).join('')}
                        </div>
                    </div>
                    <div>
                        <h3>Sales by Payment Type</h3>
                        <div class="analytics-inner-box">
                            ${data.payment_breakdown.map(p => `
                                <p>Type ${p.type}: $${Number(p.total || 0).toFixed(2)}</p>
                            `).join('')}
                        </div>
                    </div>
                </div>
                <h3>Total Hours Worked: ${Number(data.total_hours || 0)} hrs</h3>
                <h3>Employee Payroll</h3>
                <div class="payroll">
                ${data.payroll.map(e => {
                    const hours = Number(e.hours || 0);
                    const rate = Number(e.rate || 0);
                    const totalPay = hours * rate;
                    return `${e.name}: ${hours} hrs @ $${rate.toFixed(2)} = $${totalPay.toFixed(2)}<br>`;
                }).join('')}
                </div>
            `;
            
        })
        .catch(err => {
            console.error("Analytics error:", err);
        });
}