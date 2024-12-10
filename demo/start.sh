# Check if the file "./detection" exists
if [ ! -f "./detection" ]; then
    # If it does not exist, compile all .c files into an executable named "detection"
    gcc *.c -o detection
fi


# Run the Python script
python3 main.py
