
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('menu-bar').addEventListener('click', function() {
        document.getElementById('content-side-bar').classList.toggle('sidebar-hidden');
    });

    
    document.querySelector('.profile-menu').addEventListener('click', function() {
        if (confirm('Are you sure you want to log out?')) {
            window.location.href = '/register';
        }
    });
});






