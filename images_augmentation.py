from imgaug import augmenters as aug
import cv2
import glob
images_path=glob.glob("images/*.webp")
images=[]
for img_path in images_path:
    img=cv2.imread(img_path)
    cv2.imshow("image",img)
    images.append(img)
    
# Augmentation 
augmentation =aug.Sequential([
   aug.Fliplr(1),
   aug.Flipud(1), 
   aug.Rotate((-50,50)),
   aug.Crop(percent=(0, 0.3)),
   aug.KMeansColorQuantization(), 
   aug.UniformColorQuantization(),
   aug.GaussianBlur(sigma=(0.0, 3.0)),
   aug.AdditiveGaussianNoise(scale=0.1*255),
   aug.Affine(translate_percent={"x":(-0.5,0.5)})
])
augmented_images=augmentation(images=images)
for img in augmented_images:
    cv2.imshow("image_augmented",img)
    cv2.waitKey(0)