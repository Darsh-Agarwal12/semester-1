# Week 1.3, Session 2: Validate image

try:
    with open('/workspaces/semester-1/week1.3/session2/task4/images/gradient.pgm', 'r') as f:
        # Read all lines and filter out empty ones
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
    # Filter out PGM comment lines starting with '#'
    tokens = []
    for line in lines:
        if not line.startswith('#'):
            tokens.extend(line.split())
            
    if len(tokens) < 4:
        print("Error: Invalid or corrupt PGM file header.")
    else:
        magic_number = tokens[0]
        specified_width = int(tokens[1])
        specified_height = int(tokens[2])
        max_gray_value = int(tokens[3])
        
        # Everything after the first 4 tokens is pixel data
        pixel_tokens = tokens[4:]
        
        # Check 1: Validate Pixel Values
        pixels_valid = True
        for p in pixel_tokens:
            val = int(p)
            if val < 0 or val > max_gray_value:
                pixels_valid = False
                break
        
        if not pixels_valid:
            print("Invalid pixel values")
        else:
            # Check 2: Validate Dimensions
            # Total pixels read must equal expected width * height
            total_pixels = len(pixel_tokens)
            
            # We assume a row layout optimization step to determine if width vs height broke:
            # If total pixels matches neither, we calculate if a specific dimension holds up.
            if total_pixels != (specified_width * specified_height):
                # Standard convention for checking dimension mismatch when length fails:
                # If it's a perfect multiple of width but not height, height is wrong.
                if total_pixels % specified_width == 0:
                    print("Invalid height")
                else:
                    print("Invalid width")
            else:
                print("Valid image")

except FileNotFoundError:
    print(f"Error: The file could not be found.")
except ValueError:
    print("Error: Could not parse image values (non-integer data found).")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
