from user_auth import USER_AUTHENTICATION
from otp_management import OTP_GENERATE
import sys
from flask import Flask, redirect, url_for, render_template, request

class UI_backend:
    #class variables
    html_interface = Flask(__name__, template_folder="templates")

    def __init__(self, user_name, firstname, lastname, user_email, user_password):
        self.user_name = user_name
        self.firstname = firstname
        self.lastname = lastname
        self.user_email = user_email
        self.user_password = user_password
        self.generated_otp_code = None
        self.user_auth = USER_AUTHENTICATION(None, None, None, None, None)
        self.otp_auth = OTP_GENERATE(None, None, None)
        self.html_interface = UI_backend.html_interface


    def user_name_login(self):
        self.user_auth = USER_AUTHENTICATION(self.user_name, None, None, None, None)
        user_auth_val = self.user_auth.check_user_existence()

        if user_auth_val == 0:
            return 0
        else:
            return 1
        
    def user_pass_login(self):
        self.user_auth = USER_AUTHENTICATION(self.user_name, None, None, None, self.user_password)
        password_auth_val = self.user_auth.check_password()

        if password_auth_val == 0:
            return 0
        else:
            return 1
        
    def get_user_email(self):
        self.user_email = self.user_auth.check_user_email()

    def signup(self):
        self.user_auth = USER_AUTHENTICATION(self.user_name, self.firstname, self.lastname, self.user_email, self.user_password)
        self.user_auth.add_new_user()

    def OTP_verify(self):
        self.otp_auth = OTP_GENERATE(None, None, None)
        self.generated_otp_code = self.otp_auth.generate_otp()
        self.get_user_email()
        self.otp_auth = OTP_GENERATE(self.user_name, self.user_email, str(self.generated_otp_code))
        self.otp_auth.send_OTP()



class UI_frontend:
    def __init__(self):
        self.ui_backend = UI_backend(None, None, None, None, None)
        self.setup_interface_routes()

    def setup_interface_routes(self):
        self.ui_backend.html_interface.add_url_rule("/home", view_func=self.home_page, methods=["GET", "POST"])
        self.ui_backend.html_interface.add_url_rule("/login", view_func=self.login, methods=["GET", "POST"])
        self.ui_backend.html_interface.add_url_rule("/signup", view_func=self.signup, methods=["GET", "POST"])
        self.ui_backend.html_interface.add_url_rule("/OTP_verification", view_func=self.OTP_verification, methods=["GET", "POST"])

    def home_page(self):
        return render_template("home_page.html")

    def signup(self):
        if request.method == "POST":
            new_user_first_name = request.form.get("first_name")
            new_user_last_name = request.form.get("last_name")
            new_user_email = request.form.get("email")
            new_user_password = request.form.get("new_password")
            new_user_username = request.form.get("new_username")
            new_user_password_confirm = request.form.get("confirm_password")
            if new_user_password_confirm != new_user_password:
                print("Sorry, password doesnt macth to previous one.")
                return render_template("signup_page.html", content="Sorry, password doesnt macth to previous one.")
            self.ui_backend = UI_backend(new_user_username, new_user_first_name, new_user_last_name, new_user_email, new_user_password)
            self.ui_backend.signup()
            return redirect(url_for("login"))
        if request.method == "GET":
            return render_template("signup_page.html")

    def OTP_verification(self):
        #lets check if the OTP user has entered is correct
        if request.method == "POST":
            user_otp_input = int(request.form.get("otp_code"))
            if user_otp_input != self.ui_backend.generated_otp_code:
                return render_template("OTP_verification_page.html", content="Sorry, Wrong OTP code.Try again!")
            if user_otp_input == self.ui_backend.generated_otp_code:
                return redirect(url_for("home_page"))
        if request.method == "GET":
            self.ui_backend.OTP_verify()
            return render_template("OTP_verification_page.html")


    def login(self):
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            self.ui_backend = UI_backend(username, None, None, None, None)
            username_val = self.ui_backend.user_name_login()
            password_val = None

            if username_val == 0:
                return render_template("login_page.html", content="Sorry, username donesnt exist")
            if username_val == 1:
                self.ui_backend = UI_backend(username, None, None, None, password)
                password_val = self.ui_backend.user_pass_login()
            if password_val == 0:
                return render_template("login_page.html", content="username and password doesnt match")
            if password_val == 1: # OTP comes here
                return redirect(url_for("OTP_verification"))
            
        if request.method == "GET":
            return render_template("login_page.html")
        
    def run(self):
        self.ui_backend.html_interface.run(debug=True)
        


if __name__ == "__main__":
    ui = UI_frontend()
    ui.run()