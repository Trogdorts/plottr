from series import Series

class Novel(Series):
    def __init__(self,
                 title = "Default Pony",
                 genre = "science Fiction",
                 subgenre = "space opera",
                 AVG_SENTENCE_LENGTH = 16,
                 AVG_CHAPTER_LENGTH = 2500,
                 WORD_COUNT = int(100000),
                 PARTS = 3
    ):
        
        
        self.title = title
        self.genre = genre
        self.subgenre = subgenre
        self.AVG_SENTENCE_LENGTH = AVG_SENTENCE_LENGTH
        self.AVG_CHAPTER_LENGTH = AVG_CHAPTER_LENGTH
        self.WORD_COUNT = WORD_COUNT
        self.PARTS = PARTS
        
        print("Created new novel.")
        
        
    def get_title(self):
        return self.title


