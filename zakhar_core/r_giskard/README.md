# r_giskard

## Principles

### Robot has a Mind. Mind is consist of 4 program parts: Conscious, Responses, Subconscious, Unconscious

Three of the parts should work in parallel:

- **Conscious** or **Responses** - can't be paralleled with each other
- **Subconscious**
- **Unconscious**

### Purposes of the parts

- **Conscious** - thread with basic program (e.g., discovery of the territory)
- **Responses** - thread with program, started by some condition and interrupting Conscious (e.g. if the robot is falling)
- **Subconscious** - thread with program, responsible to translate commands from Conscious and Responces to the hardware (move forward -> commands to motors; smile -> command to the screen, etc.)
- **Unconscious** - system programs result of those can be observed, but the programs itself can't be impacted from anything programmatically in the explicit manner (good example for humans - heartbeat, for the robot - polling of the sensors, like camera or accelerometer, the triggers calculation)

### Threading

- **Conscious** should have only one thread
- **Responses** should have only one thread
- **Subconscious** should have only one thread
- **Unconscious** as many threads as needed.

### Other Mind entities

- **Trigger** - a bool parameter responsible for switching between Conscious and Responses.

## Other

This package is a part of the `r_giskard` project (see: [an-dr/r_giskard: Small project for experiments with unconditioned and conditioned reflexes](https://github.com/an-dr/r_giskard))