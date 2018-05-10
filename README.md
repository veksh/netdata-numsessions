# Collect number of interactive login sessions for netdata

This plugin collects a number of currently logged-in users (from `uptime` shell command),
this metric is missed from core netdata.

## installation manually
- copy plugin to `python.d` plugins dir
- copy config to `/etc/netdata/python.d/`
- restart netdata, check "logins" section

## configuration
As usual, no config is required by default
- to disable plugin, set `command` to `/bin/false`
- to change check interval, set `update_every`