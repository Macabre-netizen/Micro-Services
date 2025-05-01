from record_manager import RECORDS_MANAGEMENT

class USER_AUTHENTICATION:
    def __init__(self, username, firstname, lastname, email, password):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email  = email
        self.password = password
        
        self.records = RECORDS_MANAGEMENT()
        
    def check_user_existence(self):
        self.records.open_record_file()
        self.records.move_records_to_list() # list is holding decoded data as strings

        if self.username not in self.records.user_records:
            self.records.move_records_back_to_file()
            self.records.close_record_file()
            return 0 #returns zero id user doesnt exist
        
        else:
            self.records.move_records_back_to_file()
            self.records.close_record_file()
            return 1 #returns 1 if user exists
        
    def check_password(self):
        self.records.open_record_file()
        self.records.move_records_to_list()

        if self.password != self.records.user_records[self.username][3]:
            self.records.move_records_back_to_file()
            self.records.close_record_file()
            return 0 # returns 0 if password doesnt match
        else:
            self.records.move_records_back_to_file()
            self.records.close_record_file()
            return 1 # returns 1 if password is ok
        
    def add_new_user(self):
        self.records.open_record_file()
        self.records.move_records_to_list()
        self.records.user_records.update({self.username: [self.firstname, self.lastname, self.email, self.password]})
        self.records.move_records_back_to_file()
        self.records.close_record_file()

    def check_user_email(self):
        self.records.open_record_file()
        self.records.move_records_to_list()
        user_email = self.records.user_records[self.username][2]
        self.records.move_records_back_to_file()
        self.records.close_record_file()
        return user_email

    def delete_user(self):
        self.records.open_record_file()
        self.records.move_records_to_list()
        del self.records.user_records[self.username]
        self.records.move_records_back_to_file()
        self.records.close_record_file()


