function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }


      url = window.location.origin + "/admin/quantidadeRecAcessadasPorMes";
      $.get(url, function(data){
        var recomendadores = [], quantidade = [], days = [], sets = [];
        for(var [key,value] of Object.entries(data)){
          recomendadores.push(key);
          quantidade.push(value);
        } 
        for(i=1;i<=Math.max(quantidade[0].length,quantidade[1].length);i++){
          days.push(i);
        }
        for(i=0;i<=recomendadores.length-1;i++){
          color = getRandomColor();
          sets.push(
            {
              name: recomendadores[i],
              x : days,
              y   : quantidade[i],
              mode: 'lines+markers',
              type: 'scatter',
              line: {color: getRandomColor()},
            }
          );
        }
    

    var layout = {
        title: 'Recomendação acessada no mês',
        showlegend: true,
        xaxis: {title: {text: 'Mês'}},
        yaxis: {title: {text: 'Quantidade de recomendação'}},
    };

    Plotly.newPlot('recomendacaoMes', sets, layout, {displayModeBar: false},{showLink: true},{responsive: true});  


});