Assigning a static IP to nodes on WLANs, replace /etc/network/interfaces with

```
auto wlan0
iface wlan0 inet static
address 192.168.X.X
netmask 255.255.255.0
gateway 192.168.X.X
```

My rc.local
```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

cd /home/pi/security/
python creator.py &
node server.js rendered/ &

exit 0
```