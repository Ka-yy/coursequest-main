document.addEventListener('DOMContentLoaded', function() {
    // Initialize course carousel
    new Glide('.featured-courses .glide', {
        type: 'carousel',
        startAt: 0,
        perView: 3,
        focusAt: 'center',
        gap: 20,
        breakpoints: {
            1024: {
                perView: 2
            },
            600: {
                perView: 1
            }
        },
        autoplay: 4000,
        hoverpause: true
    }).mount();

    // Add interactivity to course cards
    const courseCards = document.querySelectorAll('.course-card');
    
    courseCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('card-hover');
        });

        card.addEventListener('mouseleave', function() {
            this.classList.remove('card-hover');
        });
    });
});