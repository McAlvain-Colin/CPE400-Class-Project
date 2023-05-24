# CPE400-Class-Project
TCP implimentation in Python for CPE400, Computer Communication Networks 
CS333 Final Project: Automated Testing and Deployment of "UNO by 'bennuttall'"
------------------------------------------------------------------------------



Table of Contents
-----------------



Installation
------------

update linux system
    sudo apt-get update
install git 
    sudo apt-get install git
install coverage
    sudo apt-get install python3-pip
    pip install coverage
install docker
    sudo apt-get install docker-ce docker-ce-cli containerd.io
check installation 
    git --version
    coverage --version
    docker --version

Usage
-----


Features
--------


Automated Testing
-----------------

To automate testing, the github repo was outfited with a YAML file. This file is located inside a .github/workflow folder. 

The name of this YAML file is "Uno".

The YAML file contains a workflow that will be triggered on a push event.

The workflow consists of two jobs: "UnitAndIntegrationTests" and "Docker".

The "UnitAndIntegrationTests" job runs on the latest version of Ubuntu and uses a matrix strategy to test the Python code against different versions of Python (3.7 to 3.11).

The job contains a set of steps that:
    Checkout the code using the GitHub Actions checkout action.
    Set up the specified version of Python and cache pip.
    Install the "ruff" package using pip.
    Install the "coverage" package using pip.
    Run linting checks using "ruff".
    Run unit tests using "coverage".

Automated Deployment
--------------------
To automate testing, the github repo was outfited with a YAML file. This file is located inside a .github/workflow folder. 

The name of this YAML file is "Uno".

The YAML file contains a workflow that will be triggered on a push event.

The workflow consists of two jobs: "UnitAndIntegrationTests" and "Docker".

The "Docker" job runs on the latest version of Ubuntu and depends on the successful completion of the "UnitAndIntegrationTests" job.

The job contains a set of steps that:
    Checkout the code using the GitHub Actions checkout action.
    Login to Docker Hub using the docker/login-action.
    Set up Docker Buildx using the docker/setup-buildx-action.
    Build and push a Docker image using the docker/build-push-action.
    The Docker image is tagged with the username and the name of the image as specified in the secrets of the repository.

This is dependant on the githib repo containing two secretes for the Docker username 
    and token.


Credits
-------
uno.py: bennuttall
pgz_screenshot.png: bennuttall
random_game.py: bennuttall
uno_tests.py: bennuttall 
    -Note: this test is included for transparency only.It is created by the original uno.py writer, bennuttall. It is not part of the CS333 Final Project. Testing Coverage is attained thorugh tests_uno.py alone.

Design Document: McAlvain_Colin
Dockerfile: McAlvain_Colin
README: McAlvain_Colin
requirements.txt: McAlvain_Colin


Configure CI/CD for your application. Docker Documentation. (2023, May 2). Retrieved May 2, 2023, from https://docs.docker.com/language/python/configure-ci-cd/ 

Contact
-------
McAlvain Colin
    github: McAlvain_Colin
    email: cmcalvain@nevada.unr.edu
