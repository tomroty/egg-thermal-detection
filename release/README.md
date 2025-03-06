# Release

Final version of the project that works directly with the MLX90640 on a Raspberry Pi.

## Usage

### Auto (Linux only)
Simply run `start.sh`

### Manual

The code must be run on a Raspberry Pi with the MLX90640 connected and all the necessary libraries installed.

You need to compile `main.c` and then run the python script `main.py`.

Make sure the line below match the name and the path of your executable (default is "`detection`").

```python
process = subprocess.Popen(["./detection", "./input.txt"], stdout=subprocess.PIPE)
```
