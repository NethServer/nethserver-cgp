<?php

# collectd's datadir
$CONFIG['datadir'] = '/var/lib/collectd';

# "png", "svg", "canvas" or "hybrid" (canvas on detail page, png on the others) graphs
$CONFIG['graph_type'] = 'hybrid';

# use the negative X-axis in I/O graphs
$CONFIG['negative_io'] = true;

# add XXth percentile line + legend to network graphs
# false = disabled; 95 = 95th percentile
$CONFIG['percentile'] = 95;

# create smooth graphs (rrdtool -E)
$CONFIG['graph_smooth'] = true;

# draw min/max spikes in a lighter color in graphs with type default
$CONFIG['graph_minmax'] = true;

# show graphs in bits or bytes
$CONFIG['network_datasize'] = 'bits';

# page refresh (in seconds)
$CONFIG['page_refresh'] = '60';

?>
