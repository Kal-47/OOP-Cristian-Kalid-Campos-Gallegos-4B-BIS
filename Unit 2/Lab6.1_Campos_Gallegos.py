
import tkinter as tk
from tkinter import ttk
import os
from abc import ABC, abstractmethod #

class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name 
    
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class SmartConsole(SmartDevice):
    def __init__(self):
        super().__init__("Playstation 3")

    def turn_on(self):
        return f"{self.name}, Is playing music."

    def turn_off(self):
        return f"{self.name}, Stopped playing music."


class SmartProjector(SmartDevice):
    def __init__(self):
        super().__init__("VistaVision 2.0")

    def turn_on(self):
        return f'{self.name}, Is playing a movie'

    def turn_off(self):
        return f"{self.name}, Stopped playing a movie"


class SmartServer(SmartDevice):
    def __init__(self):
        super().__init__("DSM Server")

    def turn_on(self):
        return f'{self.name}, Is streaming a movie'

    def turn_off(self):
        return f"{self.name}, Stopped streaming a movie"

    
class SmartLap(SmartDevice):
    def __init__(self):
        super().__init__("Thinkpad Laptop")

    def turn_on(self):
        return f'{self.name}, Is playing a video'

    def turn_off(self):
        return f"{self.name}, Stopped playing a video"



class HomeLabApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("Lab 6: Polymorphism with GUI by - Cristian Kalid Campos Gallegos")
        self.geometry("1000x1000")
        self.resizable(False, False)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_dir = os.path.join(current_dir, "app_icon.png")


        if os.path.exists(icon_dir):
            self.app_icon = tk.PhotoImage(file=icon_dir)
            self.iconphoto = (True,self.app_icon)
        else:
            print("The icon doesnt exists.")


        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Console": SmartConsole(),
            "Projector": SmartProjector(),
            "Server": SmartServer(),
            "Laptop": SmartLap(),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        lbl_header = tk.Label(
            self,
            text="Home Lab Center",
            font=("Helvetica", 20, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        group_box = tk.LabelFrame(
            self,
            text=" Select an option ",
            font=("Helvetica", 15, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = list(self.items.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # Trigger Action Button
        btn_action = tk.Button(
            self,
            text="Turn On Device",
            command=self._handle_action_on,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=16,
            pady=6
        )
        btn_action.pack(pady=15)


        btn_inaction = tk.Button(
            self,
            text="Turn Off Device",
            command=self._handle_action_off,
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=16,
            pady=6
        )
        btn_inaction.pack(pady=15)

        log_frame = tk.LabelFrame(self, text=" Activity Log ", font=("Arial", 11, "bold"))
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.log_list = tk.Listbox(log_frame, height=5, font=("Consolas", 10))
        self.log_list.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(log_frame, command=self.log_list.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_list.config(yscrollcommand=scrollbar.set)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an sostion above and click 'EXECUTE ACTION'.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

    def _handle_action_on(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_on()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self.log_list.insert(tk.END, result_message)
        self.log_list.see(tk.END) 

    def _handle_action_off(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_off()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        self.log_list.insert(tk.END, result_message)
        self.log_list.see(tk.END) 


# LAUNCHER
if __name__ == "__main__":
    app = HomeLabApp()
    app.mainloop()