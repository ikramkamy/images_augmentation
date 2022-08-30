from imgaug import augmenters as iaa
import cv2
import glob
images_path=glob.glob("images/*.webp")
images=[]
for img_path in images_path:
    img=cv2.imread(img_path)
    cv2.imshow("image",img)
    images.append(img)
    
# Augmentation 
augmentation =iaa.Sequential([
   iaa.Fliplr(1),
   iaa.Flipud(0.5), 
   iaa.Affine(translate_percent={"x":(-0.5,0.5)})
])
augmented_images=augmentation(images=images)
for img in augmented_images:
    cv2.imshow("image_augmented",img)
    cv2.waitKey(0)