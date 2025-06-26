document.addEventListener('DOMContentLoaded', function() {
    // Your JavaScript code here
    const menu = document.getElementById('menu');
    const sidebar = document.getElementById('sidebar');
    const sidebarlist = sidebar.querySelector('ul')
    const searchbar = document.getElementById('homepage-search-bar')

    menu.addEventListener('mouseover', function() {
        sidebar.style.left = 0;
    });

    sidebar.addEventListener('mouseleave', function() {
        sidebar.style.left = '-250px';

    })
    searchbar.addEventListener('keydown', function(event) {
        if (event.key === "Enter"){
            searchbar.value = ""
        }
    })

    
    })

