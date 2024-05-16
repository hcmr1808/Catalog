from faker import Faker
from src.Domain.Entity.Category import Category

class CategoryTestFixture:
    def __init__(self):
        self.fake = Faker()

    def GetValidCategoryName(self):
        category_name = ""
        while len(category_name) < 3:
            category_name = self.fake.name()
        if len(category_name) > 255:
            category_name = category_name[:255]
        return category_name

    def GetValidCategoryDescription(self):
        categoryDescription = self.fake.text()
        if len(categoryDescription) > 1000:
            categoryDescription = categoryDescription[:1000]
        return categoryDescription
    
    def GetValidCategory(self):
        valid_name = self.GetValidCategoryName()
        valid_description = self.GetValidCategoryDescription()
        return Category(valid_name, valid_description)


