# Demo

Demo version of the project to test the function locally.

## Usage

### Auto (Linux only)
Simply run `start.sh`

### Manual
You need to compile `main.c` and then run the python script `main.py`.

Make sure the line below match the name and the path of your executable (default is "`detection`").


```python
process = subprocess.Popen(["./detection", "./input.txt"], stdout=subprocess.PIPE)
```

It is possible to replace the default input, either replace the default one or change the path in the line above.

Check the `/Input` folder for more infos.