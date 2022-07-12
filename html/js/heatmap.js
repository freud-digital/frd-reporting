var cal = new CalHeatMap();
var cal_work = new CalHeatMap();

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
        var parser2 = function(data) {
            var list = {};
            data.forEach(el => {
                var work_changed = el.work_changed;
                list[work_changed] = 1;
            });
            return list;
        }
        cal.init({
            itemSelector: "#cal-heatmap-man",
            domain: "month",
            start: new Date(2021, 0),
            range: 24,
	        displayLegend: true,
            data: items,
            afterLoadData: parser
        });
        cal_work.init({
            itemSelector: "#cal-heatmap-works",
            domain: "month",
            start: new Date(2021, 0),
            range: 24,
	        displayLegend: true,
            data: items,
            afterLoadData: parser2
        });
    });
