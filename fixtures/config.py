from operator import concat
from random import randint
from names import get_name, get_last_name
from faker import Faker


empID = randint(100000, 999999)
expected_first_name = "Indiana"
expected_last_name = "Jones"
date_of_start = "2022-01-01"
username = "Admin"
password = "admin123"
expected_welcome_message = "Dashboard"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
invalid_login = "User"
expected_invalid_credentials_message = "Invalid credentials"
expected_required_message = "Required"