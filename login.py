import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy, QMessageBox, QStackedWidget

class Users():
    def __init__(self, username, password, age, email):
        self.username = username
        self.password = password
        self.age = age
        self.email = email

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register Page")
        self.setFixedSize(500, 240)
        register_layout = QGridLayout()

        label_name = QLabel('<font size = "4"> Username: </font/>')
        label_age = QLabel('<font size = "4"> Age: </font/>')
        label_email = QLabel('<font size = "4"> Email: </font/>')
        label_password = QLabel('<font size = "4"> Password: </font/>')

        
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Set your username')
        self.lineEdit_Password = QLineEdit()
        self.lineEdit_Password.setPlaceholderText('Set your Password')
        self.lineEdit_Age = QLineEdit()
        self.lineEdit_Age.setPlaceholderText('Enter your age')
        self.lineEdit_email = QLineEdit()
        self.lineEdit_email.setPlaceholderText('Enter your email')

        register_layout.addWidget(label_name, 0, 0)
        register_layout.addWidget(self.lineEdit_username, 0, 1)
        register_layout.addWidget(label_password, 1, 0)
        register_layout.addWidget(self.lineEdit_Password, 1, 1)
        register_layout.addWidget(label_email, 2, 0)
        register_layout.addWidget(self.lineEdit_email, 2, 1)
        register_layout.addWidget(label_age, 3, 0)
        register_layout.addWidget(self.lineEdit_Age, 3, 1)

        register_button = QPushButton('Register')
        register_layout.addWidget(register_button, 4, 0, 1, 2)

        login_message = QLabel('<font size = "3"> Already have an account? </font/>')
        register_layout.addWidget(login_message, 6, 0)
        login_button = QPushButton('Login!', parent=self)
        login_button.move(180, 188)
        login_button.clicked.connect(self.switch_window)
        self.setLayout(register_layout)
        register_button.clicked.connect(self.create_user)
    def create_user(self):
        userlist.append(Users(str(self.lineEdit_username.text()), str(self.lineEdit_Password.text()), self.lineEdit_Age.text(), self.lineEdit_email.text()))
        message = QMessageBox()
        message.setText('Successfully created new user!')
        message.exec()


    def switch_window(self):
        widget.setCurrentIndex(0)


class LoginForm(QWidget):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.setWindowTitle("Login Page")

        layout = QGridLayout()
        label_name = QLabel('<font size = "4"> Username </font/>')
        self.lineEdit_username = QLineEdit()
        self.lineEdit_username.setPlaceholderText('Please enter your username:')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)
        
        label_password = QLabel('<font size = "4"> Password </font/>')
        self.lineEdit_Password = QLineEdit()
        self.lineEdit_Password.setPlaceholderText('Please enter your Password:')
        layout.addWidget(label_password, 1, 0, 2, 2)
        layout.addWidget(self.lineEdit_Password, 1, 1, 2, 2)
        
        button_login = QPushButton('Login')
        button_login.clicked.connect(self.check_password)
        layout.addWidget(button_login, 3, 0, 2, 2)
        register_message = QLabel('<font size = "3"> Don\'t have an account? </font/>')
        register_button = QPushButton('Register!', parent=self)
        register_button.move(173, 197)
        layout.addWidget(register_message, 5, 0, 1, 1)
        register_button.clicked.connect(self.go_to_register)
        self.setLayout(layout)


    def check_password(self):
        msg = QMessageBox()
        for i in userlist:
            if str(self.lineEdit_username.text()) == i.username and str(self.lineEdit_Password.text()) == i.password:
                msg.setText('Success')
                msg.exec()
            else:
                msg.setText('Incorrect Password')
                print(str(self.lineEdit_username.text()), str(self.lineEdit_Password.text()))
                print(i.username, i.password)
                msg.exec()

    def go_to_register(self):
        widget.setCurrentIndex(1)


userlist = []
app = QApplication(sys.argv)
widget = QStackedWidget()
login = LoginForm()
register = Register()
widget.addWidget(login)
widget.addWidget(register)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Quitting application")