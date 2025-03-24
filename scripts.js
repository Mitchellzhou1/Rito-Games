const carousel = document.querySelector('.carousel');
const prevButton = document.querySelector('.carousel-nav.prev');
const nextButton = document.querySelector('.carousel-nav.next');
const items = document.querySelectorAll('.carousel-item');
let currentIndex = 0;

function moveCarousel() {
    const itemWidth = items[0].offsetWidth;
    const offset = -(currentIndex * itemWidth); // Move by one item at a time
    carousel.style.transform = `translateX(${offset}px)`;
}

function updateCarousel(direction) {
    const totalItems = items.length;

    if (direction === 'next') {
        currentIndex = (currentIndex + 1) % totalItems; // Move to the next item
    } else if (direction === 'prev') {
        currentIndex = (currentIndex - 1 + totalItems) % totalItems; // Move to the previous item
    }

    // Handle wrapping around the carousel
    if (currentIndex + 2 >= totalItems) {
        // If near the end, clone the first few items and append them to the end
        const overflow = currentIndex + 2 - totalItems + 1;
        carousel.appendChild(items[0].cloneNode(true));
        carousel.appendChild(items[1].cloneNode(true));
        moveCarousel();

        // After the transition, remove the cloned items and reset the carousel
        setTimeout(() => {
            carousel.style.transition = 'none'; // Disable transition for instant reset
            carousel.removeChild(carousel.lastChild);
            carousel.removeChild(carousel.lastChild);
            currentIndex = 0; // Reset to the start
            moveCarousel();
            setTimeout(() => {
                carousel.style.transition = 'transform 0.5s ease-in-out'; // Re-enable transition
            }, 50);
        }, 500);
    } else if (currentIndex === 0) {
        // If at the start, clone the last few items and prepend them to the beginning
        carousel.insertBefore(items[totalItems - 1].cloneNode(true), carousel.firstChild);
        carousel.insertBefore(items[totalItems - 2].cloneNode(true), carousel.firstChild);
        moveCarousel();

        // After the transition, remove the cloned items and reset the carousel
        setTimeout(() => {
            carousel.style.transition = 'none'; // Disable transition for instant reset
            carousel.removeChild(carousel.firstChild);
            carousel.removeChild(carousel.firstChild);
            currentIndex = totalItems - 3; // Reset to the end
            moveCarousel();
            setTimeout(() => {
                carousel.style.transition = 'transform 0.5s ease-in-out'; // Re-enable transition
            }, 50);
        }, 500);
    } else {
        moveCarousel();
    }
}

prevButton.addEventListener('click', () => {
    updateCarousel('prev');
});

nextButton.addEventListener('click', () => {
    updateCarousel('next');
});

window.addEventListener('load', () => {
    moveCarousel(); // Initialize the carousel
});