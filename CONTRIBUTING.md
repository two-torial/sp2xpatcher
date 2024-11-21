# Contributing

*We welcome your contributions to enhance this patcher.*

## How to Contribute

1. **Fork the Repository**  
   If you haven't already, fork the repository to your GitHub account.

2. **Make Your Changes**  
   Add, modify, stage, and commit your changes locally. **Do not push/sync yet.**

3. **Run Checks**  
   Execute the `checks.py` script by running: `python checks.py`  
   If the script makes any changes, commit those changes.

4. **Push Your Changes**  
   Push/sync your changes to your forked repository.

5. **Submit a Pull Request**  
   Submit a pull request to the main repository. We will review it promptly, address any issues, and merge it.

Once your pull request is merged, the patches will be available within minutes at `https://sp2x.two-torial.xyz/`.

### Important Note
When adding a new game version, ensure it is included in the [List of Supported Games](SUPPORTED.md) using the existing format.  
**Your PR will not be merged until this is done.**

## JSON Naming

**Each Spice2x patch must have a separate JSON file for each game version.**  
The file must be [named according to specific guidelines](https://github.com/spice2x/spice2x.github.io/wiki/patches.json-specification#pe-identifier) to be recognized by the [Spice2x 'Import from URL'](https://github.com/spice2x/spice2x.github.io/wiki/Patching-DLLs-(hex-edits)#importing-patches-from-a-url) feature.

A Python script, [peinfo.py](https://github.com/akitakedits/peinfo), is available to help you determine the correct name for your game's DLL file.

## Creating Spice2x Patches

**To support a new game version, you need to create its Spice2x patches from scratch.**  
Hexadecimal signature matching can help in porting patches between different game versions.  
This method is not foolproof and patches could break if the game changes too much, but it's still highly effective for MOST patches.

**You can use the Python script [find_sp2x_patches.py](https://github.com/akitakedits/find_sp2x_patches) to facilitate this process.**