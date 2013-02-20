% for component in data['data']:
%  if component['class'] == 'graphite_chart':
<chart prefix='${component['prefix']}'>
% for target in component['targets']:
    <target metric='${target['metric']}' />
% endfor
% for parameter in component['parameters']:
    <parameter name='${parameter['name']}' value='${parameter['value']}' />
% endfor
</chart>
%  endif
% endfor