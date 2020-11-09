from universe import Universe

class Series(Universe):
    def __init__(self, novels = []):
        self.novels = novels
        print("Created new series.")
        
        
        
    def add_novel(self, novel):
        self.novels.append(novel)

    def get_novels(self):
        print(self.novels)
        return self.novels