$(document).ready(function () {
    $('span.full-screen').click(function () {
        let target = $(this).parent().parent().parent().parent()
        target.toggleClass("full col-sm-12  col-md-12  col-lg-12")
    })

    $('span.copy-link').click(function () {
        id = $(this).attr('id').replace('copy_image_', '')
        $.get(`/copy_link/${id}`, function (data) {
            input = $('input[name=link_inp]')
            input.val(data)
            input.select()
            document.execCommand('copy')
            $('.alert-cont').append(`
                <div class="alert col-sm-8 col-md-6 position-fixed alert-dismissable alert-success">
                    <span class="close btn text-danger" data-dismiss="alert">
                        <i class="fas fa-times-circle"></i>
                    </span>
                    Copied <span class='alert-link'>${data}</span> successfully!
                </div>
                `)

        })
    })

    $('.photo-cont').hover(function () {
        if (!$(this).hasClass('full')) {
            $(this).find('.controls, .caption').fadeIn().css({ 'display': 'flex', 'text-align': 'center' })
        }
    },
        function () {
            if (!$(this).hasClass('full')) {
                $(this).find('.controls, .caption').slideUp()
            }
        })

    // auto dissmiss alert
    window.setTimeout(function () {
        $(".alert").slideUp(500, function () {
            $(this).remove();
        });
    }, 2500)


})