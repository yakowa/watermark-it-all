![JacobEM](https://jacobem.com/assets/media/JacobEM.png)


# Watermark-it-all

Watermark-it-all is a quick app which allows you to add a watermark to as many images as you want! This is helpful if you want to protect your work against people using images without your permission.

[![GitHub](https://img.shields.io/badge/Github-%28Click%20Me%29-blueviolet)](https://github.com/yakowa/watermark-it-all)

---

![Version: 1.0](https://img.shields.io/badge/Version-1.0-00e0a7)

![License: MIT](https://img.shields.io/badge/License-MIT-776bff)
## Documentation

### Setup

* Place your watermark image in the same folder as the `app.py` main script.
* Put every image you want to add a watermark to in the `img` folder. (There is no limit!)

**Note:** You must have [Python](https://www.python.org/) installed.

### How to run

Simply run the `run.bat` script, this will open your terminal execuing the script using Python.

Alternatively, you can simply run
```bash
py app.py {See-Param-One} {See-Param-Two}
```

### Parameters

**Param One**

Location of watermark on the base image.
| Parameter | Description                |
| :-------- | :------------------------- |
| `tl` | Places the image in the top left of the base image. |
| `tr` | Places the image in the top right of the base image. |
| `bl` | Places the image in the bottom left of the base image. |
| `br` | Places the image in the bottom right of the base image. |
| `c` | Places the image in the center of the base image. |


**Param Two**

An option for showing a preview of each image after the watermark is added.
| Parameter | Description                |
| :-------- | :------------------------- |
| `show` | Will show a preview of each image after a watermark is added. **Note:** This makes the application take a lot longer. |
| `no-show` | Will not show a preview of each image after the watermark is added. |


### Example
This would run the application with the watermark being in the center and not displaying a preview of each image.
```bash
py app.py c no-show
```