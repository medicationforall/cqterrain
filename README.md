# cqterrain
Helper Libary to Generate 3d models of buildings / terrain using CadQuery.

## Documentation 
* [Damage](documentation/damage.md)
* [Greeble](documentation/greeble.md)
* [Minibase](documentation/minibase.md)
* [Pipe](documentation/pipe.md)
* [Roof](documentation/roof.md)
* [Stairs](documentation/stairs.md)
* [Tile](documentation/tile.md)
* [Window](documentation/window.md)
* [Misc](documentation/misc.md) aka everything else
  * door
  * ladder
  * obelisk
  * stones
  * support

## Changes
* [Changelog](./changes.md)

## Dependencies
* [CadQuery 2.x](https://github.com/CadQuery/cadquery)
* [cqMore](https://github.com/JustinSDK/cqMore)
* [cadqueryhelper](https://github.com/medicationforall/cadqueryhelper)

---


## Installation
To install CQ Terrain directly from GitHub, run the following `pip` command:

	pip install git+https://github.com/medicationforall/cqterrain

**OR**

### Local Installation
From the cloned cqterrain directory run.

	pip install ./

---

## Running Example Scripts
[example_runner.py](example_runner.py) runs all examples.

``` bash
C:\Users\<user>\home\3d\cqterrain>python example_runner.py
```

**OR**

### Running individual examples
* From the root of the project run one of the example scripts:
  
``` bash
C:\Users\<user>\home\3d\cqterrain>python ./example/stairs.py
```
