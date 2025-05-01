# Micro-Services
This is a simple login, signup and OTP verification python html app.
It implements basic python knowledge with html basic knowledge using the python flask module.
First of all, the user records are stored in a dictionary in a json file, the user_records.json file. Each user has their username as the key
to their other records. Currently the users present in the json file are fake users with fake records.
So a user would have their username as the key that holds the other values like this:
  {"username": ["value1", "value2", "value3", "value4"], "username2": ["value",  ...]}
The first value to every user is their first name, then the second value is the last name, then the email then the password to the apps account. These credentials are to be provided during the users signup.

 1. Befor you run the app, you will first add a valid email address in the email_credentials.json file; this file is to hold the email       adress(the apps email adress) that is supposed to send the OTP codes to the users email that is trying to login. Make sure this email(the apps email) has an app password that allows you to sign in to it from python made apps. You will then add the email adress as the key and the app password as the value to the json file dictionary. So far the scripts only support GMAIL email adresses. The used OTP codes are stored in the OTP_file.txt file.

 2. Then you will add a user(either manualy add the user to the json file or through signup) that has a valid email adress that can be sent the OTP code during login. 

 3. Now to run the app, you will run the user_html_interface.py script in your terminall, then to access the interface you go to your browser and type http://127.0.0.1:5000/login .This will take you to the login page of the app. From there it's pretty much self explanatory.

There are other things not added to the app's scripts but were to be added such as encryption, but thats prety simple to do, feel free to add whatever asspects you wish to it.


Anyways, have fun with it :).
