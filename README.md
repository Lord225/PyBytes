# PyBytes

Tools written in python for quick bit manipulation on arbitrary sized number. 
It aims to:
* Make it simpler to swap bits than with native python ints
* Correctly wraps numbers in arithmetic operations
* Emulates behavior of unsigned, signed and Sign-module
* Try not to be pathetically slow

Example use:
```py
from pybytes import *

# creating new number, size is inferred from parameter
x = Binary('0110')
print(x, len(x)) # prints '0110 4'

y = Binary('1110')

# Arithmetic correctly wraps
print(int(x+y)) # prints 4

# But you can check status of operation
print(ops.flaged_add(x, y)) # flaged_add returns tuple: (0100, Flags(of=True, zf=False, sf=False, pf=False)), where object Flags contains status of operation.

x[0] = True  # Set first bit to High
print(x[:3]) # prints first 3 bits.

x[:3] = "010" # sets first 3 bits to '010'
print(x) # '0010'
```

This module contains some tools to work with float point numbers

```
from pybytes import *

f = floats.CustomFloat(preset='fp16') # Create 16 bit float point https://en.wikipedia.org/wiki/Half-precision_floating-point_format
print(f(0.25)) # Convert python float to custom value
print(f('0x3c00')) # prints 1.0 becouse hexadecimal 
print(f(2.0).as_hex()) # prints 2.0 in fp16 in hex

f2 = floats.CustomFloat(mantissa_size=3, exponent_size=3)

print(f2(f2(4.256))) # 4.256 is wraped to 4.0 becouse it is impossible to express with this float.
```
