// var $dd = $('*').data('toggle', 'dropdown');
// $dd.on('click', function(e) {
//     $(this).children('.badge').hide();
//     var icoWid = $(this).outerWidth(),
//         ddlWid = $('.dropdown').outerWidth(),
//         calc = -((ddlWid / 2) - icoWid);
//     $(this).next('.dropdown').css('left', calc).slideToggle();
//     $(document).on('keydown', function(e) {
//         if (e.which === 27) {
//             $('.dropdown').hide();
//         }
//     });
//     e.stopPropagation();
// });

// var json = ["Antony Smith commented on your post (2 secs ago)", "Cathel Gomes likes your post (1 sec ago)", "Joe Cale posted on your wall (few mins ago)"];
// $('.close').on('click', function() {
//     $(this).parent('#popupWrap').hide();
// });

// i = 0;

// setInterval(function notifyRefresh() {
//     if (i < json.length) {
//         $('#popupWrap').show();
//         $('#popupWrap').children('.popup-ntfctn').text(json[i]);
//         i++;
//         setTimeout(function popupAlert() {
//             $('#popupWrap').hide();
//         }, 4000);
//     } else {
//         $('#popupWrap').hide();
//         i = i;
//     }
// }, 6000);