$(document).ready(function() {
    $('.increment-btn').click(function(e) {
        e.preventDefault();
        var inc_value = $(this).closest('.row').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            var inc_value = $(this).closest('.row').find('.qty-input').val(value);
        }
    });
    $('.decrement-btn').click(function(e) {
        e.preventDefault();
        var inc_value = $(this).closest('.row').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            var inc_value = $(this).closest('.row').find('.qty-input').val(value);

        }
    });

});