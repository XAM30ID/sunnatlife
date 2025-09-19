const nav_button = document.getElementById("header__nab-btn");
const main_header_nav = document.getElementById('header__nav-items')
console.log('OK');

nav_button.addEventListener('click', () => {
    main_header_nav.classList.add('header__nav-items_active');
});


document.addEventListener('click', (e) => {
    if (!main_header_nav.contains(e.target) && !(e.target === nav_button)) {
        main_header_nav.classList.remove('header__nav-items_active')
    };
});