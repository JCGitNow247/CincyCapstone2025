// Handles login for an employee by sending their credentials to the backend.
// Redirects the user to the appropriate page based on their role.
async function submitEmployeeLogin() {
    // Get and trim input values
    const username = document.getElementById('employeeUsername').value.trim();
    const password = document.getElementById('employeePassword').value.trim();

    // Validate fields are not empty
    if (!username || !password) {
        alert("Please enter your credentials.");
        return;
    }

    // Send login request to backend
    const res = await fetch("http://localhost:5000/login-employee", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.success) {
        // Store login info in localStorage
        localStorage.setItem("employeeRole", data.role.toLowerCase());
        localStorage.setItem("employeeID", data.employeeID);

        // Redirect based on employee role
        if (data.role.toLowerCase() === "manager") {
            window.location.href = "ManagerEmployeePage/ManagerEmployeePage.html";
        } else {
            window.location.href = "EmployeePage/EmployeePage.html";
        }
    } else {
        // Invalid credentials
        alert("Invalid credentials.");
    }
}

