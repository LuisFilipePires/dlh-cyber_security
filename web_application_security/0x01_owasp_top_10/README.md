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


---




