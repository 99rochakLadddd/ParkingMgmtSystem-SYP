document.addEventListener('DOMContentLoaded', function() {
    // Fetch the navigation bar HTML
    fetch('navbar.html')
        .then(response => response.text())
        .then(data => {
            // Insert the navigation bar HTML into the placeholder div
            document.getElementById('navbar-placeholder').innerHTML = data;
        });
});

// JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the menu bar icon
    document.getElementById('menu-bar').addEventListener('click', function() {
        // Toggle the 'sidebar-hidden' class on the content side bar
        document.getElementById('content-side-bar').classList.toggle('sidebar-hidden');
    });
});


// js to get to login page after clicking on logout button

document.addEventListener('DOMContentLoaded', function() {
    // Add event listener to the logout icon
    document.querySelector('.profile-menu').addEventListener('click', function() {
        // Show confirmation dialog before logging out
        if (confirm('Bruhh you serious? We dont have forget password option !! 💀')) {
            logout(); // Logout if user confirms
        }
    });
});

// Function to perform logout action
function logout() {
    // Redirect the user to the login page
    window.location.href = '/login'; // Replace '/login' with the actual login URL
}


