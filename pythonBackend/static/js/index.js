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


const cartItems = [];

const cart = document.querySelector('.items__container');


const buttons = document.querySelectorAll('.wine__add-to-cart');
buttons.forEach((button) => {
  button.addEventListener('click', (event) => {

    const buttonClicked = event.target;
    const parent = buttonClicked.parentElement.parentElement;

    const item = document.createElement('div');
    const itemForServer = {};
    item.className = 'item';

    const imgSrc = parent.querySelector('.wine__image').src;
    const img = document.createElement('img');
    img.className = 'item__image';
    img.src = imgSrc;

    const name = parent.querySelector('.wine__name');
    const newName = name.cloneNode(true);
    newName.className = 'item__name';

    const price = parent.querySelector('.wine__price');
    const newPrice = price.cloneNode(true);
    newPrice.className = 'item__price';
    
    item.appendChild(img);
    item.appendChild(newName);
    item.appendChild(newPrice);
    console.log(item);

    cart.appendChild(item);

  });
})