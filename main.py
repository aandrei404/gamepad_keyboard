#/usr/bin python3

if __name__ == "__main__":

    # imports
    from XInput import *
    from pyautogui import press, keyDown, keyUp
    import tkinter as tk
    
    # save most used keys
    char_bank = [['a', 'b', 'c', 'd'],                      # L 0 0   -- 1
                ['e', 'f', 'g', 'h'],                      # L 0 1   -- 2
                ['i', 'j', 'k', 'l'],                      # L 1 1   -- 3
                ['m', 'n', 'o', 'p'],                      # L 1 0   -- 4
                ['q', 'r', 's', 't'],                      # L 1 -1  -- 5
                ['u', 'v', 'w', 'x'],                      # L 0 -1  -- 6
                ['y', 'z', '1', '2'],                      # L -1 -1 -- 7
                ['3', '4', '5', '6'],                      # L -1 0  -- 8
                ['7', '8', '9', '0'],                      # L -1 1  -- 9
                ['enter', 'backspace', 'space', 'tab'],    # R 0 1   -- 10
                [',', '.', '/', '\\'],                     # R 1 1   -- 11
                [';', "'", '[', ']',],                     # R 1 0   -- 12
                ['-', '=', '`', 'delete']]                 # R 1 -1  -- 13
    bank_no = 0
    # alt key unpressed/pressed
    alt_status = 0

    # windows gui
    root = tk.Tk()
    root.title("Gamepad_Keyboard")
    canvas = tk.Canvas(root, width= 200, height = 150, bg="white")
    text_key_info = canvas.create_text((100,50), text = "Keys_Info")
    text_status_info = canvas.create_text((100,100), text = "Status_Info")
    canvas.pack()
  
    set_deadzone(DEADZONE_TRIGGER,250)
    
    class MyHandler(EventHandler):
        def process_button_event(self,event):
            global bank_no
            global alt_status
            
            if event.type == EVENT_BUTTON_PRESSED:
                if event.button == "A":
                    keyDown(char_bank[bank_no][0])
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no][0])
                elif event.button == "B":
                    keyDown(char_bank[bank_no][1])
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no][1])
                elif event.button == "X":
                    keyDown(char_bank[bank_no][2])
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no][2])
                elif event.button == "Y":
                    keyDown(char_bank[bank_no][3])
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no][3])
                elif event.button == "DPAD_LEFT":
                    keyDown('left')
                    canvas.itemconfig(text_key_info, text = "arrow_left")
                elif event.button == "DPAD_RIGHT":
                    keyDown('right')
                    canvas.itemconfig(text_key_info, text = "arrow_right")
                elif event.button == "DPAD_UP":
                    keyDown('up')
                    canvas.itemconfig(text_key_info, text = "arrow_up")
                elif event.button == "DPAD_DOWN":
                    keyDown('down')
                    canvas.itemconfig(text_key_info, text = "arrow_down")
                elif event.button == "RIGHT_SHOULDER":
                    if alt_status == 0:
                        keyDown('alt')
                        canvas.itemconfig(text_key_info, text = "alt pressed")
                    else:
                        keyUp('alt')
                        canvas.itemconfig(text_key_info, text = "alt released")
                elif event.button == "LEFT_SHOULDER":
                    press('esc')
                    canvas.itemconfig(text_key_info, text = "esc")
                else:
                    canvas.itemconfig(text_status_info, text = "Unmapped button!")
        
        def process_stick_event(self, event):
            global bank_no
            # based on stick position, select character bank
            if event.stick == LEFT:
                l_thumb_stick_pos = (int(round(event.x)), int(round(event.y)))
                if l_thumb_stick_pos == (0, 0):
                    bank_no = 0
                elif l_thumb_stick_pos == (0, 1):
                    bank_no = 1
                elif l_thumb_stick_pos == (1, 1):
                    bank_no = 2
                elif l_thumb_stick_pos == (1, 0):
                    bank_no = 3
                elif l_thumb_stick_pos == (1, -1):
                    bank_no = 4
                elif l_thumb_stick_pos == (0, -1):
                    bank_no = 5
                elif l_thumb_stick_pos == (-1, -1):
                    bank_no = 6
                elif l_thumb_stick_pos == (-1, 0):
                    bank_no = 7
                elif l_thumb_stick_pos == (-1, 1):
                    bank_no = 8
                else:
                    bank_no = -1
                if bank_no == -1:
                    canvas.itemconfig(text_status_info, text = "Unmapped section!")
                else:
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no])
            elif event.stick == RIGHT:
                r_thumb_stick_pos = (int(round(event.x)), int(round(event.y)))
                if r_thumb_stick_pos == (0, 1):
                    bank_no = 9
                elif r_thumb_stick_pos == (1, 0):
                    bank_no = 10
                elif r_thumb_stick_pos == (0, -1):
                    bank_no = 11
                elif r_thumb_stick_pos == (-1, 0):
                    bank_no = 12
                elif r_thumb_stick_pos == (0, 0):
                    pass
                else:
                    bank_no = -1
                if bank_no == -1:
                    canvas.itemconfig(text_status_info, text = "Unmapped section!")
                else:
                    canvas.itemconfig(text_key_info, text = char_bank[bank_no])

        def process_trigger_event(self, event):
            if event.trigger == LEFT:
                if int(round(event.value)):
                    keyDown('shift')
                else:
                    keyUp('shift')
            elif event.trigger == RIGHT:
                if int(round(event.value)):
                    keyDown('ctrlright')
                else:
                    keyUp('ctrlright')

        def process_connection_event(self, event):
            pass
            
    handler = MyHandler(0)
    thread = GamepadThread(handler)

    root.mainloop()
    thread.stop()

else:
    raise ImportError("This is not a module!")
