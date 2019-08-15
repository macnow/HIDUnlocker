# HIDUnlocker

## Requirements
- Unlocking a Windows computer using an iPhone and/or Apple Watch.
- You cannot install anything on a Windows workstation.
- Automated password entry will be based on emulation of a USB connected keyboard
- The password must be transmitted securely and cannot be saved on any device which is unattended

## Solution
The keyboard emulating device is Raspberry Pi Zero W with Linux (Raspbian) installed.
Through the `raspberrypi_usb` script the HID device (`/dev/hidg0`) has been defined on the USB port

`HIDUnlocker.py` was written in Python. It starts an HTTPS server on port 8443.
Through the JSON API, the user can send a string of characters that is translated into keyboard codes.
Then it passes via `/dev/hidg0` to the Windows workstation.

The JSON API has the following functions defined:
- **unlockPC (password)** - it unlocks the workstation by pressing the CTRL + ALT + DEL combination, then after 1s enters the passed password and sends the ENTER code
- **lockPC ()** - CTRL+ALT+DEL, after a second sends the ENTER code
- **enterLoginPassword (login, password)** - it sends the provided login followed TAB code and then it sends password and send the ENTER code at the end
- **enterPassword (password)** - it just sends the password provided

## Instalation
Set permission to execute \
`$ chmod +x HIDUnlocker.py raspberrypi_usb`

Copy HID script to `/usr/bin` \
`$ sudo cp raspberrypi_usb /usr/bin/`

Add HID script `/usr/bin/raspberrypi_usb` to `/etc/rc.local` before `exit 0` line:\
`$ sed -i "/^exit 0/i\/usr\/bin\/raspberrypi_usb" /etc/rc.local`

Generate private key and certificate for HTTPS server
```
$ openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
Generating a 2048 bit RSA private key
..........+++
.....................................................................................+++
writing new private key to 'key.pem'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:PL
State or Province Name (full name) []:dolnoslaskie
Locality Name (eg, city) []:Wroclaw
Organization Name (eg, company) []:HOAX
Organizational Unit Name (eg, section) []:
Common Name (eg, fully qualified host name) []:raspberrypi.local
Email Address []:

```

Install certificate on your iPhone and add enable it in trust section:
```
iPhone - Settings -> General -> About -> Certificat Trust Settings ->
"ENABLE FULL TRUST FOR ROOT CERTIFICATE" -> raspberrypi.local (ON)
```

### How to run?
```
$ screen sudo ~/HIDUnlocker.py
Enter PEM pass phrase: <- enter here your private key password
Starting server at https://*:8443
CTRL+A D
[detached]
```

---

## Wymagania
- Odblokowywanie komputera z Windowsem przy użyciu iPhone\`a i/lub Apple Watcha.
- Na stacji roboczej z Windowsem nie można niczego instalować.
- Zautomatyzowane wprowadzanie hasła będzie się opierać poprzez emulację klawiatury podłączonej do portu USB
- Hasło musi być przekazywane w sposób bezpieczny i nie może być zapisywane w żadnym urządzeniu, które pozostaje bez nadzoru

## Rozwiązanie
Urządzeniem emulującym klawiaturę jest Raspberry Pi Zero W z zainstalowanym Linuksem (Raspbian).\
Poprzez skrypt `raspberrypi_usb` na porcie USB zostało zdefiniowane urządzenie HID (`/dev/hidg0`)

`HIDUnlocker.py` został napisany w Pythonie. Uruchamia on serwer HTTPS na porcie 8443.\
Poprzez JSON API użytkownik może wysłać ciąg znaków, który jest tłumaczony na kody klawiatury.\
Następnie następuje przekazanie poprzez `/dev/hidg0` do stacji roboczej z Windowsem.

W JSON API zdefiniowano funkcje:
- **unlockPC(password)** - odblokowująca stację roboczą poprzez naciśnięcie kombinacji CTRL+ALT+DEL, następnie po 1s wprowadza przekazane hasło i wysyła kod ENTERa
- **lockPC()** - CTRL+ALT+DEL, po sekundzie wysyła kod ENTERa
- **enterLoginPassword(login, password)** - wprowadza przekazany login, wysyła kod TAB, a następnie wprowadza przekazane hasło i wysyła kod ENTERa
- **enterPassword(password)** - wprowadza przekazane hasło

### Instalacja
Nadaj uprawnienia do wykonywania \
`$ chmod +x HIDUnlocker.py raspberrypi_usb`

Skopiuj skrypt definiujący urządzenie HID do `/usr/bin` \
`$ sudo cp raspberrypi_usb /usr/bin/`

Dodaj wywowałanie skryptu `/usr/bin/raspberrypi_usb` do `/etc/rc.local` przed `exit 0`:\
`$ sed -i "/^exit 0/i\/usr\/bin\/raspberrypi_usb" /etc/rc.local`

Wygeneruj klucz prywatny i certyfikat dla HTTPS serwera
```
$ openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
Generating a 2048 bit RSA private key
..........+++
.....................................................................................+++
writing new private key to 'key.pem'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) []:PL
State or Province Name (full name) []:dolnoslaskie
Locality Name (eg, city) []:Wroclaw
Organization Name (eg, company) []:HOAX
Organizational Unit Name (eg, section) []:
Common Name (eg, fully qualified host name) []:raspberrypi.local
Email Address []:

```

Instalacja certyfikatu w iPhone i dodanie go do zaufanych:
```
iPhone - Ustawienia -> Ogólne -> To urządzenie... -> Ustawienie zaufania certyfikatu ->
"WŁĄCZ PEŁNE ZAUFANIE DO CERTYFIKATÓW GŁÓWNYCH" -> raspberrypi.local (ON)
```

### Jak uruchomić?
```
$ screen sudo ~/HIDUnlocker.py
Enter PEM pass phrase: <- podanie hasła do klucza, przy każdorazowym uruchomieniu
Starting server at https://*:8443
CTRL+A D
[detached]
```
