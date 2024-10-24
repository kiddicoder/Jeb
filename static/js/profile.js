document.getElementById('profile-picture').addEventListener('click', function() {
    document.getElementById('profile_picture').click();
});

document.getElementById('profile_picture').addEventListener('change', function() {
    const form = document.getElementById('profile-picture-form');
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Failed to update profile picture');
        }
    }).then(data => {
        if (data.profile_picture_url) {
            // Update the profile picture on the profile page
            document.getElementById('profile-picture').src = data.profile_picture_url;

            // Update the profile picture in the navbar
            const navbarProfileImage = document.querySelector('.profile-image');
            if (navbarProfileImage) {
                navbarProfileImage.src = data.profile_picture_url;
            }
        } else {
            console.error('Profile picture URL not found in response');
        }
    }).catch(error => {
        console.error(error);
    });
});