# Django Test
## Python Version 3.10
## CLI Commands
``` bash
# run following commands in terminal in backend_test directory 
# after cloning.

pip install pipenv
pipenv install
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
# this command could take some time to run
python manage.py create_employees
```

``` bash
# if below command ran without any errors, 
# it means you have installed this project successfully.
python manage.py runserver
```

## Task
``` bash
1. Make a relationship between companies and employees.
2. In home page there is a table with company names and an empty link along with each company. 
   clinking on that link, should open up a page to a form with a dropdwon of employees that when choosed 
   should associate that employee with that particular company and redrirect to the table.
3. All employee names associated with a company should be displayed comma separated on the second column of the table on the home page.
4. Each employee can only be associated with one company only.
5. Employee dropdown in the form should be searchable.

```
``` bash
1.Make a relationship between companies and employees:
In the models.py file, there is a ForeignKey relationship between the Employee and 
Company models. This creates a one-to-many relationship where each employee can be 
associated with one company.

2.In the home page, there is a table with company names and an empty link along with each 
company:
In the companies.html template, a table is created displaying the company names and a 
link to add an employee to each company. When the link is clicked, it opens 
the add_employee view with the company ID as a parameter.

3.All employee names associated with a company should be displayed comma separated on 
the second column of the table on the home page:
In the companies.html template, a loop iterates through all employees associated with a 
company and displays their names in a comma-separated format.

4.Each employee can only be associated with one company only:
In the add_employee view in the views.py file, an employee can be associated with a
 company only if they do not have a company assigned already.

5.Employee dropdown in the form should be searchable:
In the add_employee.html template, the Select2 library is used to create a searchable
 dropdown for employees. The script at the bottom of the template initializes the Select2 
 functionality for the employee dropdown.

```

