$(document).ready(function() {
    let timeout;

    $('.filme').hover(function() {
        const $popup = $(this).find('.popup');
        timeout = setTimeout(function() {
            $popup.show();
        }, 1000);
    }, function() {
        clearTimeout(timeout);
        $(this).find('.popup').hide();
    });

    $('.popup').hide();

    $('.adicionar').click(function(event) {
        event.stopPropagation();
        var filmeId = $(this).data('id');
        $.ajax({
            type: 'POST',
            url: '/adicionar_assistidos',
            data: { filme_id: filmeId },
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$(document).ready(function() {
    $('.adicionar').on('click', function() {
        $(this).addClass('clicked');
        const filmeId = $(this).data('id');
        
        setTimeout(() => {

            $(this).removeClass('clicked');

            $.ajax({
                type: 'POST',
                url: '/adicionar_assistidos',
                data: { filme_id: filmeId },
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }, 200);
    });
});
