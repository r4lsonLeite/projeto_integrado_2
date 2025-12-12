class PartnerOffer:
    def __init__(self, offer_id, partner_id, title, description, criteria_json, enrollment_url, is_active=True):
        self.offer_id = offer_id
        self.partner_id = partner_id
        self.title = title
        self.description = description
        self.criteria_json = criteria_json
        self.enrollment_url = enrollment_url
        self.is_active = is_active
    def toggle_activation(self):
        self.is_active = not self.is_active
        if self.is_active:
            print(f"Offer {self.offer_id}: {self.title} is now ACTIVE.")
        else:
            print(f"Offer {self.offer_id}: {self.title} is now INACTIVE.")
        return self.is_active
    
