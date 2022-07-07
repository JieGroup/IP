# Open-source project for collecting private data

This open-source project aims to develop Interval Privacy into a human-centric technology of collecting private data, where individuals have a perceptible, transparent, and simple way of sharing sensitive data.

The code will be actively developed and maintained by Jie Ding and his collaborators.

## Reference
Ding, Jie, and Bangjun Ding. "Interval Privacy: A Framework for Privacy-Preserving Data Collection." https://arxiv.org/pdf/2106.09565.pdf
```
@article{ding2022interval,
  title={Interval Privacy: A Framework for Data Collection},
  author={Ding, Jie and Ding, Bangjun},
  journal={IEEE Transactions on Signal Processing (just accepted)},
  year={2022}
}
```

## Description

The initial stage of the project will provide a user-friendly tool to create and manage web-based interface for collecting interval-private data.

## Getting Started

### Dependencies

* Python3.8 required

### Installing

pipenv install -r requirements.txt

### Executing program

* run flask in local host
``` 
pipenv install
pipenv shell
export FLASK_APP=application.py
flask run

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

Jie Ding  
[dingj@umn.edu](http://jding.org)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
