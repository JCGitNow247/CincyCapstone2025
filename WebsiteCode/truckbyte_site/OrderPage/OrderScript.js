// Toggles the modification menu on and off
function ToggleModificationMenu(button) {
    const menu = document.querySelector('.Modification-Menu');
    const overlay = document.getElementById('overlay');
    if (!menu || !overlay) return;

    const isHidden = getComputedStyle(menu).display === 'none'

    //Toggle display
    if (isHidden) {
        menu.style.display = 'flex' 
        overlay.style.display = 'block'
    } else {
        menu.style.display = 'none'
        overlay.style.display = 'none'
    }
}

function AddToCart() {
    console.log("I was clicked!")
}