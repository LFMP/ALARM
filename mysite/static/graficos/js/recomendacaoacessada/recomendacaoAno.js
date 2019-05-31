function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }


      url = window.location.origin + "/admin/quantidadeRecAcessadasPorAno";
      $.get(url, function(data){
        var recomendadores = [], dias = [],sets = [];
        for(var [key,value] of Object.entries(data)){
          recomendadores.push(key);
          dias.push(value);
        }
        for(i=0;i<=recomendadores.length-1;i++){
          data = [];
          quantidade = [];
          for(var [key,value] of Object.entries(dias[i])){
             data.push(key);
             quantidade.push(value);
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
        title: 'Recomendação acessada no ano',
        showlegend: true,
        xaxis: {title: {text: 'Data'}},
        yaxis: {title: {text: 'Quantidade de recomendação'}},
    };
    
    Plotly.newPlot('recomendacaoAno', sets, layout, {displayModeBar: false},{showLink: true},{responsive: true},{locale: 'fr'});  


});