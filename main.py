from website import create_app
import os
import cv2
import matplotlib.pyplot as plt
from PIL import Image
app = create_app()

if __name__ == '__main__':
    #path
    path='images'
    images=os.listdir(path)
    type(images)
    print(len(images))
    img_data=[]
    for img in images:
        img_arr=cv2.imread(os.path.join(path,img))
        img_data.append(img_arr)
        
    plt.figure(figsize=(10,10))
    for i in range(len(img_data)):
        plt.subplot(6,6,i+1)
        plt.imshow(img_data[i])


    file = "C:/Users/Desktop/Documents/FYP/images/img1.jpg"
    image = Image.open(file)
    image.show()
    app.run(debug=True)

