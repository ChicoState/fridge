$(document).ready(function() {
    $(".increment-btn").click(function(e) {
        e.preventDefault();
        var inc_value = $(this).closest(".row").find(".qty-input").val();
        var value = parseInt(inc_value);
        value = isNaN(value) ? 0 : value; {
            value++;
            var itemId = $(this).parent().data("id");
            var inc_value = $(this).closest(".row").find(".qty-input").val(value);
            updateItemQuantity(itemId, value); // This will request server to update quantity in DB
        }
    });
    $(".decrement-btn").click(function(e) {
        e.preventDefault();
        var inc_value = $(this).closest(".row").find(".qty-input").val();
        var value = parseInt(inc_value);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            var inc_value = $(this).closest(".row").find(".qty-input").val(value);
            var itemId = $(this).parent().data("id");
            updateItemQuantity(itemId, value); // This will request server to update quantity in DB
        }
    });

    // This event will trigger when value is manually changed and editing is done
    // not called when increment|decrement button is pressed
    $(".itemQuantity").change(function() {
        var element = $(this);
        var quantity = parseInt(element.val());
        if (quantity && quantity >= 0) {
            var itemId = element.parent().data("id");
            updateItemQuantity(itemId, quantity);
        }
    });

});

async function updateItemQuantity(id, quantity) {
    var url = `/update-quantity/${id}/`;
    var form = new FormData();
    form.append("quantity", quantity);
    const response = await fetch(url, {
        method: "POST",
        headers: {
            Accept: "application/json",
            "X-CSRFTOKEN": getCookie("csrftoken"),
        },
        body: form,
    });

    //   if (response.ok) {
    //     // At this point, quantity has been successfully updated in the database.
    //     //   Update the fields from here if you want.
    //     var data = await response.json();
    //     console.log(data);
    //   } else {
    //     var err = await response.json();
    //     console.log(err.message);
    //   }
}

// A function to get cookies from browser
// Django stores `csrftoken` in cookie, which is required
// for all POST requests, since we will be creating new form-data
// from javascript itself, we cannot inject csrf_token as in template here.
function getCookie(cookie_name) {
    let name = cookie_name + "=";
    let ca = document.cookie.split(";");
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == " ") {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}