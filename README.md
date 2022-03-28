# Echolot
Тестовое приложение. Hello World. Для ознакомления с технологиями CI/CD

## Install
```bash
git clone https://github.com/shulepoff/echolot.git
cd echolot
python3 -m venv env 
source env/bin/activate
pip3 install -r requirements.txt
```
## Run application
```bash
gunicorn -b :8000 foobar:app
```
## Run in Docker
```bash
docker build -t echolot .
docker run -d --rm --name echolot -p 8000:8000 echolot
```

## Result 
![Screenshot](/assets/result.png)
