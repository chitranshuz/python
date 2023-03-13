official link : https://pillow.readthedocs.io/en/stable/handbook/tutorial.html

**Using the Image class**

The most important class in the Python Imaging Library is the Image class, defined in the module with the same name. You can create instances of this class in several ways; either by loading images from files, processing other images, or creating images from scratch.

To load an image from a file, use the open() function in the Image module:

```ruby
from PIL import Image
im = Image.open("hopper.ppm")
```

we can blur, change color, rotate and perform other actions like photo editing softwares. 

![image](https://user-images.githubusercontent.com/43988314/224648430-f6fdb5dc-3d90-48aa-8aa9-8d7cbf3dbd9c.png)
![image](https://user-images.githubusercontent.com/43988314/224648488-779419bb-d543-4c42-905e-72a3458bbec6.png)
![image](https://user-images.githubusercontent.com/43988314/224648523-35fe69c9-040d-4e03-b721-bd95aa3def1a.png)
