# OWASP Top 10

## 1-xor_decoder.sh
### XOR WebSphere Decoder

This project contains a Bash script that decodes WebSphere `{xor}` encoded passwords.

Some IBM WebSphere configurations store passwords using a weak XOR-based encoding mechanism.

The value is not encrypted securely; it is only obfuscated using XOR and then encoded using Base64.

Example:

``` {xor}KzosKw== ```


The `{xor}` prefix identifies the encoding method used by WebSphere.

## How it works

The decoder performs the following steps:

1. Receives the encoded value as an argument:

```
./1-xor_decoder.sh "{xor}KzosKw=="
```

Removes the {xor} prefix: {xor}KzosKw== --> ```KzosKw==```

Decodes the Base64 content: -> ```2b 3a 2c 2b```

Applies the XOR operation byte by byte with the known XOR key used by this encoding format.

XOR has the property that applying the same key twice restores the original data:

```
ciphertext XOR key = plaintext
plaintext XOR key = ciphertext
```

Converts the resulting bytes back to ASCII:

```74 65 73 74 --> test```

Input:

```./1-xor_decoder.sh "{xor}KzosKw=="```

Output:

```test```

Security Note

XOR with a fixed key is not a secure encryption method. Anyone who knows the algorithm can recover the original value.

Passwords should be stored using secure password hashing algorithms such as:

Argon2
bcrypt
PBKDF2

This example demonstrates the OWASP Top 10 concept of cryptographic failures, where weak protection mechanisms can expose sensitive information.

10.42.190.180
http://10.42.190.180/a2/crypto_encoding_failure/

## find the flag

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
---

# 2-flag.txt

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


