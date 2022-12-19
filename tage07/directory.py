class Directory:
    def __init__(self, level = -1, name = "=", size = 0, father):
        self.level = level
        self.name = name
        self.size = size
        self.father = father