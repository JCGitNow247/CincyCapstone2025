window.addEventListener('DOMContentLoaded', loadAnalyticsData);

const money = n => `$${Number(n || 0).toFixed(2)}`;
const dateLabel = s => (s || '').slice(0, 10);

async function loadAnalyticsData() {
  try {
    const res = await fetch(GetSiteHost() + '/get-analytics-summary');
    const data = await res.json();

    const byDay = data.sales_by_day ?? [];
    const payTypes = data.payment_breakdown ?? [];
    const payroll = data.payroll ?? [];

    const wrapper = document.querySelector('.analytics-wrapper');
    if (!wrapper) return;

    wrapper.innerHTML = `
      <h2>Total Sales: ${money(data.total_sales)}</h2>
      <div>Average Sale: <span>${money(data.average_sale)}</span></div>
      <div><strong>Sales This Week:</strong> <span>${money(data.sales_this_week)}</span></div>
      <div>Same Week Last Year: <span>${money(data.same_week_last_year)}</span></div>

      <div class="analytics-grid">
        <div>
          <h3>Last 7 Days</h3>
          <div class="analytics-inner-box">
            ${byDay.map(r => `<p>${dateLabel(r.sale_date)}: ${money(r.amount)}</p>`).join('')}
          </div>
        </div>
        <div>
          <h3>Sales by Payment Type</h3>
          <div class="analytics-inner-box">
            ${payTypes.map(p => `<p>${p.type}: ${money(p.total)}</p>`).join('')}
          </div>
        </div>
      </div>

      <h3>Total Hours Worked: ${Number(data.total_hours || 0)} hrs</h3>
      <div><strong>Repeat Customers:</strong> ${Number(data.repeat_customers || 0)}</div>

      <h3>Employee Payroll</h3>
      <div class="payroll">
        ${payroll.map(e => {
          const hrs = Number(e.hours || 0), rate = Number(e.rate || 0);
          return `${e.name}: ${hrs} hrs @ ${money(rate)} = ${money(hrs * rate)}`;
        }).join('<br>')}
      </div>
    `;
  } catch (err) {
    console.error('Analytics error:', err);
  }
}