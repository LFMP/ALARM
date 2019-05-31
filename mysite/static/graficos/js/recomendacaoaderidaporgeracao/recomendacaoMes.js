function getRandomColor() {
        var letters = '0123456789ABCDEF'.split('');
        var color = '#';
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
      }


      url = window.location.origin + "/admin/quantidadeRecAderidasPorGeracaoPorMes";
      $.get(url, function(data){
        var recomendadores = [], quantidade = [], cores = [], sets = [];
        for(var [key,value] of Object.entries(data)){
          recomendadores.push(key);
          quantidade.push(value);
        } 
        
        
        for(i=0;i<=recomendadores.length-1;i++){
          cores.push(getRandomColor());
        }
        sets.push(
            {
              labels: recomendadores,
              values: quantidade,
              type: 'pie',
             
              marker: {colors: cores},
            }
          );
    

    var layout = {
        title: 'Recomendação aderida no mês',
        height: 600,
        width: 400
    };

    Plotly.newPlot('recomendacaoMes', sets, layout, {displayModeBar: false},{showLink: true},{responsive: true});  


});