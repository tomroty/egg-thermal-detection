# Check if the file "./detection" exists
if [ ! -f "./detection" ]; then
    # If it does not exist, compile all .c files into an executable named "detection"
    gcc *.c -o detection
fi


# uncomment and edit the following lines if you are using a virtual environment
# VENV_PATH="/absolute/path/to/venv"
# source "$VENV_PATH/bin/activate"

# Run the Python script
python3 main.py
