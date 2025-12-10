class User:
    def __init__(self, name, adress, phone, email, date_register, password, status ):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.email = email
        self.date_register = date_register
        self.password = password
        self.status = status
    def check_password(self, password: str) -> bool:
        return self.password == password
    def to_dict(self)-> dict: 
        return{
            'name': self.name
        }
if __name__ == '__main__':
    user = User ( 'joao', 'rua' ,'joao', 'joao@joao.com', '09/12/25', 'senha', 'ativo' )
    print(user.to_dict())
    print(user.check_password('ssenha'))
    print(user.check_password('senha'))