Assigning a static IP to nodes on WLANs, replace /etc/network/interfaces with

```
auto wlan0
iface wlan0 inet static
address 192.168.X.X
netmask 255.255.255.0
gateway 192.168.X.X
```
