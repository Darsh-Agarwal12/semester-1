# Week 1.3, Session 2: Invert PGM image

filepath = f"../images/plus.pgm"
output_filepath = f"../images/inverted_plus.pgm"

try:
    # 1. Open the pgm image file to read
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
    # Filter out comments
    tokens = []
    for line in lines:
        if not line.startswith('#'):
            tokens.extend(line.split())
            
    if len(tokens) < 4:
        print("Error: Invalid PGM header structure.")
    else:
        magic_number = tokens[0]
        width = int(tokens[1])
        height = int(tokens[2])
        max_gray = int(tokens[3])
        
        original_pixels = tokens[4:]
        
        # 2. Create inverted image using the formula
        inverted_pixels = []
        for p in original_pixels:
            invert_pixel_value = max_gray - int(p)
            inverted_pixels.append(invert_pixel_value)
            
        # 3. Write the inverted pgm image to a new file
        with open(output_filepath, 'w') as out_f:
            # Write required PGM header components
            out_f.write(f"{magic_number}\n")
            out_f.write(f"{width} {height}\n")
            out_f.write(f"{max_gray}\n")
            
            # Format and join pixel data with spaces as recommended
            string_line = " ".join(str(item) for item in inverted_pixels)
            out_f.write(string_line + "\n")
            
        print(f"Success! Inverted image written to: {output_filepath}")

except FileNotFoundError:
    print(f"Error: The file could not be found.")
except ValueError:
    print("Error: Corrupt pixel numerical data encountered during parsing.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
