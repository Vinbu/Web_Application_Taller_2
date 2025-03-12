# Web_Application_Taller_2
Encryption and Decryption software, including testing in Python.
## Index
1. [Installation](#installation)
2. [Scripts](#scripts)
## Installation
>[!WARNING]
>It´s neccesary to have installed python 3.12.X in
>your system, if you don´t have it click the next
>link: [Python](https://www.python.org/downloads/)
1. Clone the repository
2. Run the following commands in your terminal
```bash
pip install typer pycryptodome pytest
```
## Scripts
The software consist of two functions: encrypt and decrypt. Run these scripts inside `src`. Go there using `cd src` inside the root.
### encrypt
To use this function you need to enter in your terminal the next command to use it:
>[!WARNING]
>Your password´s length has to be 16 characters, because of how it works the AES.
>To check the documentation click this link: [AES](https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)
```bash
python3 main.py encrypt "<message>" "<your_password>"
```
Now this will print your encrypted message. Save it, because you'll need it when you want to decrypt it.
### decrypt
To decryption you have to remember your password and run the next command in your terminal:
```bash
python3 main.py decrypt "<your_password>"
```