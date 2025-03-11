import pathlib

# Define the path to the desktop directory
desktop = pathlib.Path(r"C:\Users\saura\OneDrive\Desktop")

# Iterate over directory contents and print them
for item in desktop.iterdir():
    print(item)
