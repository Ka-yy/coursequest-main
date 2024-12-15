
document.addEventListener('DOMContentLoaded', function() {
    // Initialize both course and school carousels
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

    // Similar initialization for school carousel
    new Glide('.featured-Schools .glide', {
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
});