### How I did this 

based on [this](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)



#### Setup Instructions
```
mkdir simpleserver 
cd simpleserver/ 
git init . || git clone <REPO>
virtualenv -p python3.8 venv
source venv/bin/activate
pip install uwsgi || requirements.txt
```

#### Hello, World!
> uwsgi --http :9090 --wsgi-file helloworld.py

Full-on version 

> uwsgi --http-socket 127.0.0.1:3031 --wsgi-file helloworld.py --master --processes 4 --threads 2 --stats 127.0.0.1:9191
 

### Flask version 
> pip install flask 

> uwsgi --http-socket 127.0.0.1:3031 --wsgi-file flasky.py --callable app -H venv/

or to go full-on 

> uwsgi --http-socket 127.0.0.1:3031 --wsgi-file flasky.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191 -H venv/


## Run with caddy 
disable https for first attempt

> caddy reverse-proxy --from 127.0.0.1:80 --to 127.0.0.1:3031

## Lint locally 
> flake8 --exclude __pycache__,venv
(or else it takes forever)