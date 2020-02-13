## About FileHarvester

FileHarvester is a python3 script that will scrape a target for files of a defined extension. 

The default extensions this scrape are: pdf, doc and docx. 

Running this too often will cause a 'too many requests' message - this is on Google's side. 

Running through a proxy may help.


## Screenshots

![FileHarvester](images/fileHarvester.gif "FileHarvester in action")


## Installation

```
git clone https://github.com/cmcginley/fileHarvester.git
```

## Recommended Python Version:

FileHarvester currently supports only **Python 3** and **Linux**.

Windows support may be added.

## Dependencies:

FielHarvester depends on the `argparse` python module.

These dependencies can be installed using the requirements file:

```
- Installation on Linux
```
sudo pip install -r requirements.txt
```

Alternatively, each module can be installed independently as shown below.

```

#### argparse Module

- Install for Ubuntu/Debian:
```
sudo apt-get install python-argparse
```

- Install for Centos/Redhat:
```
sudo yum install python-argparse
``` 

- Install using pip:
```
sudo pip install argparse
```


### Usage

Short Form    | Long Form       | Description
------------- | ----------------|-------------
-s            | --site          | Site to target
-n            | --newfiletypes  | Clear the defaults and set your own file types
-a            | --addmore       | Add more file extensions to look for
-d y          | --download y     | Download all returned results (use y)


### Examples

* To list all the basic options and switches use -h switch:

``python3 fileHarvester.py -h``

* To perform a search of pdf, doc and docx files (default setting):

``python3 fileHarvester.py example.com``

* To set your own file types to search:

``python3 fileHarvester.py example.com -n txt,bin,db``

* To download the results:

``python3 fileHarvester.py example.com -d y``
``python3 fileHarvester.py example.com -n xls,xlsx -d y``


## License

FileHarvester is licensed under the GNU GPL license. take a look at the [LICENSE](https://github.com/cmcginley/LICENSE) for more information.



## Version
**Current version is 0.1**
