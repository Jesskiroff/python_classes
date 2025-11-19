class User: #python classes are written in PascalCase
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        
user_1 = User("001 ", "Jess")

print(user_1.id)