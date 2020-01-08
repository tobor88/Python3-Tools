# Python3-Tools
This is a collection of tools InfoSec people may use. 
- __fibonnaci.py__ is a simple function that InfoSec people would not use. I just really like it is all
- __porttest.py__ is used for testing whether a port is open on a remote machine.
- __pwd_generator.py__ is for quickly generating a password consisting of random characters for situtaions you may want to generate a password without entering a password manager GUI. 

Python Reverse Shell Scripts
- __py_reverse_shell_connect.py__
- __py_reverse_shell_listener.py__ 

__py_reverse_shell_listener.py__ opens a listening port you define. If no port is defined the default is 8089 as that is my favorite at the moment
Below is how to execute the script. 
```python
python3 py_reverse_shell_listener.py 8089
```
__py_reverse_shell_connect.py__ can be used to connect to a listening port. This does not neccessarily need to be used to connect to the above python listener however it does work.
```python
python3 py_reverse_shell_connect.py
# Once this is executed you will be prompted for the listening ipv4 address and port
```
