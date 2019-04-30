# Warning
These commands are carefully crafted to NOT negatively affect your system. It is HIGHLY recommended to not diviate from this script. They are also specific to Unix-like systems, do not attempt on Windows, outcomes are unkown.

This is an example of a well known vulnerability of Docker, working as intended: https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface

1. First, as a non-root user, look at your directory root `ls -al /` then try to make a new folder at directory root: `mkdir /docker-demo`. Permission denied
1. Now load up this demo as the same non-root user: `docker-compose up`
1. Look at your directory root now: `ls -al /`. `/docker-demo` shows up, I wonder what's inside  
  a. `ls -al /docker-demo` A file?  
  b. `cat /docker-demo/exploit` Uh-oh...  
  - How else could this be abused?
  - What did the attacker need to be able to do?
4. Alright, so how can we mitigate this?
