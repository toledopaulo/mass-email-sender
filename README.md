# 📧 Mass Email Sender
<strong>Desktop &amp; Web application to send multiples emails</strong>


# How to use

## Web version
[Click here](https://toledopaulo.github.io/mass-email-sender/) to access the website (🔜)

## Desktop version
[Click here](https://toledopaulo.github.io/downloads) to download the latest version

# Compiling yourself
### Clone the repository
```console
git clone "https://github.com/toledopaulo/mass-email-sender.git"
cd mass-email-sender
```
### Install app dependencies
```console
cd src/desktop
pip install -r ./requirements.txt
```
### Compile using pyinstaller
```console
pip install pyinstaller
pyinstaller --noconfirm --onefile --console --noupx "./app.py"
```

