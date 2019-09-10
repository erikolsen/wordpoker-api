class BasePage:
    url = None

    def __init__(self, driver):
        self.driver = driver

class HomePage(BasePage):
    pass
