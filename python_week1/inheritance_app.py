class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def display_info(self):
        return (
            f"Username: {self.username}\n"
            f"Email: {self.email}\n"
        )
    
class AdminUser(User):
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    def display_info(self):
        return (
            f"{super().display_info()}"
            f"Admin Level: {self.admin_level}\n"
        )
    
if __name__ == "__main__":
    user = User("kishen", "kishen@example.com")
    admin = AdminUser("admin_k", "admin@example.com", 3)

    print(user.display_info())
    print(admin.display_info())
