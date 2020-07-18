# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('meme2.png')

    # add text to the top and bottom of the meme
    meme_gen.add_text("int C = 0, Me = 0;", 85, 0, 40, 'black')
    meme_gen.add_text("C++, Me += 0;", 110, 410, 40, 'black')

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()
