## Foundations of Software Engineering
This repository provides a starting point for students participating in the Foundations course at CODE University. 

To use this repository, you need to have: 
- basic working knowledge of Python, git, and the terminal 
- a terminal running on your own computer which gives access to a linux-like command line 
- Python 3.8 Installed and running

#### Setup Instructions
```
mkdir simpleserver 
cd simpleserver/ 
git init . || git clone <REPO>
virtualenv -p python3.8 venv
source venv/bin/activate
pip install uwsgi || requirements.txt
```

based on [this](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html)


#### Hello, World!
> uwsgi --http :8080 --wsgi-file hello_world/hello_world.py

Full-on version 

> uwsgi --http-socket 127.0.0.1:8080 --wsgi-file hello_world/hello_world.py --master --processes 4 --threads 2 --stats 127.0.0.1:8181
 

### Flask version 
> pip install flask 

> uwsgi --http-socket 127.0.0.1:8080 --wsgi-file sample_website/sample_website.py --callable app -H venv/

or to go full-on 

> uwsgi --http-socket 127.0.0.1:8080 --wsgi-file sample_website/sample_website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/


## Run with caddy 
# disable https for first attempt

# > caddy reverse-proxy --from 127.0.0.1:80 --to 127.0.0.1:8080

## Lint locally 
> `flake8 --exclude __pycache__,venv`
(or else it takes forever)

## get CD running on GCP/GAE 

based roughly on https://github.com/google-github-actions/deploy-appengine 

#### On GCP 

1. Get cloud credits [LINK]
1. create project https://cloud.google.com/resource-manager/docs/creating-managing-projects
1. create app engine application https://console.cloud.google.com/appengine/create (europe-west-3 is FRA)
1. create service account https://cloud.google.com/iam/docs/creating-managing-service-accounts

![Permissions](./documentation/service-account-permissions.png?raw=true)

1. enable app engine api https://console.developers.google.com/apis/library/appengine.googleapis.com 

1. enable cloud buld api 
https://console.cloud.google.com/marketplace/product/google/cloudbuild.googleapis.com

1. allow cloud build to deploy to app engine 
https://cloud.google.com/cloud-build/docs/deploying-builds/deploy-appengine#grant-permissions


1. Give service account permission to act as project accountt (???) --> https://github.com/DrAdamRoe/foundations-sample-website-/runs/1558999799?check_suite_focus=true

1. get service account private key 
https://cloud.google.com/iam/docs/creating-managing-service-account-keys

--> you should now have a .JSON file on your own computer


On GitHub: 
1. Add secret https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets

