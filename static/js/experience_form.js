document.addEventListener('DOMContentLoaded', function() {
    function validateExperienceForm(form) {
        const startDate = form.querySelector('#id_start_date').value;
        const endDate = form.querySelector('#id_end_date').value;
        let valid = true;

        if (!startDate) {
            form.querySelector('#start-date-error').textContent = 'This field is required.';
            valid = false;
        } else {
            form.querySelector('#start-date-error').textContent = '';
        }

        if (!endDate) {
            form.querySelector('#end-date-error').textContent = 'This field is required.';
            valid = false;
        } else {
            form.querySelector('#end-date-error').textContent = '';
        }

        return valid;
    }

    const addExperienceForms = document.querySelectorAll('#add-experience-form');

    addExperienceForms.forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!validateExperienceForm(form)) {
                event.preventDefault();
            }
        });
    });
});
