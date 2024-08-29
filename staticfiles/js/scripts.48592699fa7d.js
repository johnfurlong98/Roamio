/*!
* Start Bootstrap - Blog Home v5.0.9 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


document.getElementById('like-button').addEventListener('click', function() {
    const url = this.getAttribute('url');
    console.log(this)
    console.log(url)

    fetch(url, {
        method: 'PATCH',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),  // Ensure you send the CSRF token for security
        },
        body: null,  // No body content for the PATCH request
    }).then(response => {
        if (response.ok) {
            alert("Liked")
        } else {
            alert("Unable to like")
        }
    }).catch(error => console.error('Error:', error));
});

// Function to get CSRF token from cookies
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
