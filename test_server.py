import pytest
#from main2 import *

#test predict function
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

# def test_predict():
#     assert 3==5


# def test_connection():
#     client = app.test_client()
#     url = '/dogs.html'
#     response = client.get(url)
#     assert response.status_code == 200
#     assert b"Small Breeds" in response.data
#     assert b"Large Breeds" in response.data
#     assert b"HDB Approved" in response.data

# def test_yolo_model():
#     sample_image = "test.jpg"
#     yolo_model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')
#     yolo_output = yolo_model(image1)
#     url = '/dogs.html'
#     response = client.get(url)
#     assert response.status_code == 200
#     assert b"Small Breeds" in response.data
