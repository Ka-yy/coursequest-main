document.addEventListener('DOMContentLoaded', () => {
    // Filter Sidebar Toggle
    const filterToggle = document.querySelector('.filter-toggle');
    const filterSidebar = document.querySelector('.filters-sidebar');
    const exploreContent = document.querySelector('.explore-content');

    filterToggle.addEventListener('click', () => {
        filterSidebar.style.left = filterSidebar.style.left === '0px' ? '-250px' : '0px';
        exploreContent.style.marginLeft = exploreContent.style.marginLeft === '250px' ? '0' : '250px';
    });

    // View Toggle (Grid/List)
    const viewToggleButtons = document.querySelectorAll('.view-toggle button');
    const resultsContainer = document.querySelector('.results-container');

    viewToggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove active class from all buttons
            viewToggleButtons.forEach(btn => btn.classList.remove('active'));
            
            // Add active class to clicked button
            button.classList.add('active');
            
            // Toggle view
            if (button.dataset.view === 'list') {
                resultsContainer.classList.remove('grid-view');
                resultsContainer.classList.add('list-view');
            } else {
                resultsContainer.classList.remove('list-view');
                resultsContainer.classList.add('grid-view');
            }
        });
    });

    // Pagination Interaction
    const prevPageBtn = document.querySelector('.prev-page');
    const nextPageBtn = document.querySelector('.next-page');
    const currentPageSpan = document.querySelector('.current-page');

    let currentPage = 1;

    prevPageBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            updatePagination();
        }
    });

    nextPageBtn.addEventListener('click', () => {
        currentPage++;
        updatePagination();
    });

    function updatePagination() {
        currentPageSpan.textContent = currentPage;
        // Here you would typically make an AJAX call to fetch the next/previous page of results
    }
});