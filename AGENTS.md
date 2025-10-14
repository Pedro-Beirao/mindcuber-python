
## Project Overview

This is a Python 3.9 program that solves Rubik's cubes using an EV3 Mindstorms robot without requiring an SD card. The system uses computer vision to scan the cube state and the Kociemba algorithm to generate solutions.

## Architecture

### Core Components

1. **mindcuber-python.py** - Main solver script that:
   - Connects to EV3 via USB/Bluetooth/WiFi
   - Controls two motors (arm on port A, platform on port B)  
   - Executes Kociemba solution sequences
   - Handles cube manipulation logic (hold/release/rotate/turn)

2. **rubik.py** - Entry point script that:
   - Launches cube scanning via webcam using rubiks-cube-tracker
   - Provides command-line interface for webcam selection and help
   - Manages the overall solving workflow

3. **rubikscubetracker/__init__.py** - Computer vision module that:
   - Uses OpenCV to detect cube squares from camera images
   - Processes 6 cube faces (U, L, F, R, B, D) 
   - Performs color recognition and validation
   - Generates Kociemba string for solver input

### Key Dependencies

- **ev3-dc**: EV3 motor control library
- **kociemba**: Rubik's cube solving algorithm  
- **opencv-python**: Computer vision for cube scanning
- **rubiks-cube-tracker**: Cube detection and color analysis
- **rubiks-color-resolver**: Color mapping and validation

## Development Commands

### Installation & Setup
```bash
# Install OpenCV first (if not already installed)
pip install opencv-python

# Install the package and all dependencies
pip install git+https://github.com/PBeGood4/mindcuber-python

# Alternative: Install from local source
sudo python3 setup.py install
```

### Build & Clean
```bash
# Build and install package
make all

# Clean build artifacts  
make clean
```

### Running the System
```bash
# Default: Use webcam 0
rubik.py

# Specify different webcam
rubik.py -w 1

# Show help and options
rubik.py -h

# Show installation paths
rubik.py -local
```

### Configuration
The main configuration is in `mindcuber-python.py` line 29:
```python
ev3device = ev3.EV3(protocol=ev3.USB, host='00:16:53:3D:F8:DF')
```

Required changes:
- Set protocol: `ev3.USB`, `ev3.BLUETOOTH`, or `ev3.WIFI` (USB recommended)
- Set host: EV3's MAC address (found in Brick Info / ID)

## Hardware Setup

### Motor Connections
- **Port A**: Arm motor (controls cube rotation)
- **Port B**: Platform motor (controls cube face turns)

### Robot Construction
Use the `MindCub3r-v1p0.pdf` building instructions provided in the repository.

## Testing Approach

The system uses manual testing with physical hardware:
1. Build and position the MindCub3r robot
2. Connect EV3 to computer via preferred protocol
3. Place scrambled cube on platform
4. Run scanning and solving process
5. Verify solution accuracy and timing

## Important Implementation Details

### Motor Control Functions
- `hold()`: Secures upper cube layers
- `release()`: Releases cube grip
- `rot(dir, release)`: Rotates cube using arm motor
- `turn(dir, times)`: Turns platform for face rotations

### Cube State Management
- Tracks current face orientation (`faceDown` variable)
- Handles all 6 face rotations (U, D, L, R, F, B)
- Supports clockwise, counter-clockwise, and double turns
- Uses Kociemba algorithm for optimal solution generation

### Error Handling
- Motor synchronization via `wait()` and `waitT()` functions
- Cube detection validation with contour analysis
- Color recognition verification across 6 faces
- Solution execution with timing and progress tracking
