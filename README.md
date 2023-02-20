# white-rabbit <img align="right" width="210" height="300" src="https://raw.githubusercontent.com/jgabrielfreitas/white-rabbit/master/art/white-rabbit.png">
`white-rabbit` is a log-decorator to take up the execution time of functions 

## installation 
```shell
$ pip install white-rabbit
```

## usage
``` python
import logging
import time
from white_rabbit.stopwatch import stopwatch

logging.basicConfig(level=logging.INFO)


@stopwatch(logger=logging)
def my_function():
    time.sleep(1)
    print("My function was executed.")


my_function()
```

---
And the output should be like
```
INFO:root:Running my_function...
INFO:root:my_function took 1.00473 seconds to run.
My function was executed.
```

## LICENSE
```
MIT License

Copyright (c) 2023 João Freitas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
