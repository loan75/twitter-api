from datetime import datetime


class Tweet:
    def __init__(self, message):
        self.id = None
        self.text = message
        self.created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
