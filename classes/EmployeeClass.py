class Employee:
    def __init__(self, manager, user, contactInfo):
        self._manager = manager
        self._user = user
        self.contact_info = contactInfo

    def get_manager(self): return self._manager

    def set_manager(self, manager):
        if not isinstance(manager, Employee): raise TypeError("Employee must be of Type Employee")

    # TODO: create Employee model
    def save(self):
       pass
       """
        user = User.objects.create(id=self.id, password=self.password,
                                   first_name=self.first_name, last_name=self.last_name,
                                   email=self.email, role=self.role,
                                   phone_number=self.phone_number, address=self.address)
        return f"{user.first_name} {user.last_name} with role {self.role} saved to database"
        """
