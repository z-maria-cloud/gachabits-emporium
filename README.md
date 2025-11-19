# Gachabits Emporium

Generate random objects with the Gachabits API.

## Dependencies

This program needs to make requests to an instance of the [Gachabits API](https://github.com/z-maria-cloud/gachabits-api) in order to work.

After you install and setup **Gachabits API**, create a `.env` file in the emporium directory:

```
SERVER_ADDRESS=http://localhost:3000/batch
```

## Setup

This project must be run inside a Python virtual environment. To create the development environment:

```
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

## Usage

Enter the Python virtual environment with `. env/bin/activate`.

Choose from one of the available `.json` files or create your own. Run `python3 emporium.py [chosen filename]`, and you will get your chosen object!