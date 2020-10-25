function getWeekendValue() {
    var uiWeekend = document.getElementsByName("uiWeekend");
    for(var i in uiWeekend) {
      if(uiWeekend[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

  
  function onClickedEstimateCons() {
    console.log("Estimate consumption button clicked");
    var avgtemp = document.getElementById("uiAvgtemp");
    var mintemp = document.getElementById("uiMintemp");
    var maxtemp = document.getElementById("uiMaxtemp");
    var precip = document.getElementById("uiPrecip");
    var weekend = getWeekendValue();
    var deltatemp = document.getElementById("uiDeltatemp");
    var estCons = document.getElementById("uiEstimatedCons");
  
    var url = "http://127.0.0.1:5000/predict_beer_consumption";
  
    $.post(url, {
        average temperature (c): parseFloat(avgtemp.value),
        min temperature (c): parseFloat(mintemp.value),
        max temperature (c): parseFloat(maxtemp.value),
        precipitation (mm): parseFloat(precip.value)
        weekend: weekend,
        delta temperature (c): parseFloat(deltatemp.value)
    },function(data, status) {
        console.log(data.estimated_cons);
        estCons.innerHTML = "<h2>" + data.estimated_cons.toString() + " Litres</h2>";
        console.log(status);
    });
  }