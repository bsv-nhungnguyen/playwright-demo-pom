
class LoginPageLocators:
    INPUT_USERNAME = "//input[@placeholder = 'メールアドレス']" #メールアドレス
    INPUT_PASSWORD = "//input[@placeholder = 'パスワード']" #パスワード
    BUTTON_LOGIN = "//button[@type='submit']" #ログイン

    
class SignupPageLocators:
    INPUT_EMAIL = "//input[@placeholder = 'メールアドレス']" #メールアドレス (Message)
    INPUT_PASSWORD = "//input[@placeholder = 'パスワード']" #パスワード (Password)
    INPUT_PASSWORD_CONFIRM = "//input[@placeholder = 'パスワード（確認）']" #パスワード（確認）
    BUTTON_SIGNUP = "//button[@type='submit']" #サインアップ