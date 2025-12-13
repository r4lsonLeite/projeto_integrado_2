import datetime
class EventMetric:
    def __init__(self, event_id: int, user_id: int , event_type: str , reference_id: int, event_date: datetime):
        self.event_id = event_id
        self.user_id = user_id
        self.event_type = event_type
        self.reference_id = reference_id
        self.event_date = event_date
    def record_event(self):
        print(f"Event {self.event_id} recorded: Type='{self.event_type}', User={self.user_id}, Date={self.event_date}.")
        return True


