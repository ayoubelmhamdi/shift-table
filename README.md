# Table-Shift

**Table-Shift** is a Python-based simulation tool for radiotherapy treatment planning. It generates random CT scan isocenter (ISO) positions and random displacements with directions, allowing users to practice calculating new treatment ISO positions. This tool is ideal for learning and exercises in radiotherapy planning, particularly for understanding how to adjust ISO positions based on given displacements.

## Features
- Generates random initial CT ISO positions within specified ranges.
- Applies random displacements with directions (Left/Right, Superior/Inferior, Anterior/Posterior).
- Displays the initial CT ISO positions and displacements for user calculation.
- Reveals the correct treatment ISO positions after a short pause for self-assessment.

## Usage
1. Clone the repository or download the script.
2. Run the script using Python 3:
   ```bash
   python table_shift.py
   ```
3. Follow the on-screen instructions to practice calculating treatment ISO positions.

## Example Output
```
Initial CT ISO Position:
x: 5.3
y: 45.7
z: -15.2

Displacements to Apply:
3.5 Left
2.1 Superior
4.8 Posterior

Treatment ISO Position:
x: 1.8
y: 47.8
z: -20.0
```

## Requirements
- Python 3.x
- No additional libraries required.

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
