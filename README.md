# PRTR transfers API deployment

This repository contains the scripts for the deployment of the best models found in https://github.com/USEPA/PRTR-QSTR-models/tree/data-driven

# Remote

This API was deployed at AWS where you can also test it from the docs endpoint

http://3.92.83.22:5000/v1/api_documentation

# Local use

## 1. Install requirements

```
pip install -r requirements.txt --no-cache-dir
```
## 2. Run de app

```
uvicorn main:app --reload --port 8000
```

## 3. Go to localhost

http://127.0.0.1:8000/v1/api_documentation
