'''
flow all,response,flows
flow alias <,resp_arg1,flows
port information,response,portchannel
port information <,resp_arg1,portchannel
interface npb,response,opbinterfaces
interface npb <,resp_arg1,opbinterfaces
interfaces summary,response,interfaces
interfaces summary <,resp_arg1,interfaces
platform summary,response,devices
platform environment information,response,environment
reboot-cause,response,reboot-cause
ztp status,response,ztp-status
uptime,response,uptime
system uptime,response,sysuptime
clock,response,clock
boot,response,boot
platform ssdhealth,response,ssdhealth
system memory,response,sysmemory
memory utilisation,response,memutil
cpu util,response,cpuutil
syslog information,response,syslog
gtp inforation,response,gtp
platform psustatus,response,psus
snmp-trap,response,snmptrap
snmp-community,response,snmp-community
interface counters,response,interface stats
interface counters <,resp_arg1,interface stats
interface transciever info,response,interface transceivers
interface transceiver info <,resp_arg1,interface transceivers
lldp neighbours,response,lldp neighbors
docker memory-usage,response,docker stats
process stats,response,process stats
platform syseeprom,response,eeprom stats
snmp-trap thresholds,response,snmp threshold
flow rules <,resp_arg2,flows rules
tacacs-server,response,tacacs-server
timezone,response,clock timezone
ntp,response,ntp
flow counters <,resp_arg3,flows rules statistics
'''
