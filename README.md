# Python3-Tools
This is a collection of tools InfoSec people may use. 
- __fibonnaci.py__ is a simple function that InfoSec people would not use. I just really like it is all
- __hex2num.py__ I hate doing hexadecimal math. This is a command I made to help me calculate the offset in a buffer overflow when I have a return address of 0x4c. Calculating 0x4c to decimal is shown in the command below
```python3
./hex2num.py
# RESULTS OF RUNNING ABOVE COMMAND
Enter a hexadecimal value to convert to decimal: 4c # Enter 4c not 0x4c
4c in Decimal = 76
```
- __hex2text.py__ This command is meant to easily calculate the text value of hexadecimal value to string. I found this useful when using msf-pattern_create to crash an application and discover the registries EIP value of the crash.
```python3
./hex2text.py
# RESULTS OF RUNNING ABOVE COMMAND
Enter the hexadecimal value you want to conver to text: 42306142
B0aB
```
- __porttest.py__ is used for testing whether a port is open on a remote machine.
- __pwd_generator.py__ is for quickly generating a password consisting of random characters for situtaions you may want to generate a password without entering a password manager GUI. 
- __py_portscanner.py__ I plan on making my baby as a great way for testing for open ports when python3 is available on a target
- __porttest.py__ simple tool that was great for met in getting started in working with sockets

Python Reverse Shell Scripts
- __py_reverse_shell_connect.py__
- __py_reverse_shell_listener.py__ 

__py_reverse_shell_listener.py__ opens a listening port you define. If no port is defined the default is 8089 as that is my favorite at the moment
Below is how to execute the script. 
```python
python3 py_reverse_shell_listener.py
# Edit the contents of this file to change the listening port
```
__py_reverse_shell_connect.py__ can be used to connect to a listening port. This does not neccessarily need to be used to connect to the above python listener however it does work.
```python
python3 py_reverse_shell_connect.py
# Once this is executed you will be prompted for the listening ipv4 address and port
```

![alt text](https://raw.githubusercontent.com/tobor88/Python3-Tools/master/portscanner.png "Py Port Scanner")

As can be seen from the image above, py_portscanner.py uses the following format. These examples scan all ports on the defined host.
```python
python3 .\py_portscanner.py <ipv4 address>
python3 .\py_portscanner.py 192.168.0.1
```
