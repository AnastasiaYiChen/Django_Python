/*M05 Django:HTML Templates
Author: Yi Chen
2020_10_29

File Name: chart.js*/

/*The getElementsByName() method of the Document object returns a NodeList Collection of elements with a choiceLabels name in the document.
* which is label of the chart*/
var choiceLabels = document.getElementsByName("choiceLabels");
var choiceLabelArray = [];
for (var i = 0; i < choiceLabels.length; i++) {
    choiceLabelArray.push(choiceLabels[i].value);
}

/*The getElementsByName() method of the Document object returns a NodeList Collection of elements with a choiceVotes name in the document.
* which are voted data of the chart*/
var choiceVotes = document.getElementsByName("choiceVotes");
var choiceVoteArray = [];
for (var i = 0; i < choiceVotes.length; i++) {
    choiceVoteArray.push(choiceVotes[i].value);
}

/*draw a pie chart*/
var ctx = document.getElementById('pie-chart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: choiceLabelArray,
        datasets: [{
            label: '# of Votes',
            data: choiceVoteArray,
            backgroundColor: [
                '#ff331e',
                '#fd9571',
                '#feded3',
                '#fffbf9',

            ],
            borderColor: [
                '#7c0000',
                '#ff6029',
                '#d2a89a',
                '#c6bdb4',

            ],
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            "display": true
        },
        tooltips: {
            "enabled": true
        },
        scales: {
            yAxes: [{
                display: true,
                gridLines: {
                    display : true
                },
                ticks: {
                    display: true,
                    beginAtZero:true
                }
            }],
            xAxes: [{
                gridLines: {
                    display : true
                },
                ticks: {
                    beginAtZero:true
                }
            }]
        }
    }
});