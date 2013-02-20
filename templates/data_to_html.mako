<%!
import components
%>
<html><body>
% for component in data['data']:
  ${components.render_html(component)}
% endfor
</body></html>