function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }


      url = window.location.origin + "/admin/quantidadeRecAcessadasPorHora";
      $.get(url, function(data){

        var recomendadores = [], dias = [],sets = [];

        for(var [key,value] of Object.entries(data)){
          recomendadores.push(key);
          dias.push(value);
        }
        for(i=0;i<=recomendadores.length-1;i++){
          data = [];
          quantidade = [];
          var num = 0;
          for (var j = 0;j<dias[i].length;j++){
              var string;
              if(num<10){
                  string = "0" + num.toString() + ":00";
              }
              else{
                  string = num.toString() + ":00";
              }

              data.push(string);
              quantidade.push(dias[i][j]);
              num = num + 1;
          }


          color = getRandomColor();
          sets.push(
            {
              name: recomendadores[i],
              x : data,
              y   : quantidade,
              mode: 'lines+markers',
              type: 'scatter',
              line: {color: getRandomColor()},
            }
          );
        }


    var layout = {
        title: 'Recomendação acessada por hora',
        showlegend: true,
        xaxis: {title: {text: 'Hora'}},
        yaxis: {title: {text: 'Quantidade de recomendação'}},
    };

    Plotly.newPlot('recomendacaoHora', sets, layout, {displayModeBar: false},{showLink: true},{responsive: true},{locale: 'fr'});


});