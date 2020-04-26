# Word cloud generator

A tool for generating word cloud from a list of input URLs or single URL in command.

Feel free to hit me up with suggestions.


### Installing


Download the latest version from Git Repo

```
git clone git@github.com:riazibrahim/cert_stash.git
```

Change to the source code folder

```
cd cert_stash
```
Start a new virtual environment

```
python -m venv venv

source venv/bin/activate
```

Install all the requirements

```
pip install -r requirements.txt
```

## Running the tool


##### Usage 1: To obtain word cloud from a single single URLs:
```
python cyber_cloud.py -u 'https://www.us-cert.gov/ncas/alerts/aa20-107a' -o cyberwordcloud
```
##### Usage 2: To obtain word cloud from a list of  URLs:
```
python cyber_cloud.py -f url_list.lst -o cyberwordcloud 
```

## Built With

* [Python3](https://www.python.org/download/releases/3.0/) 


## Authors

* **Riaz Ibrahim** - [riazibrahim](https://github.com/https://github.com/riazibrahim/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details