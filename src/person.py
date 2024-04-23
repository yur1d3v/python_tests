import requests

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.data_obtained = False

    def get_all_data(self):
        response = requests.get('')

        if response.ok:
            self.data_obtained = True
            return 'CONNECTED'
        else:
            self.data_obtained = False
            return 'ERROR 404'