## Main wip

## 3.4.1
* Update to cadqueryhelperversion 1.5.0
* Changed from using assembly.save (deprecated) to assembly.export

## 3.4.0
* Updated min python version 3.10
* Update to cadqueryhelperversion 1.5.0
* Added door TiledDoor handle parameters. Updated example, and documentation.
  * handle_mirrored:bool
  * handle_handle_length:float
  * handle_base_chamfer:float
* Cleaned up instances where I was setting the callback parameter for workplane.eachpoint invocations.
  * https://github.com/CadQuery/cadquery/issues/1395


## 3.3.0
* Added roof tile_alt

## 3.2.1
* Fix a bug with how the keep blocks are generated in stucco_brick_blocks.
* Refactored stucco_brick_blocks.
* Fix where the stucco example is writing it's stl file to the right location.

## 3.2.0
* Added material stacked_wave_from_map
* Added material stucco_brick_blocks
* Added examples for stucco_brick_blocks
* Updated material documentation

## 3.1.0
* Added build_plate for CrystalWall
* Added build_assembly for CrystalWall

## 3.0.1
* wired up crystal wall base_peak_count and added base_segments parameter

## 3.0.0
* Changed the crystal wall api. 
* Added additional parameters to the crystal wall.
  * Made height an optional tuple
  * removed min_height
  * Added render_crystals boolean parameter.
  * Added additional crystal tuple parameters.
  * Added base parameters.

## 2.8.2
* Fix walkway documentation example import.

## 2.8.2
* Fix walkway rail chamfer bug due to length. 

## 2.8.1
* Fix book documentation link in readme.md

## 2.8.0
* Added book package
  * Added book
  * Added book_random
  * Added books
  * Added bookcase
  * added Bookcase class
  * Updated README.md


## 2.7.0
* Fixed source file paths in damage.md
* door Hatch removed unused parameter
* Added uneven textured minibases
  * Added uneven textured slotted base
  * Added uneven textured circular base
  * Added uneven textured hexagon base
  * Added uneven textured rectangle base
  * Added uneven textured ellipse base
  * Added Uneven minibase group example
* Added crystal package
  * Added crystal_random
  * Added Crystal Wall
* Added license blocks 

## 2.6.0
* Moved skirmishbunker BlastDoor, Hatch and SplitDoor code into cqterrain door.

## 2.5.0
* Move cqportal shieldwall code into cqterrain.
* Updated README.md

## 2.4.0
* Upgrade cadqueryhelper to 1.4.2
* Added tile truchet_circle_three, example, and documentation

## 2.3.0
* Added tile truchet_circle_two, example, and documentation

## 2.2.0
* Upgrade cadqueryhelper to 1.4.1 - Added uneven_spline
* Added damage uneven_spline_plane
* Updated damage documentation

## 2.1.0
* Move cqspoolterrain.spool code, examples, documentation into cqterrain.spool

## 2.0.3
* Added industrial pipe annotations
* Added industrial stair annotations
  
## 2.0.2
* Bit by windows file case insensitive files
  
## 2.0.1
* Cleaned up IndustrialStairs example

## 2.0.0
* Upgrade cadqueryhelper to 1.3.0 - resolves numpy issue
* Move cqspoolterrain.pipe code into cqterrain.pipe
* Move cqspoolterrain.industrial_stairs code into cqterrain.stairs
* Move cqindustry barrier code into cqterrain.barrier
* Move cqindustry walkway code into cqterrain.walkway
* Resolved a bug with the industrial pipe generation.

## 1.2.4
* Make seed nullable for uneven terrain generation 

## 1.2.3
* Fix Dwarf Star union bug when using with rarray

## 1.2.2
* Fix Dwarf Star union bug when using with rarray

## 1.2.1
* Added license blocks
* Added dwarf_star tile
* Fixed door documentation

## 1.2.0
* Refactored stairs into own module
* Moved stones into material module, and Added Material.md documentation
  * Added center_blocks
  * Added tower_stones
  * Added uneven_blocks
  * Added uneven_centered_blocks
* Added documentation.md index
* Added stairs round module, documentation, and examples
  * Added greebled_stairs
  * Added outline
  * Added plain stairs
  * Added Ramp 

## 1.1.2
* Added damage uneven plane
  * Added documentation
  * Added examples 
* Added HeavyDoor to door module
* Updgraded cadqueryhelper version 1.2.5
  * Added uneven wave


## 1.1.1
* Added bridge TileStraight
  * Added example
  * Added Documentation
* Fixed bridge BaseStraight example
* Added bridge TileBridge
  * Added example

