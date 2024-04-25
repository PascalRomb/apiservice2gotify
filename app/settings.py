import os
from dotenv import load_dotenv

class Settings():
    def load_variable(self, variable_name):
        variable = os.environ.get(variable_name)
        assert variable is not None, variable_name + " is not set in dotenv file"
        return variable
            


    def load_variables(self):
        load_dotenv()
        self.WUD_GOTIFY_APP_TOKEN = self.load_variable("WUD_GOTIFY_APP_TOKEN")
        self.SPEEDTEST_GOTIFY_APP_TOKEN = self.load_variable("SPEEDTEST_GOTIFY_APP_TOKEN")
        self.GOTIFY_SERVER_URL = self.load_variable("GOTIFY_SERVER_URL")

settings = Settings()