# Environment setup

To completely setup environment for the first time:

### 1. First time setup

1. Install virtualenv

   `sudo apt-get install virtualenv`

2. Create a new virtualenv

   At the root of the repository:
   `virtualenv venv`

### 2. Install dependencies

1. Activate virtualenv

   `source venv/bin/activate`

2. Install dependencies into activated virtualenv

   _(venv) $_ `pip install -r requirements.txt`

## Usual virtualenv activation, deactivation

- **Activate**

   `source venv/bin/activate`

- **Deactivate**

   _(venv) $_ `deactivate`
