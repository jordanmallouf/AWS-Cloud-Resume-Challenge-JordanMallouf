const apiUrl = 'https://ln4bofmpuk.execute-api.us-east-1.amazonaws.com/prod/visitor-counter';

async function fetchVisitorCount() {
    try {
        const response = await fetch(apiUrl);
        const data = await response.json();

        // Update the visitor count on the page
        document.getElementById('visitor-count').innerText = data.views;
    } catch (error) {
        console.error('Error fetching visitor count:', error);
        document.getElementById('visitor-count').innerText = 'N/A'; // Fallback display
    }
}

// Fetch the visitor count on page load
document.addEventListener('DOMContentLoaded', fetchVisitorCount);
