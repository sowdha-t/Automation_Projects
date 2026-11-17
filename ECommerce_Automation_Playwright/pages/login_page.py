class LoginPage:

    def __init__(self,page):
        self.page = page

        #Locators
        self._username_field = page.get_by_placeholder("Username")
        self._password_field = page.get_by_placeholder("Password")
        self._submit_button = page.get_by_role("button", name="Login")
        self._header_title = page.locator(".header_label")
        self._error_message = page.locator("h3[data-test='error']")

    def navigate(self,url):
        self.page.goto(url)

    def login(self,username,password):
        self._username_field.fill(username)
        self._password_field.fill(password)
        self._submit_button.click()

    @property
    def error_message(self):
        return self._error_message

    @property
    def username_field(self):
        return self._username_field
    @property
    def password_field(self):
        return self._password_field
    @property
    def submit_button(self):
        return self._submit_button


