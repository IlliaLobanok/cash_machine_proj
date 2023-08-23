a small pet-project dedicated to development of web-based cash machine/register system.
planned functions are:
    - log in/out
    - open, edit, close receipt
    - create, edit, remove product
    - run X- and Z-reports
    - add, edit, delete user
    - distribution of functions among different user roles

for correct running:
    1. use
        pip install -r requirements.txt
    , then clone repo to your machine.
    2. use misc/MySQL/DB_ERD.mwb to reverse-engineer the database.
    3. start the MySQL server as root, no password, host 127.0.0.1 (default).
    4. run the main.py.

it is also planned to add WSGI server in the future. currently everything is holding on flask development server.

please consider this as my learning pet-project, which has evolved from programming course at third university year.