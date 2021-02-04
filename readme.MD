## Foundations of Software Engineering
This repository provides a starting point for students participating in the Foundations course at CODE University. 

To use this repository, you need to have: 
- basic working knowledge of Python, git, and the terminal 
- a terminal running on your own computer which gives access to a linux-like command line 
- Python 3.8 Installed and running
- An account on GitHub

### Local Setup Instructions
Students of the class should begin by forking this repository so that it is in their own GitHub repository. Forking is like making a copy, but fancier. 

Before continuing, make sure that this repository has _your_ username in the URL, not Adam's or anyone else's. 


On your own computer: 
- Create a new folder, with a name like "foundations". That's up to you. e.g. `mkdir foundations`
- change directory into that new folder, e.g. `cd foundations`
- clone (like downloading, but fancier) _your_ forked repository from GitHub onto your own computer, e.g. `git clone https://github.com/<Best_Username_EVer>/foundations-sample-website-.git`

Now you should have your own fork (copy) of the foundations repository (folder) cloned (downloaded) onto your own computer. 

#### Before you continue: check your version of python 

Make sure that you are using a version of Python which is relatively new, at least version 3.8. You can check this by using the command `python --version`at the command line. You can also a very fancy script by typing `python check_setup/version_check.py`. 

You should see something like this: 

![Your version of Python will work with this code!](./documentation/version_check.png?raw=true)

If you see a longer message (`### oh no! ###`), you are using a version of Python which is too old. You will need to use Python 3.8 or newer. Like with all other software, you have to update the language itself from time to time. 

Keep in mind that many computers have multiple versions of Python installed on them. It might be that you need to type `python`, `Python`, `python3`,`python3.8`, or something else, to get a version that you have already installed. Or you may need install it. 

### Create a fresh, new, virtual environment
@TODO add instructions from previous years. 

source venv/bin/activate

### Run the "Hello, World!" website on your own computer

At this point, you should finally be able to run the "hello, world!" website locally on your own computer. The command `uwsgi` will run a server. Try this command to start your server (e.g. run your website):

> uwsgi --http :8080 --wsgi-file hello_world/hello_world.py

If you see something like `uwsgi: command not found`, something is wrong with your _environment_ (the way the computer is setup), not the code itself. Make sure you have activated a virtual environment, are running python3.8 or newer, and have installed the libraries listed in requirements.txt, as described above. 


This will run a super simple website, only accessible on your own computer. To see it, navigate to http://localhost:8080 in your browser. It should look like this: 

![Your local Hello, World! website](./documentation/localhost_helloworld.png?raw=true)

If you haven't done so yet, this is a good time to open the file you are running, `hello_world/hello_world.py`. This is about as bare-bones as a web server can get. 

These instructions are based on [the uwsgi documentation](https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html). To learn more or troubleshoot, that is a good place to start. 

## Run the sample website on your own computer, using Flask. 

Building on the previous example, we will use a framework for building websites called Flask. We will go into more details on what it is in class, and why it is useful. 

Running a website using Flask using the same basic command, `uwsgi`, but requires a few more arguments: 

> uwsgi --http-socket 127.0.0.1:8080 --wsgi-file sample_website/website.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:8181 -H venv/

You should now be able to go http://localhost:8080 in your browser and see the Hello, Flask! Website 

![Your local Hello, Flask! website](./documentation/localhost_helloflask.png?raw=true)

This command starts a server (`uwsgi`), specifies which IP address and port to run on (`http-socket`), chooses which file to run off of (`wsgi-file`), specifies what the application itself is called (`app`, defined in the file you are running), specifies a second automatic site for statistics (`stats`), tells your computer what resources (think processing) this application requests in order to run well (`processes` and `threads`), and lastly, selects a version of Python (`-H`). Whew. For now, you don't need to think too much about all of this. We will work with the file and the socket a bit in the coming weeks in particular.

## Congratulations! You are Running Your First Website! 

Alright, you've gotten the sample website running on your own computer with Flask. That is no small feat. You should be proud of yourself. Now we're going to take it up a notch. 

### Edit The Website
If the website is running, turn it off (`Ctrl+C` in the terminal to quit. You need to turn the website off and on again, called reloading, to get changes. 

Open `sample_website/website.py`, and greet in a different way. I've edited mine to greet myself, for instance. It now returns "Hello, Adam!". After starting the web server locally again, it shows this, too. 

![Your local Hello, Flask! website](./documentation/localhost_helloadam.png?raw=true)

Alright! We are getting close to running by hand, on our computers, the things we did in the first week on Glitch. This is a good moment to open the browser inspector tools and play around with the HTML and CSS like we did on other live websites, too. 

## Code Quality: Linting 
As software grows in scale and complexity, the quality of the code itself becomes more and more important. Think about organizing your closet or cleaning a shared space like a kitchen or bathroom with roommates or family members. At some point, you need to agree on how you are going to do it, otherwise people get frustrated. There are many standards out there, and in practice, every language has its own best practices, and different organizations - or different teams within organizations - will do things differently. Thankfully, Python has a standard called PEP8, which we will do our best to adhere too. Read more about the standard, what is in it, and linting in general [here](https://realpython.com/python-pep8/), for instance.

We will use a tool called `flake8`to lint our code. It should already be installed via your `requirements.txt` file. 

To lint your code, run: 

> `flake8 --exclude venv`

If you see _no output at all_, it means everything is fine. 

![Successful Linting: no errors at all!](./documentation/local_flake8.png?raw=true)

This may be a bit unsatisfying. We all want to be rewarded with a green success message for doing a good job, right? Think of this is an alarm system which is _not_ going off. That's a good thing! 

If you want to see more under the hood, add the `--verbose` flag. This will show you what it is doing, and convince you that it is doing something. 

> `flake8 --exclude venv --verbose`


By the way, the flag `--exclude` tells flake8 to ignore some directories. The `venv` directory contains the Python programming language itself, so linting that is basically saying "Did the authors of the Python language itself adhere to best-practices in writing the Code?". While perhaps quite interesting, it is not really relevant right now. And may take a long time. If you notice the tool slowing down over time, you may also want to exclude the `__pycache__` directory, which is generated by your computer when you run your software, to speed things up. 


### Writing Better Code, the first time around
We don't want to wait for alarm to go off and tell us we are doing something wrong, we want the alarm to not go off in the first place, right? Now is the time to set up VSCode to help you write better (Python) Code. 

Let's start with installing & enabling the Python extension. You may have it already. To check, go to _Extensions_ and search for Python. VSCode is open-source and anyone can add an extension to the marketplace. The number of stars and downloads gives you a hint about popularity and quality, which is a good place to start. We will use the top extension, from Microsoft (who is the main developer of VSCode itself, too.)

![VSCode's Python Marketplace](./documentation/vscode_python_marketplace.png?raw=true)

If you see something like this, it is installed already! you are good to go. Click on the settings cog to customize it. 

Linting can also be enabled directly in the CODE editor. You will see yellow underlines for warnings and red underlines for errors. This gives you quick feedback as a developer, correcting errors quickly. [Enable and learn more about Linting in VSCode here](https://code.visualstudio.com/docs/python/linting)


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

