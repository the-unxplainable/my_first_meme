from simpleimage import SimpleImage

FONT_FILE = 'Impact.ttf'
# For custom colours use:- color='rgb(0, 0, 0)'

class MemeGenerator:
    # Initialize the important variables i.e. tex and filename
    def __init__(self, filename):
        # it's basically the constructor which initializes the meme's image, 
        # and accepts as a parameter the filename of the image
        self.text=[]
        self.filename=filename

    # We never called this method but it can be used to updTate the image during runtime
    def set_image(self, filename):
        self.filename=filename
        
    # We called 'add_text' in 'memegen_test.py' twice to pass values
    # Passed values are 'Cutom text', x-coordinate of the text and y-coordinate of the text
    def add_text(self, text, x, y, size, color):
        self.text.append((text, x, y, size, color))

    def render(self):
        img = SimpleImage(self.filename)
        for text, x, y, size, color in self.text:
            img.create_text(text,x,y, FONT_FILE, size=size,color=color)
        img.show()