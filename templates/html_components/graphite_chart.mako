<%!
import graphite
%>
<div class='graphite_chart'>
<h3>${component['name']}</h3>
<img src='${graphite.chart_url(component)}' />
</div>