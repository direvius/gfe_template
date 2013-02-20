<html><body>
<%
import graphite
%>
% for component in data['data']:
%  if component['class'] == 'graphite_chart':
<img src='${graphite.chart_url(component)}' />
%  endif
% endfor
</body></html>