# rFactor 2 VEH Generator
Generates .VEH files from a csv file and DDS files.
Configurable (soon, tm).

## Prerequisite
Install latest Python https://www.python.org/downloads/
Important to select add Python to PATH at installation

## The data.csv and base.VEH
The `data.csv` and `base.VEH` are heavily interlinked.
the `base.VEH` will be used as the template for the final results.
Inside `base.VEH` you can see words that are wrapped with {}, that means
it will be replaced from data inside the `data.csv`

Future updates will enable you to add custom keywords by yourself so it's
not fixed/hardcoded with the current keywords.
For the time being, if you want to use another VEH template. This is the list
of keywords that can be put into your `VEH` file 
(remember to wrap them with {})

1. {NUMBER}
2. {SKIN_FILE}
3. {TEAM}
4. {CLASS}
5. {NAME}

Keywords can be duplicated inside the `VEH` file.

## Guest skin
If you want to have guest skin, just provide the exact file `guest_alt.dds`
in your input folder.

## Guide
1. Put your dds files inside input folder
2. the format of DDS files must be `xx_alt.dds` otherwise it will be skipped
3. `base.VEH` is the base template, change it to your vehicle `VEH`.
    Use `base.VEH` as an example on how to interpolate data from CSV into your
    vehicle's `VEH`
4. open cmd and type `python veh_generator.py`
    (if it doesn't work try to change to `python3`)
5. Your `VEH` files and `DDS` files will be compiled inside `output` folder
    and ready to be packaged via MAS

