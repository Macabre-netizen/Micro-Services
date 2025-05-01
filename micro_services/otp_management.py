from record_manager import RECORDS_MANAGEMENT
import random
import smtplib

class OTP_GENERATE:
    def __init__(self, username, user_email, otp_code):
        self.user_records = RECORDS_MANAGEMENT()
        self.username = username
        self.user_email = user_email
        self.otp_code = otp_code

    def generate_otp(self):
        self.user_records.open_OTP_file()
        self.user_records.move_OTPs_to_list()

        while True:
            new_otp = random.randint(100000, 999999)
            if new_otp not in self.user_records.used_OTPs:
                self.user_records.used_OTPs.append(str(new_otp)+"\n")
                break
        
        self.user_records.move_OTPs_back_to_file()
        self.user_records.close_OTP_file()
        return new_otp
    
    def send_OTP(self):
        self.user_records.open_email_details_file()
        self.user_records.move_email_details_to_list()

        for key, value in self.user_records.email_details_content.items():
            business_email = key
            business_email_password = value

        email_subject = "Your One-Time Password (OTP) for Micro-services:"
        email_body = f"Subject: Your One-Time Password (OTP)\nHello user {self.username},\n"
        email_body += f"Your One-Time Password (OTP) for verifying your identity is:\n"
        email_body += f"OTP Code: {self.otp_code} (Valid for [xx] minutes)\n"
        email_body += f"Please enter this code in the app to complete your verification. Do not share this code with anyone.\n"
        email_body += f"If you didn't request this OTP, please ignore this email\n"
        email_body += f"Thank you.\n"
        email_msg = f"Subject: {email_subject}\n\n{email_body}"

        service = smtplib.SMTP("smtp.gmail.com", 587)
        service.ehlo()
        service.starttls()
        service.ehlo()
        service.login(business_email, business_email_password)
        service.sendmail(business_email, self.user_email, email_msg)
        self.user_records.move_email_details_back_to_file()
        self.user_records.close_email_details_file()
    
# my_num = OTP_GENERATE(None, None, None) # first the users username, then their email, then the OTP code
# new_num = my_num.generate_otp()
# my_num = OTP_GENERATE("Ibra", "musukuibrahim1@gmail.com", str(new_num))
# my_num.send_OTP()