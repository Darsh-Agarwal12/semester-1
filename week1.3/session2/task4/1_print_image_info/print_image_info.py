# Week 1.3, Session 2: Print PGM image info

try:
    with open('/workspaces/semester-1/week1.3/session2/task4/images/feep.pgm', 'r') as f:
        # Read lines, stripping whitespaces
        lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Filter out any comment lines starting with '#'
        header_data = []
        for line in lines:
            if not line.startswith('#'):
                header_data.extend(line.split())
                
        # A valid PGM header contains at least: Magic Number, Width, Height, Max Gray Value
        if len(header_data) >= 4:
            magic_number = header_data[0]
            width = header_data[1]
            height = header_data[2]
            max_gray_value = header_data[3]
            
            # Print dimensions and max gray value exactly as requested
            print(f"Dimensions: {width} x {height} pixels")
            print(f"Max Gray Value: {max_gray_value}")
        else:
            print("Error: The file does not appear to be a valid PGM format header.")

except FileNotFoundError:
    print(f"Error: The file could not be found. Please check the name and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")