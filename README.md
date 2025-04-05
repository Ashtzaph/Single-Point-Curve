# Single Point Curve Add-on for Blender

This add-on creates a minimal curve object with a single control point and collapsed handles.

## Features

- Creates a single control point at the 3D cursor location
- Handles are collapsed into the control point (zero length)
- Provides a clean starting point for building custom curves
- Fully integrated with Blender's undo system

## Installation

1. Download the latest release
2. In Blender, go to `Edit > Preferences > Add-ons`
3. Click "Install" and select the downloaded ZIP file
4. Enable the add-on

## Usage

1. Position your 3D cursor where you want the point
2. Press `Shift+A > Curve > Single Point`
3. In Edit Mode (Tab), you can:
   - Add new points with `Ctrl+Click`
   - Extrude handles by selecting and pressing `E`
   - Create actual curves from this starting point

## Development

To contribute or modify:

```bash
git clone https://github.com/yourusername/single_point_curve.git
cd single_point_curve
```

## License

[MIT License](LICENSE)

MIT License

Copyright (c) 2025 Amir Diab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
