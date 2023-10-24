import os

upload = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "document", "testheadsculpture.jpg")

def get_testheadsculpture_path():
    return upload
