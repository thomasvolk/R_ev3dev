R_ev3dev
========

R_ev3dev is a socket server to control ev3dev robot remotely.

quick start
-----------

install the server:

    ./setup.py install

run the server:

    python3 -m R_ev3dev

parameters:

* --help - help
* --host - host default ''
* --port - port default 9999

environment varaibles:

* LOGLEVEL - server loglevel (DEBUG, INFO, WARN, ERROR) 

development
-----------

run server:

    ./setup.py run_server
    
run server with ev3dev2 mock:

    PYTHONPATH=tests LOGLEVEL=INFO ./setup.py run_server
