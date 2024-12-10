# Check if the file "./detection" exists
if [ ! -f "./detection" ]; then
    # If it does not exist, compile all .c files into an executable named "detection"
    gcc *.c -o detection
fi

# Activate the Python virtual environment
source venv/bin/activate

# Run the Python script
python3 main.py