function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }


      url = window.location.origin + "/admin/quantidadeRecMedia";
      $.get(url, function(data){
        var recomendadores = [], quantidade = [], colors = [], sets = [];
        for(var [key,value] of Object.entries(data)){
          recomendadores.push(key);
          quantidade.push(value);
        } 
       for(i=0;i<=recomendadores.length-1;i++){
          colors.push(getRandomColor());
        }  
        
        sets.push(
          {
            x : recomendadores,
            y   : quantidade,
            type: 'bar',
            marker:{
            color: colors 
            },
          }
        );

    var layout = {
        title: 'Eficiência Média no Mês',
        xaxis: {title: {text: 'Recomendador'}},
        yaxis: {title: {text: 'Eficiência Percentual (%)'}},
    };

    Plotly.newPlot('recomendacaoMedia', sets, layout, {displayModeBar: false},{showLink: true},{responsive: true});  


});