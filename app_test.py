import unittest
import pyperclip
from account import Account
from password import Password
from client import Client
from credentials import Credentials

class AppTest(unittest.TestCase):
    def setUp(self):
        self.account_obj=Account("Gmail", "Ryan", "brian56005")
        self.user_obj=Client("Ryan", "brian56005")
        self.credentials_obj=()

    def tearDown(self):
        Client.users_list=[]

    # def test_account_init(self):
     #    self.assertEqual(self.account_obj.acc_nm, "Gmail")
      #   self.assertEqual(self.account_obj.acc_uname, "Ryan")
      #   self.assertEqual(self.account_obj.acc_pass, "brian56005")

    # def test_gen_password(self):
    #    pass_length=int(input("Test sys password length: "))
    #    self.assertEqual(len(Password.gene_password()), pass_length)

    # def test_gen_password_copy(self):
    #    self.assertEqual(Password.gene_password(), pyperclip.paste())        

    #def test_user_init(self):
    #    self.assertEqual(self.user_obj.username, "Ryan")
    #    self.assertEqual(self.user_obj.password, "brian56005")

    #def test_add_user(self):
    #    self.user_obj.add_user(self.user_obj)
    #    self.assertEqual(len(Client.users_list),1)

    #def test_add_multiple_users(self):
    #    self.user_obj.add_user(self.user_obj)
    #    other_user_object=Client("John", "doe123")
    #   other_user_object.add_user(other_user_object)      
    #    self.assertEqual(len(Client.users_list),2)

    #def test_check_login(self):
    #    self.user_obj.add_user(self.user_obj)
    #    self.assertTrue(self.user_obj.check_login("Ryan", "brian56005"))

    #def test_return_user(self):
    #    self.user_obj.add_user(self.user_obj)
    #    self.assertEqual(Client.return_user("Ryan", "brian56005"), self.user_obj)

    #def test_create_credential_sys_password(self):
    #    print(" ")
    #    print("### Create credential with system password test ###")
    #    self.credentials_obj.create_credential()
    #    self.assertEqual(len(self.credentials_obj.credentials_list),1) 

    #def test_create_credential_custom_password(self):
    #    print(" ")
    #    print("### Create credential with system password test ###")
    #    self.credentials_obj.create_credential()
    #    self.assertEqual(len(self.credentials_obj.credentials_list),1)

    
    # def test_delete_credential(self):
    #     print(" ")
    #     print("### Delete credential test ###")
    #     self.credentials_obj.add_credential()
    #     self.credentials_obj.delete_credential()   
    #     self.assertEqual(len(self.credentials_obj.credentials_list),0)


    def test_copy_credential(self):
        print(" ")
        print("### Copy credential test. Use any account name, username: 'Ryan', password: 'brian56005' ###")
        self.credentials_obj.add_credential()
        self.credentials_obj.copy_credential()
        self.assertEqual(pyperclip.paste(), "Ryan brian56005")


if __name__=='__main__':
    unittest.main()