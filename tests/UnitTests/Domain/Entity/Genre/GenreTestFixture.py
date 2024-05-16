from faker import Faker
from src.Domain.Entity.Genre import Genre
import uuid
from typing import List

class GenreTestFixture:
    def __init__(self):
        self.fake = Faker()
    
    def GetValidGenreName(self):
        genreName = self.fake.name()
        return genreName

    def GetExampleGenre(self, isActive:bool = True, categoriesIdsList: List[uuid.UUID] = None) -> Genre:
        genre = Genre(self.GetValidGenreName())
        if categoriesIdsList is not None:
            for categoryId in categoriesIdsList:
                genre.AddCategory(categoryId)
        return genre
        