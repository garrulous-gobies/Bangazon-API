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
- run `./django_data.sh api data.json`

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
- search for customers that have never placed an order  by appending `?active=false` to the url (e.g. http://localhost:8000/api/v1/customers/?active=false)

### Orders
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all orders at http://localhost:8000/api/v1/orders/
- get a specific order by appending an id to the url (e.g. http://localhost:8000/api/v1/orders/1/)
- get only completed orders at http://localhost:8000/api/v1/orders/?completed=true
- get only incomplete orders at http://localhost:8000/api/v1/orders/?completed=false
- get product resources on a specific order by appending `?_include=products` to the url (e.g. http://localhost:8000/api/v1/orders/1/?_include=products)
- get an expanded customer resource on a specific order by appending `?_include=customers` to the url (e.g. http://localhost:8000/api/v1/orders/1/?_include=customers)
- accessing an order detail view will show the product details associated with that order

### Employees
Methods allowed: [GET, POST, PUT]

- get a list of all employees at http://localhost:8000/api/v1/employees/
- get a specific employee by appending an id to the url (e.g. http://localhost:8000/api/v1/employees/1/)
- Each employee representation lists the name of the associated department
- Each employee representation lists the currently-assigned computer (null if none assigned)

### Computers
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all computers at http://localhost:8000/api/v1/computers/
- get a specific computer by appending an id to the list url (e.g. http://localhost:8000/api/v1/computers/1/)


### Products
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all products at http://localhost:8000/api/v1/product/
- get a specific product by appending an id to the list url (e.g. http://localhost:8000/api/v1/computers/1/)
-Foreign Key relationship to ProductType

### ProductType
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all productTypes at http://localhost:8000/api/v1/productType/
- get a specific product type by appending an id to the list url (e.g. http://localhost:8000/api/v1/productType/1/)

### PaymentType
Methods allowed: [GET, POST, PUT, DELETE]

- get a list of all paymentTypes at http://localhost:8000/api/v1/paymentType/
- get a specific payment type by appending an id to the list url (e.g.http://localhost:8000/api/v1/paymentType/1/)
-Foreign Key relationship to customer

### Departments
Methods allowed: [GET, POST, PUT]

- get a list of all departments at http://localhost:8000/api/v1/departments
- get a specific department by appending an id to the list url (e.g.http://localhost:8000/api/v1/departments/1/)
- can embed employees with "?_include=employees" to view a list of all employees in each department
- Can filter departments with budgets greater than a certain number with "?_filter=budget&_gt=

## trainingProgram

Methods allowed [GET, POST, PUT, DELETE(only if training program is in the future)]

- get a list of all training programs at http://localhost:8000/api/v1/trainingProgram
- get a specific department by appending an id to the list url (e.g.http://localhost:8000/api/v1/trainingProgram/1/)
-Employees related to the training program (signed up) will be included in the response
- appending the query string ?completed=false will return only training programs with a date in the future (e.g. http://localhost:8000/api/v1/trainingProgram?completed=false)



