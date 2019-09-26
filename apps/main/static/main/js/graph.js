$( document ).ready(function() {

async function getData() {

    const response = await fetch(`https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-chart?interval=5m&region=US&symbol=${ticker}&lang=en&range=${range}`, {
	"method": "GET",
	"headers": {
		"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
		"x-rapidapi-key": "9cf6f84669mshf37812fae4d0b86p19dc92jsnac00aa2c3e97"
	}
})
const myJson = await response.json();
console.log(JSON.stringify(myJson));
var ptag = document.getElementById('data')

var chartData = []
var listOfOpen = myJson.chart.result[0].indicators.quote[0].open
console.log(myJson.chart.result)
for(var i = 0; i < listOfOpen.length; i++){
    chartData.push(listOfOpen[i])
}
console.log(chartData)
// chart data

var ctx = document.getElementById('myChart').getContext('2d');
    
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: chartData,
            datasets: [{
                label: 'Apple',
                fill: false,
                data: chartData,
                borderColor:  'rgba(255, 159, 64, 1)',
                borderWidth: 1
            },]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: false
                    }
                }]
            }
        }
    });

    }
getData()
