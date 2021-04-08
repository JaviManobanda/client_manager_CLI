import uuid


class ClientModel:
    """Client models

        Args:
            name ([type]): [description]
            company ([type]): [description]
            mail ([type]): [description]
            position ([type]): [description]
            uid ([type], optional): [description]. Defaults to None.
    """

    def __init__(self, name, company, email, position, uid=None):

        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)  # convierte nuestro objeto en diccionario

    @staticmethod  # crea un metodo estatico
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
