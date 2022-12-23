# A Django Framework Integration for Wallet Auth in Thirdweb

Based on documentation available for other frameworks here: https://portal.thirdweb.com/auth

**Frontend**: For wallet connection in NextJS/Typescript
**Backend**: Django/DjangoRestFramework in Python

## Setup

### To setup the frontend: 

```bash
$ cd thirdweb-auth-django 
$ make web-build
$ make web-run
```

###  To setup the backend: 
First create a python virtual environment: 
```bash
python -m venv venv
```

Then install the dependencies: 
```bash
$ pip install -r requirements.txt
```

Finally, run the server:
```bash
$ make server-run
```

Then simply navigate to https://localhost:3000 to interact with the app!

