# Gamepad keyboard

Small stupid project I made in one night because I wanted to type using a Xbox360 controller instead of my keyboard + mouse. It was good for a couple of laughs with my roommate but I doubt someone will ever use this professionally... I used [XInput](https://github.com/Zuzu-Typ/XInput-Python) to interact with the Gamepad and [PyAutoGUI](https://github.com/asweigart/pyautogui/tree/master) for keyboard-related tasks.

## How this works

- Left Trigger is mapped to Left Shift, Right Trigger to Left Ctrl.
- Left Bumper is mapped to ESC, Right Bumper to ALT.
- DPAD is used for the arrow keys.
- A, B, X, Y -> mapped to keys from the character bank:

<!-- I ain't making this prettier-->
| Bank_No  | A     | B  | X | Y |
| -------  | -     | - | - | - |
|    1     | a     | b | c | d |
|    2     | e     | f | g | h |
|    3     | i     | j | k | l |
|    4     | m     | n | o | p |
|    5     | q     | r | s | t |
|    6     | u     | v | w | x |
|    7     | y     | z         | 1 | 2 |
|    8     | 3     | 4         | 5 | 6 |
|    9     | 7     | 8         | 9 | 0 |
|    10    | enter | backspace | space | tab |
|    11    | ,     | . | / | \ |
|    12    | ;     | ' | [ | ] |
|    13    | -     | = | ` | delete |

- To select a character bank, for the ones from 1 to 9, move the Left Joystick in a clockwise motion and each of the 9 positions will select a bank. The Joystick needs to be held in that position or else it will default to the (0, 0) bank. For the banks 10-13, the Right Joystick is used, and it does not need to be held in place (for easier use).
- Other characters can be used with Shift + the specific key from the bank.

The mini window GUI shows information about the current bank and what key is pressed.
