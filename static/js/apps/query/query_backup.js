/* Yihang Zhao @ 2016.11.12
 * Query: Advance searching and editing of Data Models 
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

//CSRF Protection: csrf token insert
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(function() {
    $('#btn_backup').click(function(e) {
        $.ajax({
            type: "POST",
            url: "/query/backup-date/",
            data: $(this).serialize(),

            success: function(resp) {
                    $("#backup_error").text(resp);
                    $("#backup_error").show()
            },

            error: function() {
                    $("#backup_error").text('Unknown server error.');
                    $("#backup_error").show()
            }
        });
    });

    $('#restore_form').submit(function(e) {
        $.ajax({
            type: "POST",
            url: "/query/restore-date/",
            data: $(this).serialize(),
            
            success: function(resp) {
                    $("#restore_error").text(resp);
                    $("#restore_error").show()
            },

            error: function() {
                    $("#register_error").text('Unknown server error.');
                    $("#register_error").show()
            }
        });        

        return false;
    });
});
