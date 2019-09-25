$( document ).ready(function() {
    $('#search_submit').click(
        function(event) {
            event.preventDefault()
            const ticker = $('#search_ticker').val()
            const string = `https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary?region=US&symbol=${ticker}`
        }
    )

















    
});