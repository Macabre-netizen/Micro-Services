import json
import rsa
#This file is responsible for opening the file and making the records accesible

#Now lets add RSA Encryption

class RECORDS_MANAGEMENT:
    #class variables
    user_records = None #represents the contents of the file as a dictionary
    record_file = None #represents our record file
    OTP_file = None
    used_OTPs = [] # holds the contents of the file in a list as strings
    OTP_file_contents = None
    email_details_file = None
    email_details_content = None

    def __init__(self):
        self.user_records = RECORDS_MANAGEMENT.user_records
        self.record_file = RECORDS_MANAGEMENT.record_file
        self.OTP_file = RECORDS_MANAGEMENT.OTP_file
        self.used_OTPs = RECORDS_MANAGEMENT.used_OTPs
        self.OTP_file_contents = RECORDS_MANAGEMENT.OTP_file_contents
        self.email_details_file = RECORDS_MANAGEMENT.email_details_file
        self.email_details_content = RECORDS_MANAGEMENT.email_details_content
        self.rsa_public_file = None
        self.rsa_private_file = None
        self.rsa_private_key = None
        self.rsa_public_key = None
        self.saved_public_key = None
        self.saved_private_key = None

    def open_record_file(self):
        self.record_file = open("user_records.json", "r+")

    def move_records_to_list(self):
       self.user_records = json.load(self.record_file)

    def move_records_back_to_file(self):
        self.record_file.seek(0)
        self.record_file.truncate()
        json.dump(self.user_records, self.record_file)

    def close_record_file(self):
        self.record_file.close()
    
    def open_OTP_file(self):
        self.OTP_file = open("OTP_file.txt", "r+")
        self.OTP_file_contents = self.OTP_file.readlines()

    def move_OTPs_to_list(self):
        for otp in self.OTP_file_contents:
            self.used_OTPs.append(otp)

    def move_OTPs_back_to_file(self):
        self.OTP_file.seek(0)
        self.OTP_file.truncate()
        self.OTP_file.writelines(self.used_OTPs)

    def close_OTP_file(self):
        self.OTP_file.close()

    def open_email_details_file(self):
        self.email_details_file = open("email_details.json", "r+")

    def move_email_details_to_list(self):
        self.email_details_content = json.load(self.email_details_file)

    def move_email_details_back_to_file(self):
        self.email_details_file.seek(0)
        self.email_details_file.truncate()
        json.dump(self.email_details_content, self.email_details_file)

    def close_email_details_file(self):
        self.email_details_file.close()

    def open_rsa_keys(self):
        self.rsa_public_file = open("public_key.pem", "rb")
        self.rsa_private_file = open("private_key.pem", "rb")

    def access_rsa_keys(self):
        self.saved_public_key = self.rsa_public_file.read()
        self.rsa_public_key = rsa.PublicKey.load_pkcs1(self.saved_public_key)
        self.saved_private_key = self.rsa_private_file.read()
        self.rsa_private_key = rsa.PrivateKey.load_pkcs1(self.saved_private_key)

    def close_rsa_keys(self):
        self.rsa_public_file.close()
        self.rsa_private_file.close()




    