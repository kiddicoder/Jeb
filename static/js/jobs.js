$(document).ready(function() {
    // Function to get CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!/^http:.*/.test(settings.url) && !/^https:.*/.test(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Function to convert timestamp to custom timesince format
    function customTimesince(dateString) {
        const date = new Date(dateString);
        const now = new Date();
        const delta = Math.floor((now - date) / 1000);
        const days = Math.floor(delta / 86400);

        if (days < 1) {
            const hours = Math.floor(delta / 3600);
            const minutes = Math.floor((delta % 3600) / 60);
            const seconds = delta % 60;

            if (hours > 0) {
                return `${hours}h ago`;
            } else if (minutes > 0) {
                return `${minutes}m ago`;
            } else {
                return `${seconds}s ago`;
            }
        } else if (days === 1) {
            return "1d ago";
        } else if (days < 7) {
            return `${days}d ago`;
        } else if (days < 30) {
            const weeks = Math.floor(days / 7);
            return `${weeks}w ago`;
        } else if (days < 365) {
            const months = Math.floor(days / 30);
            return `${months}m ago`;
        } else {
            const years = Math.floor(days / 365);
            return `${years}y ago`;
        }
    }

    // General function to fetch filters (categories or companies) from the server and display them in the modal
    function fetchFilters(url, listId) {
        $.ajax({
            url: url,
            type: 'GET',
            success: function(resp) {
                var selectedFilters = $(listId).data('selectedFilters') || [];
                var filterHtml = resp.filters.map(filter => {
                    var selectedClass = selectedFilters.includes(filter.id.toString()) ? 'selected' : '';
                    return `<div class="filter-item ${selectedClass}" data-id="${filter.id}">
                                <span class="icon add"></span>
                                <span class="icon check"></span>
                                <span>${filter.name}</span>
                            </div>`;
                }).join('');
                $(listId).html(filterHtml);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    }

    // Perform search with optional sorting, category, company, applied, and favorites filtering
    function performSearch(sort_by = 'date') {
        var searchText = $('#search-box').val();
        var selectedCategories = $('#category-list .filter-item.selected').map(function() {
            return $(this).data('id');
        }).get().join(',');

        var selectedCompanies = $('#company-list .filter-item.selected').map(function() {
            return $(this).data('id');
        }).get().join(',');

        var appliedFilter = '';
        if ($('#already-applied').is(':checked') && $('#not-applied').is(':checked')) {
            appliedFilter = 'both';
        } else if ($('#already-applied').is(':checked')) {
            appliedFilter = 'applied';
        } else if ($('#not-applied').is(':checked')) {
            appliedFilter = 'not_applied';
        }

        var favoritesFilter = '';
        if ($('#favorites').is(':checked')) {
            favoritesFilter = 'favorites';
        }

        var url = `/jobs?search_filter=${searchText}&sort_by=${sort_by}`;
        if (selectedCategories) {
            url += `&categories=${selectedCategories}`;
        }
        if (selectedCompanies) {
            url += `&companies=${selectedCompanies}`;
        }
        if (appliedFilter) {
            url += `&applied_filter=${appliedFilter}`;
        }
        if (favoritesFilter) {
            url += `&favorites_filter=${favoritesFilter}`;
        }

        $('#category-list').data('selectedFilters', selectedCategories.split(','));
        $('#company-list').data('selectedFilters', selectedCompanies.split(','));

        $.ajax({
            url: url,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<a href="/jobs/${d.id}">
                                <div class="job-card">
                                    <div class="favorite-wrapper">
                                        <input type="checkbox" id="favorite-${d.id}" class="favorite-checkbox" ${d.is_favorited ? 'checked' : ''}/>
                                        <label for="favorite-${d.id}" class="heart-label"></label>
                                    </div>
                                    <div class="job-date">${customTimesince(d.created_at)}</div>
                                    <img src="${d.company_logo}" alt="Logo of ${d.company_name}" class="company-logo">
                                    <div class="job-title">${d.title}</div>
                                    <div class="company-name">${d.company_name}</div>
                                    <div class="due-date">Due date: ${d.due_date}</div>
                                </div>
                            </a>`;
                }).join('');
                $('#jobs-list').html(newHtml);
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    }

    // Event handlers for search and sort functionalities
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        performSearch();
    });

    $('#search-box').on('keypress', function(e) {
        if (e.which == 13) {
            e.preventDefault();
            performSearch();
        }
    });

    $('#sort-by').on('change', function(e) {
        var sortBy = $(this).val();
        performSearch(sortBy);
    });

    // Event handlers for category modal
    $('#category-btn').on('click', function() {
        $('#category-modal').show();
        fetchFilters('/jobs/fetch-categories/', '#category-list');
    });

    $('#apply-category-filter').on('click', function() {
        $('#category-modal').hide();
        performSearch();
    });

    // Event handlers for company modal
    $('#company-btn').on('click', function() {
        $('#company-modal').show();
        fetchFilters('/jobs/fetch-companies/', '#company-list');
    });

    $('#apply-company-filter').on('click', function() {
        $('#company-modal').hide();
        performSearch();
    });

    $('.close').on('click', function() {
        $(this).closest('.modal').hide();
    });

    // Handle filter item selection
    $(document).on('click', '.filter-item', function() {
        $(this).toggleClass('selected');
    });

    // Event handlers for applied/not applied checkboxes
    $('.filter-checkbox').on('change', function() {
        performSearch();
    });

    // Handle favorite toggle
    $(document).on('change', '.favorite-checkbox', function() {
        var jobId = $(this).attr('id').split('-')[1];
        var isChecked = $(this).is(':checked');

        $.ajax({
            url: `/jobs/toggle-favorite/${jobId}/`,
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(resp) {
                if (resp.status === 'added') {
                    console.log(`Job ${jobId} added to favorites.`);
                } else if (resp.status === 'removed') {
                    console.log(`Job ${jobId} removed from favorites.`);
                }
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });

    // Initialize modal display to none
    $('#category-modal').hide();
    $('#company-modal').hide();
});


