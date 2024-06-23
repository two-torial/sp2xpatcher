# Contributing

You may help the community by contributing patches.  

## How?

**Fork** the project, **add/modify** files, propose a **Pull Request** and we'll get to it asap.  
**Important Note:** When adding a new game version, add it to the [List of supported games](SUPPORTED.md) using the existing format, we won't merge your PR until you do.

Once a pull request is merged, patches will be available within minutes at `https://sp2x.two-torial.xyz/`

## Converting web to json (spice2x) patches

Right now **this has to be done manually**, however we plan on having tooling available to make this easier.  
Look at the files respective structures (html and json) and try to figure it out yourself.

## JSON Naming

**Spice2x patches have one json file per game version**.  
It needs to be **[named in a very specific way](https://github.com/spice2x/spice2x.github.io/wiki/patches.json-specification#pe-identifier)** to be recognized by the [Spice2x 'Import from URL'](https://github.com/spice2x/spice2x.github.io/wiki/Patching-DLLs-(hex-edits)#importing-patches-from-a-url) feature.

A python [peinfo.py](https://github.com/akitakedits/peinfo) script is available to help you figure that name out for your provided game's dll file.  
Check out [peinfo's README](https://github.com/akitakedits/peinfo/blob/main/README.md) for more information.
