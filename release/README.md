# Release

Final version of the project that works directly with the MLX90640 on a Raspberry Pi.
The code includes a firebase database connection but it is disabled by default because a token is required.

## Usage

### Auto (Linux only)
Simply run `start.sh`

### Manual

run this line to enter the virtual environment (required for dependencies)

`source venv/bin/activate`


You need to compile `main.c` and then run the python script `main.py`.

Make sure the line below match the name and the path of your executable (default is "`detection`").

```python
process = subprocess.Popen(["./detection", "./input.txt"], stdout=subprocess.PIPE)
```
