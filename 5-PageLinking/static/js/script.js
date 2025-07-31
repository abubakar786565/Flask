// Mobile Navigation Toggle
document.getElementById('mobileToggle').addEventListener('click', function() {
    document.getElementById('navLinks').classList.toggle('active');
});

// Search Functionality
document.getElementById('searchBtn').addEventListener('click', performSearch);
document.getElementById('searchInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        performSearch();
    }
});

function performSearch() {
    const query = document.getElementById('searchInput').value.trim();
    if (query) {
        // In a real app, you would redirect to a search results page
        alert(`Searching for: ${query}`);
        document.getElementById('searchInput').value = '';
    }
}

// Real-time search
document.getElementById('searchInput').addEventListener('input', function() {
    const query = this.value.trim();
    const resultsContainer = document.getElementById('searchResults');
    
    if (query.length > 2) {
        fetch(`/search?q=${query}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    let html = '';
                    data.forEach(item => {
                        html += `
                            <div class="result-item" onclick="window.location.href='${item.url}'">
                                <h4>${item.title}</h4>
                                <p>${item.type}</p>
                            </div>
                        `;
                    });
                    resultsContainer.innerHTML = html;
                    resultsContainer.style.display = 'block';
                } else {
                    resultsContainer.innerHTML = '<div class="result-item">No results found</div>';
                    resultsContainer.style.display = 'block';
                }
            });
    } else {
        resultsContainer.style.display = 'none';
    }
});

// Close flash messages
document.querySelectorAll('.close-flash').forEach(button => {
    button.addEventListener('click', function() {
        this.parentElement.style.display = 'none';
    });
});

// FAQ Accordion
document.querySelectorAll('.faq-question').forEach(question => {
    question.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        const isActive = this.classList.contains('active');
        
        // Close all FAQ items
        document.querySelectorAll('.faq-question').forEach(q => {
            q.classList.remove('active');
            q.nextElementSibling.style.maxHeight = null;
            q.nextElementSibling.style.padding = '0 25px';
        });
        
        // Open current if it was closed
        if (!isActive) {
            this.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + 'px';
            answer.style.padding = '0 25px 25px';
        }
    });
});

// Testimonial slider
let currentTestimonial = 0;
const testimonials = document.querySelectorAll('.testimonial');

function showTestimonial(index) {
    testimonials.forEach(testimonial => testimonial.style.display = 'none');
    testimonials[index].style.display = 'block';
}

// Auto-rotate testimonials
setInterval(() => {
    currentTestimonial = (currentTestimonial + 1) % testimonials.length;
    showTestimonial(currentTestimonial);
}, 5000);

// Initialize first testimonial
showTestimonial(0);

// Close search results when clicking outside
document.addEventListener('click', function(e) {
    if (!e.target.closest('.search-box')) {
        document.getElementById('searchResults').style.display = 'none';
    }
});

// Animation on scroll
function animateOnScroll() {
    const elements = document.querySelectorAll('.feature-card, .post-card, .value-card, .team-member');
    
    elements.forEach(element => {
        const elementPosition = element.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (elementPosition < screenPosition) {
            element.classList.add('animate__animated', 'animate__fadeInUp');
        }
    });
}

window.addEventListener('scroll', animateOnScroll);
// Initial check
animateOnScroll();