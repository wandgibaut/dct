# Distributed Cognitive Toolkit

The Distributed Cognitive Toolkit (DCT) is a toolkit based primally on shellscript and python (although this can be freely changed) to allow the construction of Distributed Cognitive Architectures, either in the form of containers of in a multi-device fashion.

This project is based on [Cognitive Systems Toolkit (CST)](https://github.com/CST-Group/cst) and follows the same theories what CST rellies on.

## Prerequisites
- All scripts in this repository presume execution in a **Linux** environment (or another system with **bash** support). 
- The default scripts presented here also use **Python 3**, but this is optional as you may make any change you want.

## Basic Notions

(do cst)

## Usage

In order to make a **Codelet** work, it must have a *proc* script that will be called in a loop, the registry of the input and output **Memories**, including an allias, the ip/port for communication and the type of communication (a mongo DB, a Redis DB or just a comm over TCP) and, if needed, a configuration of a server to receive TCP msgs. Then, the *run.sh* script must be called to put the codelet in activity. This structure, although simple, allows this kind of Codelet to run in very limited hardwares or multiple ones run in a more powerful computing system, like a Desktop or Notebook. It is highly recommended that you run the Codelets inside a container (like a **Docker** Container) if you working on a PC (or other multipurpose system) to both have a better control over network configurations and to avoid issues that may harm your system.

This repository also contains utility **Docker-compose** scripts that creates all codelets of a given **Mind** in containers and put them to work.


### Structure of a Codelet

In the *src/codelet* folder you can find all scripts that constitutes a **Codelet**. The *methods* folder contains all basic scripts to make the codelet work and is not meant to be changed except if you don't want to work with python or wanna make structural changes. In the codelet's root folder you may find five files and another folder (besides *methods*):

- fields.json
- calculateActivation.sh
- proc.sh
- proc.py
- server.py
- memories

The first one, *fields.json* contains information regarding this codelet, including *name*, *timestep*, *inputs* and *outputs*. Here, inputs and outputs are lists with strutures containing *ip/port*, *name* and *type*, and represents each **memory** which this codelet interacts. The second one should be costumized to fit your project and reflect a calculation of the activation of the codelet, something that may be used to verify if the process represented by the *proc.sh* code should happen or not.

The following two, *proc.sh* and *proc.py*, represent the base script called by other scripts in *methods* (and is under the same advice of changing only if not working with python) and the actual script that you should put your code reflecting what the codelet should really do. Remember that this is called in a loop, with a sleep of *timestep* seconds between each call.

The *server.py* script is called in case a TCP communication as receiver is expected. This creates a server and listen to a specific *ip/port* that must be declared. Future improvements will deal with **originally unexpected** TCP communications.

Finally, the memories folder should contain all simple **.json* files representing memories readed or writen through TCP communication.

### Structure of a Memory

The basic structure of what consists the is something like this:

**{"name": "motor-memory", "ip/port": "172.28.1.1:9999", "type": "tcp", "I": "3671", "eval": 0.0}**

The **'I'** field may contain any type of data, been responsabilty of the user to deal with the information correctly.

Note that it is writen as a json object and may be inside a *.json* file or as a entry in a database such *mongo* or *redis*. 


### Running a Codelet inside a Docker Container


In the examples/docker folder there is a *docker-compose.yml* file that, when run with *docker-compose up*, creates six containers, where two of them are a MongoDB and a Redis container and the other four represents a codelet each. This simple example ilustrates the communication between the codelets based on the information present in the *fields.json* and the parallel nature of this architecture. 

The two database containers are places where collections representing **Memories** associated with Codelets, from what they read and write information.

All containers are created with pythonCodelet (botar link) image, which is based on python3 image with *pymongo* and *redis* installed.



### Running a Codelet inside a Raspberry Pi
(exemplos e notas no raspi)

### Running a Codelet inside an Arduino
(exemplo e notas no arduino)


# __________________________________________________________

Note: This project is still under development, and some concepts or features might not be available yet. [Feedback/bug report](https://github.com/wandgibaut/dct/issues) and [Pull Requests](https://github.com/wandgibaut/dct/pulls) are most welcome!