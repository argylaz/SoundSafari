document.addEventListener("DOMContentLoaded", function() {
    // Bio editing
    const bioElement = document.querySelector('.bio-content');
    bioElement.addEventListener('blur', function() {
        const newBio = this.innerText;
        fetch('/path/to/update_bio/', { // Update this URL
            method: 'POST',
            body: JSON.stringify({'bio': newBio}),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Ensure you have a function to get CSRF token
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    // Function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
