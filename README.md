# [TWO-TORIAL](https://two-torial.xyz)'s Spice2x Patcher

### URL: `https://sp2x.two-torial.xyz/`

## About

This repo contains patches to use with [Spice2x 'Import from URL'](https://github.com/spice2x/spice2x.github.io/wiki/Patching-DLLs-(hex-edits)#importing-patches-from-a-url) feature.  
We'll be keeping the **repo public** and **url alive** for as long as possible, **feel free to [contibute patches](CONTRIBUTING.md)** for the community through pull requests!

## Usage

See our guide on [spice2x patching](https://two-torial.xyz/extras/patchsp2x/) and use the url provided above.

<details><summary><h2>Contributing</h2></summary>

You may help the community by contributing patches.  

## How?

**Fork** the project, **add/modify** files, propose a **Pull Request** and we'll get to it asap.  
**Important Note:** When adding a new game version, add it to the [List of supported games](SUPPORTED.md) using the existing format, we won't merge your PR until you do.

Once a pull request is merged, patches will be available within minutes at `https://sp2x.two-torial.xyz/`

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

</details>
<details><summary><h2>Supported Games</h2></summary>

*Click on a game's name to reveal supported versions.*

<details><summary><b>beatmania IIDX</b></summary>

<details><summary><b>beatmania IIDX 18 Resort Anthem</b></summary>

### [LDZ] `bm2dx.dll`
- 2011-07-12 - [JDZ-4e110e2b_ba839](JDZ-4e110e2b_ba839.json)

</details>
<details><summary><b>beatmania IIDX 19 Lincle</b></summary>

### [KDZ] `bm2dx.dll`
- 2012-09-03 - [KDZ-503f32fb_b6262](KDZ-503f32fb_b6262.json)

</details>
<details><summary><b>beatmania IIDX 20 tricoro</b></summary>

### [LDJ] `bm2dx.dll`
- 2012-09-19 - [LDJ-5052a3ea_c4112](LDJ-5052a3ea_c4112.json)
- 2013-09-09 - [LDJ-521ffeca_d8d73](LDJ-521ffeca_d8d73.json)

</details>
<details><summary><b>beatmania IIDX 21 SPADA</b></summary>

### [LDJ] `bm2dx.dll`
- 2013-10-02 - [LDJ-525394a7_d19f3](LDJ-525394a7_d19f3.json)
- 2014-07-16 - [LDJ-53bd1ab4_e7173](LDJ-53bd1ab4_e7173.json)
  
</details>
<details><summary><b>beatmania IIDX 22 PENDUAL</b></summary>

### [LDJ] `bm2dx.dll`
- 2014-09-17 - [LDJ-53ec605b_ccf53](LDJ-53ec605b_ccf53.json)
- 2015-08-05 - [LDJ-55b9eab9_f2d73](LDJ-55b9eab9_f2d73.json)

</details>
<details><summary><b>beatmania IIDX 23 copula</b></summary>

### [LDJ] `bm2dx.dll`
- 2016-08-31 - [LDJ-57ba48d8_e5d81](LDJ-57ba48d8_e5d81.json)

</details>
<details><summary><b>beatmania IIDX 24 SINOBUZ</b></summary>

### [LDJ] `bm2dx.dll`
- 2017-08-28 - [LDJ-599b7176_f4fb1](LDJ-599b7176_f4fb1.json)

</details>
<details><summary><b>beatmania IIDX 25 CANNON BALLERS</b></summary>

### [LDJ] `bm2dx.dll`
- 2018-09-19 - [LDJ-5b985f71_183324](LDJ-5b985f71_183324.json)

</details>
<details><summary><b>beatmania IIDX 26 Rootage</b></summary>

### [LDJ] `bm2dx.dll`
- 2019-09-02 - [LDJ-5d651fc5_415844](LDJ-5d651fc5_415844.json)
- 2019-10-07 - [LDJ-5d91850e_4158c4](LDJ-5d91850e_4158c4.json)

</details>
<details><summary><b>beatmania IIDX 27 HEROIC VERSE</b></summary>

### [LDJ-003] `bm2dx.dll`
- 2020-09-29 - [LDJ-5f713b52_6d4090](LDJ-5f713b52_6d4090.json)

### [LDJ-010] `bm2dx.dll`
- 2020-09-29 - [LDJ-5f713946_7f52b0](LDJ-5f713946_7f52b0.json)

</details>
<details><summary><b>beatmania IIDX 28 BISTROVER</b></summary>

### [LDJ-003] `bm2dx.dll`
- 2021-09-15 - [LDJ-613aa4d4_91aa00](LDJ-613aa4d4_91aa00.json)

### [LDJ-010] `bm2dx.dll`
- 2021-09-15 - [LDJ-613aa28a_9e58d0](LDJ-613aa28a_9e58d0.json)

</details>
<details><summary><b>beatmania IIDX 29 CastHour</b></summary>

### [LDJ-003] `bm2dx.dll`
- 2022-08-24 - [LDJ-63040c54_6679ac](LDJ-63040c54_6679ac.json)

### [LDJ-010] `bm2dx.dll`
- 2022-08-24 - [LDJ-63040b80_73273c](LDJ-63040b80_73273c.json)

</details>
<details><summary><b>beatmania IIDX 30 RESIDENT</b></summary>

### [LDJ-003] `bm2dx.dll`
- 2023-09-05 - [LDJ-64ef0ff5_1037754](LDJ-64ef0ff5_1037754.json)

### [LDJ-010] `bm2dx.dll`
- 2023-09-05 - [LDJ-64ef0ec9_844b10](LDJ-64ef0ec9_844b10.json)

### [LDJ-012] `bm2dx.dll`
- 2023-09-05 - [LDJ-64ef1153_777dc0](LDJ-64ef1153_777dc0.json)

</details>
<details><summary><b>beatmania IIDX 31 EPOLIS</b></summary>

### [LDJ-012] `bm2dx.dll`
- 2023-10-18 - [LDJ-65290d78_9254f0](LDJ-65290d78_9254f0.json)
- 2024-03-05 - [LDJ-65de809d_94e9bc](LDJ-65de809d_94e9bc.json)
- 2024-04-15 - [LDJ-661758fa_95ceec](LDJ-661758fa_95ceec.json)
- 2024-05-07 - [LDJ-662a0a1f_98f11c](LDJ-662a0a1f_98f11c.json)
- 2024-06-05 - [LDJ-665e9f8f_9a384c](LDJ-665e9f8f_9a384c.json)

### [LDJ-010] `bm2dx.dll`
- 2023-12-06 - [LDJ-656d3226_a145e0](LDJ-656d3226_a145e0.json)
- 2024-03-25 - [LDJ-65fbdb9b_a29c4c](LDJ-65fbdb9b_a29c4c.json)
- 2024-05-07 - [LDJ-662a05c7_a5bf9c](LDJ-662a05c7_a5bf9c.json)

</details>
</details>

<details><summary><b>Sound Voltex</b></summary>

<details><summary><b>SOUND VOLTEX II -infinite infection-</b></summary>

### [KFC] `soundvoltex.dll`
- 2014-10-22 (PhaseII) - [KFC-543e7ccd_10e693](KFC-543e7ccd_10e693.json)

</details>
<details><summary><b>SOUND VOLTEX III GRAVITY WARS</b></summary>

### [KFC] `soundvoltex.dll`
- 2015-11-16 (Season 1) - [KFC-56497884_20131c](KFC-56497884_20131c.json)
- 2016-12-12 (Season 2) - [KFC-58365cd4_21e91c](KFC-58365cd4_21e91c.json)

</details>
<details><summary><b>SOUND VOLTEX IV HEAVENLY HAVEN</b></summary>

### [KFC] `soundvoltex.dll`
- 2018-01-16 - [KFC-5a55ed92_26d3cb](KFC-5a55ed92_26d3cb.json)
- 2019-02-06 - [KFC-5c541c96_27bc7b](KFC-5c541c96_27bc7b.json)

</details>
<details><summary><b>SOUND VOLTEX VIVID WAVE</b></summary>

### [KFC] `soundvoltex.dll`
- 2019-10-31 (CN ver.) - [KFC-5dbaae15_36ea80](KFC-5dbaae15_36ea80.json)
- 2020-01-15 - [KFC-5e18527b_31c780](KFC-5e18527b_31c780.json)
- 2020-12-22 - [KFC-5fdadbea_330980](KFC-5fdadbea_330980.json)

</details>
<details><summary><b>SOUND VOLTEX EXCEED GEAR</b></summary>

### [KFC] `soundvoltex.dll`
- 2021-12-14 - [KFC-61b19602_57ac68](KFC-61b19602_57ac68.json)
- 2024-01-16 - [KFC-659f91b3_696318](KFC-659f91b3_696318.json)
- 2024-01-30 - [KFC-65b1fc65_69c278](KFC-65b1fc65_69c278.json)
- 2024-02-06 - [KFC-65bb66cb_69cfb8](KFC-65bb66cb_69cfb8.json)
- 2024-02-20 - [KFC-65cda95b_6a5748](KFC-65cda95b_6a5748.json)
- 2024-03-18 - [KFC-65f174e7_6ae218](KFC-65f174e7_6ae218.json)
- 2024-04-02 - [KFC-66039c56_6be478](KFC-66039c56_6be478.json)
- 2024-04-30 - [KFC-6629f133_6bcea8](KFC-6629f133_6bcea8.json)
- 2024-05-21 - [KFC-6643ed55_663968](KFC-6643ed55_663968.json)
- 2024-06-04 - [KFC-6656ee0c_664a78](KFC-6656ee0c_664a78.json)
- 2024-06-25 - [KFC-667290d9_665948](KFC-667290d9_665948.json) (**INCOMPLETE**)

</details>
</details>
</details>