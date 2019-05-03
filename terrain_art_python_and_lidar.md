# Terrain, Art, Python, and LiDAR

Cool hacker/maker talk about using public data for 3d art with 3d printers and mills.

Where does Andrew go to make this stuff? London or SF? Not Noisebridge...

- Speaker: Andrew Godwin
  - Django, Migrations, South
  - Owns a lot of lasers
  - Works at eventbrite in SF
- Online resources:
- PyCon Description: https://us.pycon.org/2019/schedule/presentation/151/

github.com/andrewgodwin/gis_tools
github.com/andrewgodwin/lidartile



## Legacy of mapping in civilization

- Put 2 giant radars on a space shuttle and flew around the entire earth to get a complete height map
  - About 30 meters accuracy
  - Great for islands, mountains, valleys.
    - Cannot see behind mountains - missing data due to angle of shuttle 
  - whole data about a gigabyte

## Lets add lasers - now we have space and lasers
 
- Lidar radio rangefinding
- Down to the centimeter accuracy
- Incredibly detailed but of a smaller area
- Lidar planes regularly fly over cities and map them entirely
- Cities, you can see individual trees, it's extremely precise and huge...


## Ok lasers, python, stuff, let's make things

1. Laser-cut profiles

- DEM: Digital Elevation Model
  - bitmap
  - height map
  - in the greyscale renderings shown, white is highest, black lowest, just a 2d array, value for each point on the array
667229
  - convert DEM to CSV to make it easy
  - Pick on in n rows, draw a contour with `svgwrite` library
  - scotland didn't really look good in the cross-section, hawaii is perfect... it depends


## Full detail map of San Francisco

- I would like one of these for my wall, what does it weigh? Can I have the rendered and chopped STL files that he used?
  - ACTION: email and ask Andrew Godwin for the san francisco STL files... maybe they are on his github
- Zoomed in there is no continuous surface, you can't print it in the raw lidar form.
  - How do we convert the raw file of 3d vectors (x, y, z) into a solid model?
  - python-pcl -- python point cloud library, returns height map from vectors.
  - lastools not free but free for small amounts of data - does the same thing for money
  - load DEM, clip height top+bottom, smooth rough features, then write out an STL file
    - smoothing pass is an array pass in python, because the laser data has noise, from reflections, etc
    - andrew generated his own STL files with struct.pack
    - struct.pack( stuff ) - see photo on my camera
  - should i have used numpy? yes... did I... no!  i should have, but i was just full speed.


## CNC Milled national parks

- Andrew Godwin goal of visiting all 59 national parks in the US
  - several alaskan are fly in only
  - some are boat only
  - some you need a boat to get to the other half of the park
- Made miniature maps of national parks out of metal
- viewer.nationalmap.gov - US National DEM
- get national park coordinates or something - a national park website in the slides
- use QGIS to cut out map
  - unfortunately their DEM has something off.. he explained it but it isn't in the slides.
- use STL again for milling machine
- huge wrinkle: 
  - map projections, some work great at equator and terrible at poles
  - projection in alaska looks terrible in lower 48 states...
  - no consensus on which projection to use with the lidar data
  - projections made the list of things i refuse to work with
- gcode, same as 3d printers, 8 hours milling each, breaking bits, very painful
  - would be great to send python directly to gcode machine instead of converting over an hour
- need better stl optimization, millions of polygons is not great
  - fusion360 just quit
  - run mesh optimizer in blender, computer completely unrespomnsive for 5 mins
    - would be great with python+numpy for optimization
  - once optimized, move to fusion360

