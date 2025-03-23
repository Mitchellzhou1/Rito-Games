document.addEventListener('DOMContentLoaded', () => {
    const games = [
        {
            name: 'League of Legends',
            description: 'A fast-paced, competitive online game.',
            image: 'images/league-of-legends.jpg',
            link: 'https://www.leagueoflegends.com'
        },
        {
            name: 'VALORANT',
            description: 'A tactical first-person shooter.',
            image: 'images/valorant.jpg',
            link: 'https://www.riotgames.com/en/games/valorant'
        },
        {
            name: 'Aicles',
            description: 'An immersive role-playing game set in a mystical world.',
            image: 'images/arcane-chronicles.jpg',
           
::contentReference[oaicite:2]{index=2}

 const prevButton = document.querySelector('.carousel-nav.prev');
const nextButton = document.querySelector('.carousel-nav.next');
const carousel = document.querySelector('.carousel');
let currentIndex = 0;

function moveCarousel() {
    const totalItems = document.querySelectorAll('.carousel-item').length;
    const itemWidth = document.querySelector('.carousel-item').offsetWidth;
    const offset = -(currentIndex * itemWidth);

    carousel.style.transform = `translateX(${offset}px)`;
}

prevButton.addEventListener('click', () => {
    const totalItems = document.querySelectorAll('.carousel-item').length;
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = totalItems - 1; // Loop back to last item
    }
    moveCarousel();
});

nextButton.addEventListener('click', () => {
    const totalItems = document.querySelectorAll('.carousel-item').length;
    if (currentIndex < totalItems - 1) {
        currentIndex++;
    } else {
        currentIndex = 0; // Loop back to first item
    }
    moveCarousel();
});


