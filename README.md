## Cybersecurity Luxembourg Academy
 
 This repository contains my progress on the projects from the Cybersecurity Luxembourg Academy.

All projects are committed by modules as I progress through the program.

Each project includes a detailed description of the studies, concepts learned, and the project itself.

## Target Environment
- To connect to the target environment, I first establish the VPN connection using the .ovpn file with:
- `sudo openvpn /path/to/file.ovpn`
- After that, I launch the target machine in the sandbox/platform and start testing.
- If the target hostname does not resolve, I add it manually to /etc/hosts by mapping the target IP to the hostname. `echo "10.10.11.25 target.local" | sudo tee -a /etc/hosts` 
- (tee to resolve a problem of authorization with linux) or `sudo nano /etc/hosts` insert example: ```10.42.172.168 web0x01.hbtn```



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

## 2-flag.txt

The hint says:

> Check the Headers, `Bearer` exactly ;)

Inspecting the HTTP request headers reveals an Authorization header: ```network``` filter ```xhr```

a Authorization
	```bearer eyd1c2VybmFtZSc6ICd5b3NyaScsICdwYXNzd29yZF9oYXNoJzogJ0R6NThKek1kS0FVR1BDWVZDeThRTW1zRmFRZ1lad0FHT0E9PSd9```


The value after `Bearer` looks like Base64 encoding.

### Step 1 - Decode the Bearer token

Decode the token:

```echo "eyd1c2VybmFtZSc6ICd5b3NyaScsICdwYXNzd29yZF9oYXNoJzogJ0R6NThKek1kS0FVR1BDWVZDeThRTW1zRmFRZ1lad0FHT0E9PSd9" | base64 -d```


Output:
```{'username': 'yosri', 'password_hash': 'Dz58JzMdKAUGPCYVCy8QMmsFaQgYZwAGOA=='}```

### Step 2 - Decode the password hash

The previous task showed that the application uses:

Base64 encoding
XOR encryption
Static XOR key: 0x5f

First decode the password field:

```echo "Dz58JzMdKAUGPCYVCy8QMmsFaQgYZwAGOA==" | base64 -d | xxd```

output:
```
00000000: 0f3e7c27331d2805063c26150b2f1032
00000010: 6b0569081867000638
```


### Step 3 - Apply XOR decryption

```
Using the key from the previous task:
./1-xor_decoder.sh "Dz58JzMdKAUGPCYVCy8QMmsFaQgYZwAGOA=="
Pa#xlBwZYcyJTpOm4Z6WG8_Yg
```

output:Pa#xlBwZYcyJTpOm4Z6WG8_Yg

### credentials:

```
username: yosri
password: Pa#xlBwZYcyJTpOm4Z6WG8_Yg
```

### Flag

After authentication, i got the flag:

```4f62815ade89e7d21ba46f7e3618b841```


---

## 3

by pray attention in request response 

```
last_actions	
"John - Visited you - Wed Aug 5 10:28:26 2026 - UserID: 918203", 
"Jimmy - Visited you - Wed Aug 5 10:28:26 2026 - UserID: 32781850", 
"Dexter - Visited you - Wed Aug 5 10:28:26 2026 - UserID: 811152675" ]

```

At John profile : John Doe

```
"You - Visited Yosri - Wed Aug  5 10:28:26 2026 - UserID: 918203",
"Yosri - Visited you - Wed Aug  5 11:57:43 2026 - UserID: 58263966"
```
Jimmy profile : Jimmy Neutron
```
"You - Visited Yosri - Wed Aug  5 10:28:26 2026 - UserID: 32781850",
"Yosri - Visited you - Wed Aug  5 11:59:08 2026 - UserID: 58263966"
```
Dexter profile: Dexter Didi
```
You - Visited Yosri - Wed Aug  5 10:28:26 2026 - UserID: 811152675
Yosri - Visited you - Wed Aug  5 12:00:12 2026 - UserID: 58263966
```



