var cal = new CalHeatMap();

fetch("https://raw.githubusercontent.com/freud-digital/frd-reporting/gh-pages/data/manifestations_all.json")
    .then(response => response.json())
    .then(data => {        
        var items = data.data;
        var parser = function(data) {
            var list = {};
            data.forEach(el => {
                var man_changed = el.man_changed;
                list[man_changed] = 1;
            });
            return list;
        }
        cal.init({
            domain: "month",
            start: new Date(2021, 0),
            range: 24,
	        displayLegend: true,
            data: items,
            afterLoadData: parser
        });
    });
