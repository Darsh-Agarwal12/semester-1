import math
from image import Image  

class LookupTable:
    def __init__(self):
        """Initialise a default identity LUT where output equals input."""
        self.table = list(range(256))

    def display(self):
        """Prints the mapping of pixel values performed by the LUT."""
        print("Index -> New Value")
        for i in range(256):
            print(f"{i:3d} -> {self.table[i]:3d}")

    def apply_in_place(self, img: Image):
        """Modifies the given image directly using the LUT.
        
        Takes advantage of the __setitem__ method in image.py.
        """
        for i in range(img.width * img.height):
            # Uses __getitem__ via img[i] and __setitem__ via img[i] = ...
            original_pixel = img[i]
            img[i] = self.table[original_pixel]

    def apply(self, img: Image) -> Image:
        """Passes the given image through the LUT, returning a new image copy.
        
        Uses the exact .copy() method available in your image.py.
        """
        new_img = img.copy()  # Direct usage of your deepcopy wrapper
        
        for i in range(img.width * img.height):
            new_img[i] = self.table[img[i]]
        return new_img


class InvertLUT(LookupTable):
    def __init__(self):
        """Initialise an inverting LUT."""
        super().__init__()
        self.table = [255 - x for x in range(256)]


class ContrastLUT(LookupTable):
    def __init__(self):
        """Initialise a non-linear scaling LUT (Square Root scaling example)."""
        super().__init__()
        self.table = [int(math.sqrt(x / 255.0) * 255) for x in range(256)]


def main():

    try:
        print("Reading source image...")
        img = Image.read("/workspaces/semester-1/week1.6/session2/images/coins.pgm")
    except FileNotFoundError:
        print("Error: 'input.pgm' not found. Please provide a valid PGM file.")
        return

    invert_lut = InvertLUT()
    contrast_lut = ContrastLUT()

    print("Applying Inversion LUT (creating a copy)...")
    inverted_img = invert_lut.apply(img)
    inverted_img.write_pgm("output_inverted.pgm")
    print("Saved: output_inverted.pgm")

    print("Applying Contrast Enhancement LUT (in-place modification)...")
    contrast_lut.apply_in_place(img)
    img.write_pgm("output_contrast_enhanced.pgm")
    print("Saved: output_contrast_enhanced.pgm")

if __name__ == "__main__":
    main()
