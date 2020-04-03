# Echolot
Тестовое приложение. Hello World

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

