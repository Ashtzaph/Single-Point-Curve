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


