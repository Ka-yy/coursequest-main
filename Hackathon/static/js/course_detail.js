document.addEventListener('DOMContentLoaded', function() {
    // Add interactive hover effects to class cards
    const classCards = document.querySelectorAll('.class-card');
    
    classCards.forEach(card => {
        card.addEventListener('mouseover', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 15px rgba(0,0,0,0.1)';
        });

        card.addEventListener('mouseout', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
        });

        // Track which class was viewed
        const viewClassButton = card.querySelector('.btn-explore');
        viewClassButton.addEventListener('click', function() {
            const classId = card.getAttribute('data-class-id');
            // Optional: You could add analytics tracking here
            console.log(`Viewing class: ${classId}`);
        });
    });

    // Optional: Handle responsive design for class grid
    function adjustClassGridLayout() {
        const classesGrid = document.querySelector('.classes-grid');
        if (classesGrid) {
            const screenWidth = window.innerWidth;
            if (screenWidth < 600) {
                classesGrid.style.gridTemplateColumns = '1fr';
            } else if (screenWidth < 1024) {
                classesGrid.style.gridTemplateColumns = 'repeat(2, 1fr)';
            } else {
                classesGrid.style.gridTemplateColumns = 'repeat(3, 1fr)';
            }
        }
    }
    
    adjustClassGridLayout();
    window.addEventListener('resize', adjustClassGridLayout);
});