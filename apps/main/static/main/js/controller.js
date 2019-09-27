function getServerResponse(str) {
    $(document).on('click', `#${str}`, function(e){
        e.preventDefault();
        // console.log(str)
        $.ajax({
            url: `/get_${str}`,
            method: 'post',
            data: {
                ticker: $('#search_ticker').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (serverResponse) {
                console.log(serverResponse)
                $('#stats').html(serverResponse)
            },
            error: function (serverResponse) {
                console.log(serverResponse)
                $('#stats').html(`<h1>Shit happened in ${str}</h1>`)
            },
        })
    })
}

function setPage() {
    $.ajax({
        url: '/get_nav',
        method: 'post',
        data: {ticker: $('#search_ticker').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()},
        success: function (serverResponse) {$('#navigation_bar').html(serverResponse);},
    })
    let IDs = ['technical', 'profile', 'financial', 'news']
    for (let id of IDs){
        getServerResponse(id)
    }
    (() => {
        $.ajax({
            url: `/get_profile`,
            method: 'post',
            data: {
                ticker: $('#search_ticker').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (serverResponse) {
                $('#stats').html(serverResponse)
            },
        })
    })()
}

$('#search_submit').click(function (e) {
    e.preventDefault();
    setPage();
})
