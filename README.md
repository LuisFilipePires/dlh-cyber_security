## Cybersecurity Luxembourg Academy
 
 This repository contains my progress on the projects from the Cybersecurity Luxembourg Academy.

All projects are committed by modules as I progress through the program.

Each project includes a detailed description of the studies, concepts learned, and the project itself.

---
---

## Target Environment
- To connect to the target environment, I first establish the VPN connection using the .ovpn file with:
- `sudo openvpn /path/to/file.ovpn`
- After that, I launch the target machine in the sandbox/platform and start testing.
- If the target hostname does not resolve, I add it manually to /etc/hosts by mapping the target IP to the hostname. 

`echo "10.42.43.219 target.local" | sudo tee -a /etc/hosts` 

- (tee to resolve a problem of authorization with linux) or 

`sudo nano /etc/hosts` insert example: ```10.42.43.219 web0x01.hbtn```


### VPN Connection Issues - Check VPN status:


```ip a | grep tun ```

```ip addr | grep tun```

If tunX is stuck or other:

```
sudo pkill openvpn
sudo ip link delete tun0

and confirm

ip addr | grep tun
```

Restart VPN:

```sudo openvpn file.ovpn```

Confirm:

Initialization Sequence Completed

---

### test

then test with ping: ```ping web0x01.hbtn``` and confir with : ```curl -I http://web0x01.hbtn/```

``` ping web0x01.hbtn
PING web0x01.hbtn (10.42.43.219) 56(84) bytes of data.
64 bytes from web0x01.hbtn (10.42.43.219): icmp_seq=1 ttl=126 time=27.8 ms
64 bytes from web0x01.hbtn (10.42.43.219): icmp_seq=2 ttl=126 time=26.6 ms
64 bytes from web0x01.hbtn (10.42.43.219): icmp_seq=3 ttl=126 time=29.9 ms
64 bytes from web0x01.hbtn (10.42.43.219): icmp_seq=4 ttl=126 time=26.8 ms

```

confirm

```
curl -I http://web0x01.hbtn/

HTTP/1.1 302 FOUND 
or
HTTP/1.1 200 OK

```

### open in browser

http://web0x01.hbtn/

or

http://10.42.43.219/

or by clicking directly in `HTTP pot 80` button





