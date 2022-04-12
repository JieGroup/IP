# IP

This open-source project aims to develop Interval Privacy into a human-centric technology of collecting private data, where individuals have a perceptible, transparent, and simple way of sharing sensitive data.

The code will be actively developed and maintained by Jie Ding and his team.

# Reference
Ding, Jie, and Bangjun Ding. "Interval Privacy: A Framework for Data Collection." arXiv preprint arXiv:2106.09565 (2021).
```
@article{ding2021interval,
  title={Interval Privacy: A Framework for Data Collection},
  author={Ding, Jie and Ding, Bangjun},
  journal={arXiv preprint arXiv:2106.09565},
  year={2021}
}
```

## Description

The initial stage of the project will provide a user-friendly tool to create and manage web-based interface for collecting interval-private data.

## Getting Started

### Dependencies

* Python3 required

### Installing

* setup python virtual env
https://docs.python-guide.org/dev/virtualenvs/

* install pip and python
```
sudo yum -y install python-pip
sudo yum install python37
```
* run one time on a server or computer
```
pip3 install --user virtualenv
python3 -m virtualenv --version
```
* cd into the project folder and install virtual env there, e.g. 
```
cd /Users/jie/Desktop/web-development/survey/ 
python3 -m virtualenv venv
```
* activate/deactivate
```
source venv/bin/activate
deactivate
which python3
```
* install necessary packages
```
pip3 install -r requirements.txt
```

### Executing program

* run flask in local host
```
export FLASK_ENV=development 
export FLASK_APP=app
FLASK_APP=app flask run --host=0.0.0.0 --port=8000
```
* check what was exported 
```
declare -p FLASK_APP
```
* Then view it live from 
http://3.141.9.233:8000/

 
## Help

Please contact Jie for any concerns on the open-source project

## Authors

Contributors names and contact info

ex. Jie Ding  
ex. [dingj@umn.edu](http://jding.org)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details


