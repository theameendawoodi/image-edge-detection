import numpy as np
import cv2

def edge_detection(image,destination_path):
    kernel1=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
    kernel2=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    gray_img=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges=cv2.filter2D(gray_img,-1,kernel1)
    edge=cv2.filter2D(edges,-1,kernel2)
    cv2.imwrite(destination_path,edge)
    return 0

image_destination=input("enter the path of the image")
dest_file=input("ewnter the name of the output image")
image=cv2.imread(image_destination)
edge_detection(image, dest_file)