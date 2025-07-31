async function submitEmployeeLogin() {
    const username = document.getElementById('employeeUsername').value.trim();
    const password = document.getElementById('employeePassword').value.trim();

    if (!username || !password) {
        alert("Please enter your credentials.");
        return;
    }

    const res = await fetch("http://localhost:5000/login-employee", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.success) {
        localStorage.setItem("employeeRole", data.role.toLowerCase());
        localStorage.setItem("employeeID", data.employeeID);

        if (data.role.toLowerCase() === "manager") {
            window.location.href = "ManagerEmployeePage/ManagerEmployeePage.html";
        } else {
            window.location.href = "EmployeePage/EmployeePage.html";
        }
    } else {
        alert("Invalid credentials.");
    }
}