## 1.1.0
* Added bridge module
  * Added BaseRamp
  * Added BaseStraight
  * Added Bridge orchestrator
  * Added Examples
  * Added Documentation
* Updated README.md

## 1.0.4
* Updgraded cadqueryhelper version 1.2.3
  * Upped cadquery to version 2.4.x 

## 1.0.3
* Updgraded cadqueryhelper version 1.2.2

## 1.0.2
* Updgraded cadqueryhelper version 1.2.1

## 1.0.1
* Updgraded cadqueryhelper version 1.2.0

## 1.0.0
### Overview
* Updated every file
* Added type annotations
* Documented all modules
* example_runner.py runs all examples
* Updgraded cadqueryhelper version 1.1.2
* Added missing license blocks

## Breaking
* I believe roof import path may have changed.
* stone.make_stones algorithm generates different outputs.
* rivet tile now places its rivets on top of the tile face. 
  * As opposed to inside the center of the object and just lackadaisically poking through.

### Details
* Updated README.md
* Renamed out directory to stl
* Removed old files
* Split window.py file out into it's own package. Added annotations, examples, and documentation.
  * casement
  * cinquefoil
  * cinquefoil_frame
  * frame
  * grill
  * lattive_fancy
  * lattice
* Split roof.py file out into it's own package. Added annotations, examples, and documentation.
  * angle
  * gable
  * hip
  * shell
  * tiles
* Split out minibase.py methods into it's own package. Added annotations, examples, and documentation.
  * circle
  * ellipse
  * Added hexagon
  * make_magnet_outline
  * recangle
  * slot
* Moved building files into their own package
* Moved spokedWheel from tile to greeble package and updated documentation
  * Moved greeble examples
* Made door into it's own package
* Annotated packages:
  * tile
  * greeble
  * damage
  * window
  * pipe
  * Ladder
  * obelisk
  * roof
* Added damage documentation.
* Added pipe documentation.
* Added misc documentation.
  * door
  * ladder
  * obelisk
  * make_stones
  * support
* Added tile.truchet_triangle
* Added tile.truchet_circle
* Added example_runner.py
* Refactored make stones to no longer use an assembly
* Building changes
  * Refactored wall
  * Changed example output paths to have building prefix
  * Refactored Room
* Added Board; with example, and documenation
* Added gothic_one greeble, with example and documentation
* Added pull_hande door, with example and documentation
* Fixed tile rivet bug.
* Documented Truchet Circle tile.
* Documented Truchet Triange tile. - that's a rabbit hole.
* Fix rivet_round tile padding parameter now does something.
* Added TilesPlate to tile package

## 0.3.3
* Upped cadqueryhelper version 0.2.1
  * Added shape.coffin

## 0.3.2
* Papercut fixes

## 0.3.1
* Added pipe.corrugated_straight
* Added tile.apricorn
* Added tile.bolt_panel
* Added tile.charge
* Added tile.conduit
* Added tile.carton
* Added tile.carton2
* Tile documentation and examples for apricorn, bolt_panel, charge, glyph, conduit, carton, carton2

## 0.3.0
* Upped cadqueryhelper version 0.2.0
  * "Base" class refactoring 

## 0.2.1
* Added damage.grid_seed
* Added blast grid examples.

## 0.2.0
* Added damage module and created blast template code.

## 0.1.9
* Added tile rivet_round
* Added tile spoked_wheel

## 0.1.8
* Upped cadqueryhelper version

## 0.1.7
* Upped cadqueryhelper version

## 0.1.6
* Updated the license
* Cleaned up install dependencies

## 0.1.5
* Split out tile.py code into separate files.
* moved tile examples into separate folder
* Added Apache 2 License headers to source files
* Added new tiles
  * Plain
  * Chamfer_frame
  * Rivet
  * Slot
  * Slot Diagonal
  * Glyph - experimental
* Added tile documentation.

## 0.1.4
* Added Obelisk code and examples
* Upped dependency version of cadqueryhelper to 0.1.1

## 0.1.3
* Added Greeble Vent
  * Added documentation
* Upped required cadqueryhelper version to 0.1.0
* Fix octagon tile not centering correctly

## 0.1.2
* Jamie Broke the __init__.py at the root directory

## 0.1.1
* Updated cadquery version
* Upped cadqueryhelper version to 0.0.8
* * Attempt to fix __init__.py references

## 0.1.0
* Added Star Tile
* Added Windmill Tile

## 0.0.5
* Modify octagon_with_dots to use union.
* octagon_with_dots added tile_height param.

## 0.0.4
* initial Release
