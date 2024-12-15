document.addEventListener('DOMContentLoaded', function() {
    // Add interactive hover effects to school cards
    const schoolCards = document.querySelectorAll('.school-card');
    
    schoolCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.classList.add('hover-effect');
        });

        card.addEventListener('mouseleave', function() {
            this.classList.remove('hover-effect');
        });

        // Optional: Add click interaction to explore school
        card.addEventListener('click', function() {
            const schoolId = this.dataset.schoolId;
            window.location.href = `/schools/${schoolId}/`;
        });
    });

    // Optional: Search/Filter functionality for schools
    const searchInput = document.getElementById('school-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.toLowerCase();
            schoolCards.forEach(card => {
                const schoolName = card.querySelector('h3').textContent.toLowerCase();
                card.style.display = schoolName.includes(searchTerm) ? 'block' : 'none';
            });
        });
    }
});