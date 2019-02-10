# HIDUnlocker

## Założenia
- Odblokowywanie komputera z Windowsem przy użyciu iPhone\`a i/lub Apple Watcha.
- Na stacji roboczej z Windowsem nie można niczego instalować.
- Zautomatyzowane wprowadzanie hasła będzie się opierać poprzez emulację klawiatury podłączonej do portu USB
- Hasło musi być przekazywane w sposób bezpieczny i nie może być zapisywane w żadnym urządzeniu,\
które pozostaje bez nadzoru

## Realizacja
Urządzeniem emulującym klawiaturę jest Raspberry Pi Zero W z zainstalowanym Linuksem (Raspbian).\
Poprzez skrypt `raspberrypi_usb` na porcie USB zostało zdefiniowane urządzenie HID (`/dev/hidg0`)

`HIDUnlocker.py` został napisany w Pythonie. Uruchamia on serwer HTTP chroniony SSLem na porcie 8443.\
Poprzez JSON API użytkownik może wysłać ciąg znaków, który jest tłumaczony na kody klawiatury.\
Następnie następuje przekazanie poprzez `/dev/hidg0` do stacji roboczej z Windowsem.

W JSON API zdefiniowano funkcje:
- **unlockPC(password)** - odblokowująca stację roboczą poprzez naciśnięcie kombinacji CTRL+ALT+DEL, następnie po 1s wprowadza przekazane hasło i wysyła kod ENTERa
- **lockPC()** - CTRL+ALT+DEL, po sekundzie wysyła kod ENTERa
- **enterLoginPassword(login, password)** - wprowadza przekazany login, wysyła kod TAB, a następnie wprowadza przekazane hasło i wysyła kod ENTERa
- **enterPassword(password)** - wprowadza przekazane hasło

### Instalacja
Nadawanie uprawnień do wykonywania \
`$ chmod +x HIDUnlocker.py raspberrypi_usb`

Skopiowanie skryptu definiującego urządzenie HID do `/usr/bin` \
`$ sudo cp raspberrypi_usb /usr/bin/`

Dodanie wywołanie skryptu `/usr/bin/raspberrypi_usb` do `/etc/rc.local` przed `exit 0`:\
`$ sed -i "/^exit 0/i\/usr\/bin\/raspberrypi_usb" /etc/rc.local`

Wygenerowanie klucza i certyfikatu
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

### Uruchomienie
```
$ screen sudo ~/HIDUnlocker.py
Enter PEM pass phrase: <- podanie hasła do klucza, przy każdorazowym uruchomieniu
Starting server at https://*:8443
CTRL+A D
[detached]
```
