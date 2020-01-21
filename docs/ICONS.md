# Icons

Icons for CameraHub were purchased from [Icons8](https://icons8.com/icons) in SVG vector format. At the time of writing, we are using
the [iOS set](https://icons8.com/icons/ios) in blue. The SVG files are placed unaltered in the `icons/svg/` directory in the root of this project.

There is a script to automatically generate sets of icons with the correct names, at the correct resolutions, in PNG format. It will **remove**
existing sets of icons at those resolutions that will be regenerated.

You must update the mapping between the original Icons8 filenames and the names that will be used in the application (usually the names of the Models).

For example, this command will generate two sets of icons, in 50x50 and 100x100 resolution, and place them in `schema/static/icons/` where they can be used:

```sh
cd icons
./generate-icons.pl 50 100
```
