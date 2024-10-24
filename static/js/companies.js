$(document).ready(function() {
    function performCompanySearch() {
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/companies?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<a href="/companies/${d.id}">
                                <div class="company-card">
                                    <img src="${d.logo_url}" alt="Logo of ${d.name}" class="company-card-logo">
                                    <div class="company-card-name">${d.name}</div>
                                </div>
                            </a>`;
                }).join('');
                $('#company-list').html(newHtml);
            },
            error: function(xhr, status, error) {
                console.error("Failed to fetch companies: ", error);
            }
        });
    }

    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        performCompanySearch();
    });

    $('#search-box').on('keypress', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            performCompanySearch();
        }
    });
});
