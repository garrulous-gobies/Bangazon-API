# BangazonAPI

### Installing the project
- Create an empty directory to house your new project
- run `virtualenv env` to create a virtual environment within that directory
- run `source env/bin/activate` to initialize a virtual environment (type `deactivate` at any time to exit the environment)
- run `git clone [repository id]`
- run `cd BangazonAPI`
- run `pip install -r requirements.txt`

### Seed the database with pre-fabricated data
We've already created a file to populate the database file.
- run `python manage.py makemigrations api`
- run `python manage.py migrate`
## ADD INFO HERE ----------------------------------------------------------------------

### Starting the project
- run `python manage.py runserver`
- access the application in a browser at http://localhost:8000/api/v1/.

### Customers
Methods allowed: [GET, POST, PUT]

- get a list of all customers at http://localhost:8000/api/v1/customers/
- get an individual customer by appending an id to the url (e.g. http://localhost:8000/api/v1/customers/1/)
- get a customer and all products that the customer is selling by appending `?_include=products` to the end of the url (e.g. http://localhost:8000/api/v1/customers/?_include=products)
- get a customer and all payment types that the customer has available by appending `?_include=payments` to the end of the url (e.g. http://localhost:8000/api/v1/customers/?_include=payments)
- search for any customer property that matches a query by appending `?q=` followed by your query to the end of the url (e.g. http://localhost:8000/api/v1/customers/?q=woods would return any customers with information related to 'woods' (first name, last name, street address, etc.). This query does not have to be an exact match to return results.)

### Orders
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all orders at http://localhost:8000/api/v1/orders/
- get a specific order by appending an id to the url (e.g. http://localhost:8000/api/v1/orders/1/)
- get only completed orders at http://localhost:8000/api/v1/orders/?completed=true
- get only incomplete orders at http://localhost:8000/api/v1/orders/?completed=false
- get product resources on a specific order by appending `?_include=products` to the url (e.g. http://localhost:8000/api/v1/orders/1/?_include=products)
- get an expanded customer resource on a specific order by appending `?_include=customers` to the url (e.g. http://localhost:8000/api/v1/orders/1/?_include=customers)