$(document).ready(function () {
            $(document).on('submit', '#ticker_form', function (e) {
                e.preventDefault();
                $.ajax({
                    url: '/getTicker',
                    method: 'post',
                    data: $(this).serialize(),
                    success: function (serverResponse) {
                        $('.graph').html(serverResponse);
                    }
                })
            })
})