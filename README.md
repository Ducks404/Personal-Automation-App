How this automation folder works
========================
The main script that is being run constantly in the background is **app.py**
All the other python scripts in here are being imported and called in the main script.
When adding anything to the main script, please:
1. Make a new subclass of FileSystemEventHandler.
2. Add an exclude parameter that takes in a list defaulted to an empty list.
3. Describe clearly what the script does as a comment in the main script.