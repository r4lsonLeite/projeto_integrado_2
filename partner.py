class Partner:
    def __init__(self, partner_id, name, partner_type, contact):
        self.partner_id = partner_id
        self.name = name
        self.partner_type = partner_type
        self.contact = contact
    def publish_service(self, service_name, service_description):
        print(f"Partner {self.name} successfully published service: {service_name}")
        return True

