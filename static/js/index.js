const sandwich = document.querySelector(".sandwich");
const sandwichLinks = document.querySelector(".sandwich__links");


sandwich.addEventListener('click', () => {
    // panel.style.display = 'block';
    // sandwichLinks.style.display = 'flex';
    // sandwichLinks.style.height= 'fit-content';
    // sandwichLinks.style.width = '74vw';
    // sandwichLinks.style.padding = '25px';
    // sandwichLinks.style.opacity = '1';
    if (sandwichLinks.style.display == 'flex') {
        sandwichLinks.style.display = 'none';
    } else {
        sandwichLinks.style.display = 'flex';
    }
    
})
