function getServerResponse(str) {
    $(document).on('click', `#${str}`, function (e) {
        e.preventDefault();
        $.ajax({
            url: `/get_${str}`,
            method: 'post',
            data: {
                ticker: $('#search_ticker').val(),
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function (serverResponse) {
                $('#stats').html(serverResponse)
                $('#graph').html('')
            },
            error: function (serverResponse) {
                $('#graph').html('')
                $('#stats').html(`<h1>Shit happened in ${str}</h1>`)
            },
        })
    })
    // $('#graph').html();
}

function setPage() {
    $.ajax({
        url: '/get_nav',
        method: 'post',
        data: {
            ticker: $('#search_ticker').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (serverResponse) {
            $('#navigation_bar').html(serverResponse);
        },
    })
    let IDs = ['technical', 'profile', 'financial', 'news']
    for (let id of IDs) {
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

function getInterval(str) {
    if (str === '1d') {
        return '5m'
    }
    if (str === '5d') {
        return '60m'
    } else {
        return '1d'
    }
}

$(document).on('change', "input[name='graph_range']", function (e) {
    e.preventDefault();
    let val =$("input[name='graph_range']").val()
    console.log(val)
    console.log(getInterval(val))
    $.ajax({
        url: '/getTicker1',
        method: 'post',
        data: {
            graph_range: val,
            ticker: $("input[name='ticker']").val(),
            interval: getInterval(val),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (serverResponse) {
            console.log(serverResponse)
            $('#graph').html(serverResponse);
        },
        error: function (re) {
            console.log(serverResponse)
            $('#graph').html('<h1>Graph is not happy</h1>');
        }
    })
})