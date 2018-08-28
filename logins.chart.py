# -*- coding: utf-8 -*-
# Description: users netdata python.d module
# Author: Alexey Vekshin (alexei.vekshin@gmail.com)

# sles 11 notes: 
# - zypper install python-ordereddict
# - some python.d.plugin patching required (from time import time)
# - paths:
#   - /usr/lib64/netdata/python.d/logins.chart.py
#   - /etc/netdata/python.d/logins.conf

# to test: sudo su netdata -s /bin/bash and run
# - sles: /usr/lib64/netdata/plugins.d/python.d.plugin debug trace 1 logins
# - centos: /usr/libexec/netdata/plugins.d/python.d.plugin debug trace 1 logins

import re
from bases.FrameworkServices.ExecutableService import ExecutableService

# default module values (can be overridden per job in `config`)
# update_every = 2
priority = 60000
retries = 60
# set command: "/bin/false" in config to disable

# list of chart ids
ORDER = ['sessions']

CHARTS = {
    # id -> {options: [], lines: [[]]}
    'sessions': {
        # [name, title, units, family, context, charttype],
        'options': [None, "Current system interactive users", "users", "sessions", "logins.sessions", "line"],
        'lines': [
            # [unique_dimension_name, name, algorithm, multiplier, divisor]
            ['sessions', None, 'absolute']
        ]}
}

class Service(ExecutableService):
    def __init__(self, configuration=None, name=None):
        ExecutableService.__init__(self, configuration=configuration, name=name)
        self.command = "/usr/bin/uptime"
        self.order = ORDER
        self.definitions = CHARTS
        # conf access: self.configuration.get('host', '127.0.0.1')

    def _get_data(self):
        """
        returns dict {unique_dimention_name -> value} or None
        """
        raw_data = self._get_raw_data()
        if not raw_data:
            return None
        users = re.findall('(\d+) user', raw_data[0])[0]
        return {'sessions': users }
