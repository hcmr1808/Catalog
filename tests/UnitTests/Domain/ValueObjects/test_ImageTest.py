from faker import Faker

from src.Domain.ValueObjects.Image import Image

faker = Faker()

def test_Instantiate():
    path = faker.image_url(width=640, height=480)
    image = Image(path)

    assert image.path == path

def test_EqualsByPath():
    path = faker.image_url(width=640, height=480)
    image = Image(path)
    sameImage = Image(path)

    IsItEqual = image == sameImage

    assert IsItEqual

def test_DifferentPath():
    path = faker.image_url(width=640, height=480)
    differentPath = faker.image_url(width=640, height=480)
    image = Image(path)
    differentImage = Image(differentPath)

    isItDifferent = image != differentImage

    assert isItDifferent

