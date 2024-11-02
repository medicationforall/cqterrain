# cqterrain
Helper Libary to Generate 3d models of buildings / terrain using CadQuery.

[![](documentation/image/building/17.png)](documentation/building.md)<br />

[![](documentation/image/tile/30.png)](documentation/tile.md)

## Project Documention
* [Documentation](documentation/README.md)
* [Bridge](documentation/bridge.md)
* [Building](documentation/building.md) 
* [Damage](documentation/damage.md)
* [Door](documentation/door.md)
* [Greeble](documentation/greeble.md)
* [Minibase](documentation/minibase.md)
* [Pipe](documentation/pipe.md)
* [Roof](documentation/roof.md)
* [Stairs](documentation/stairs.md)
* [Tile](documentation/tile.md)
* [Window](documentation/window.md)
* [Misc](documentation/misc.md) aka everything else
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
