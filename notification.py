import datetime
class Notification:
    def __init__(self, notification_id: int, user_id: int, channel: int , content: str, send_date: datetime, send_status: str):
        self.notification_id = notification_id
        self.user_id = user_id
        self.channel = channel
        self.content = content
        self.send_date = send_date
        self.send_status = send_status
    def send_notification(self):
        if self.send_status == 'pending':
            self.send_status = 'sent'
            print(f"Notification {self.notification_id} successfully SENT via {self.channel}.")
            return True
        elif self.send_status == 'sent':
            print(f"Notification {self.notification_id} has already been SENT.")
            return False
        else:
            self.send_status = 'failed'
            print(f"Notification {self.notification_id} FAILED to send.")
            return False