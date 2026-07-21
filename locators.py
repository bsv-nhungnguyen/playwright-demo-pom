
class LoginPageLocators:
    INPUT_USERNAME = "//input[@placeholder = 'メールアドレス']" #メールアドレス
    INPUT_PASSWORD = "//input[@placeholder = 'パスワード']" #パスワード
    BUTTON_LOGIN = "//button[@type='submit']" #ログイン
class HomePageLocators:
    BUTTON_LOGOUT = "//button[@class='logout-button']" #ログアウト
    BUTTON_PROFILE = "//a[@href='/profile']" #プロフィール