document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('post-job-form');
    const startDateInput = document.getElementById('id_start_date');
    const dueDateInput = document.getElementById('id_due_date');
    const startDateError = document.getElementById('start-date-error');
    const dueDateError = document.getElementById('due-date-error');

    form.addEventListener('submit', function (event) {
        let valid = true;
        startDateError.innerHTML = '';
        dueDateError.innerHTML = '';

        if (!startDateInput.value) {
            valid = false;
            startDateError.innerHTML = 'Please select a start date.';
        }

        if (!dueDateInput.value) {
            valid = false;
            dueDateError.innerHTML = 'Please select a due date.';
        }

        if (!valid) {
            event.preventDefault();
        }
    });
});

