% for component in data['data']:
%  if component['class'] == 'graphite_chart':
<chart prefix='${component['prefix']}' parameters='${component['parameters']}'>
% for target in component['targets']:
    <target metric='${target['metric']}' function='${target['function']}'/>
% endfor
</chart>
%  endif
% endfor