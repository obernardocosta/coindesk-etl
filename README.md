# Initiate

## Create and Activate the virtual environment
```bash
python3 -m venv venv
source venv/bin/active
```

## To install modules from requirements

```bash
pip3 install -r requirements.txt
```

## To install a new module and save it in requirements

```bash
pip3 install <module_name> && pip3 freeze > requirements.txt
```

## To test with PyTest 
```bash
pytest --cov-report term-missing --cov=src tests/
```

## To test with PyTest Watcher
```bash
ptw . --cov-report term-missing --cov=src tests/
```