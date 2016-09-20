/* cchen @ 2016.09.02
 * User Account Setting JS
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

/*csrf verifying*/
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(function() {
        $(".btn").click(function(){
            this.blur();    //remove focus
        });

        /*submit*/
        $("#pwd_reset").submit(function(){
            pwd = $("[name=npassword]").val();
            cpwd = $("[name=cpassword]").val();
            
            $("#pwd_reset_ok").hide();
            if (pwd == "" || cpwd == "") {
                $("#pwd_reset_error").text("Please input password.")
                $("#pwd_reset_error").show();
                $("#mismatch_error").hide();
            }
            else if (pwd != cpwd) {
                $("[name=cpassword]").val("")
                $("#mismatch_error").show();
            }
            else {
                $("#mismatch_error").hide();
                $.ajax({
                    type:   "POST",
                    url:    "/account-settings/",
                    data:   $("#pwd_reset").serialize(),

                    success:    function(html) {
                        console.log("ab" + $("#pwd_reset").serialize());
                        resp = $.trim(html)
                        if (resp == "OK") {
                            location.reload();
                        }
                        else {
                            $("#pwd_reset_error").text(resp);
                            $("#pwd_reset_error").show();
                        }
                    }

                });
            }           
            return false; 
        });
});
