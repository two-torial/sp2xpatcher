# Contributing

*You may help the community by contributing patches.*

## How?

1. **Fork** the project if you don't already have it
2. **Add/Modify/Stage/Commit** files as necessary **BUT don't Push/Sync them yet**
3. **Run** the `checks.py` script with `python checks.py`
4. If the script did anything: **Commit** its changes
5. **Push/Sync** the changes to your repo
6. **Propose a Pull Request** and we'll get to it asap

Once a pull request is merged, patches will be available within minutes at `https://sp2x.two-torial.xyz/`

### /!\ Important Note 
When adding a new game version, add it to the [List of supported games](SUPPORTED.md) using the existing format, we won't merge your PR until you do.

## JSON Naming

**Spice2x patches have one json file per game version**.  
It needs to be **[named in a very specific way](https://github.com/spice2x/spice2x.github.io/wiki/patches.json-specification#pe-identifier)** to be recognized by the [Spice2x 'Import from URL'](https://github.com/spice2x/spice2x.github.io/wiki/Patching-DLLs-(hex-edits)#importing-patches-from-a-url) feature.

A python [peinfo.py](https://github.com/akitakedits/peinfo) script is available to help you figure that name out for your provided game's dll file.  
Check out [peinfo's README](https://github.com/akitakedits/peinfo/blob/main/README.md) for more information.

## Converting web to json (spice2x) patches

Right now **this has to be done manually**, however we plan on having tooling available to make this easier.  
Look at the files respective structures (html and json) and try to figure it out yourself.

## Porting spice2x patches

It is possible to port patches from **one version of a game to another**.  
A python [port_sp2x_patches.py](https://github.com/akitakedits/port_sp2x_patches) script is available to help you through some of that work.  
However it will **not be able to port all patches** and it will **not always be 100% accurate**, **false positives can occur**.  
Porting patches the script cannot, or fixing false positives will have to be done manually.