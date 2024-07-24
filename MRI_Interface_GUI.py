import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create and display the GUI based on the XML structure
def create_gui():
    root = tk.Tk()
    root.title("MRI Parameter Editor")

    notebook = ttk.Notebook(root)

    # Function to create a parameter card with columns and parameters
    def create_parameter_card(notebook, display_name, parameters):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text=display_name)
        left_column = ttk.Frame(frame)
        left_column.pack(side="left", fill="both", expand=True)
        right_column = ttk.Frame(frame)
        right_column.pack(side="left", fill="both", expand=True)

        for param in parameters.get("left", []):
            if param:
                param_frame = ttk.Frame(left_column)
                param_frame.pack(fill="x", padx=40, pady=10)
                ttk.Label(param_frame, text=param).pack(side="left")
                if param.startswith("YesNo"):
                    tk.Radiobutton(param_frame, text="Yes").pack(side="left")
                    tk.Radiobutton(param_frame, text="No").pack(side="left")
                else:
                    ttk.Entry(param_frame).pack(side="right")

        for param in parameters.get("right", []):
            if param:
                param_frame = ttk.Frame(right_column)
                param_frame.pack(fill="x", padx=40, pady=10)
                ttk.Label(param_frame, text=param).pack(side="left")
                if param.startswith("YesNo"):
                    tk.Radiobutton(param_frame, text="Yes").pack(side="left")
                    tk.Radiobutton(param_frame, text="No").pack(side="left")
                else:
                    ttk.Entry(param_frame).pack(side="right")

    # Routine Card
    routine_params = {
        "left": ["Echo Time", "Repetition Time", "Averages", "Repetitions", "Total Scan Time", "", "YesNoMinEchoTime", "AcqMode", "NPro", "ProUndersampling", "PVM_EffSWh", "Flip Angle"],
        "right": ["Slices", "Slice Orientation", "PVM_SliceThick", "PVM_Matrix", "PVM_Fov"]
    }

    routine_frame = ttk.Frame(notebook)
    notebook.add(routine_frame, text="Routine")

    routine_notebook = ttk.Notebook(routine_frame)
    routine_notebook.pack(fill="both", expand=True)

    create_parameter_card(routine_notebook, "Routine Parameters", routine_params)

    # fMRI Card as a subcard of Routine Card
    fMRI_params = {
        "left": ["No Of Prestimulus Baseline", "No of Stimulations", "No of Baseline Stimulations", "No of Epochs", "Total Repetitions"]
    }

    fMRI_frame = ttk.Frame(routine_notebook)
    routine_notebook.add(fMRI_frame, text="fMRI Parameters")

    # Adding fMRI parameters
    for param in fMRI_params["left"]:
        if param:
            param_frame = ttk.Frame(fMRI_frame)
            param_frame.pack(fill="x", padx=40, pady=10)
            ttk.Label(param_frame, text=param).pack(side="left")
            ttk.Entry(param_frame).pack(side="right")

    # Toggle button in the fMRI subroutine card
    toggle_button_var = tk.BooleanVar()

    def toggle_button():
        if toggle_button_var.get():
            toggle_button.config(text="fMRI On")
        else:
            toggle_button.config(text="fMRI Off")

    toggle_button = tk.Checkbutton(fMRI_frame, text="Off", variable=toggle_button_var, command=toggle_button)
    toggle_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Contrast Card
    contrast_main_params = {
        "left": ["Minimum Echo Time", "PVM_EchoTime", "PVM_EffSWh", "PVM_RepetitionTime", "Flip Angle", "PVM_DummyScans", "PVM_DummyScansDur", "PVM_NMovieFrames", "PVM_MotionSupOnOff"],
        "right": ["PVM_FatSupOnOff", "PVM_FovSatOnOff", "PVM_MagTransOnOff", "PVM_TriggerModule", "PVM_TriggerOutOnOff"]
    }
    create_parameter_card(notebook, "Contrast - Main", contrast_main_params)

    # Geometry Card
    geometry_main_params = {
        "left": ["PVM_SliceThick", "PVM_ObjOrderScheme", "PVM_MajSliceOri", "", "", "PVM_Fov", "PVM_AntiAlias"],
        "right": ["PVM_SPackArrNSlices", "PVM_SPackArrSliceOrient", "PVM_SPackArrReadOrient", "PVM_SPackArrSliceOffset", "PVM_SPackArrSliceGapMode", "PVM_SPackArrSliceGap", "PVM_SPackArrSliceDistance"]
    }
    create_parameter_card(notebook, "Geometry - Main", geometry_main_params)

    # Sequence Card
    sequence_main_params = {
        "left": ["", "PVM_EffSWh", "PVM_AcquisitionTime", "ExcPulse1Enum", "ReadSpoiling", "Auto Slice Spoiler"],
        "right": ["Method", "RampCompYN", "GradSync"]
    }
    create_parameter_card(notebook, "Sequence - Main", sequence_main_params)

    # Setup Card
    setup_main_params = {
        "left": ["PVM_RefPowMod1", "PVM_RefPowCh1", "PVM_RefPowStat1", "Receiver Gain", "Calc. Pulse Ampl.", "Exc. Pulse Attenuation"],
        "right": ["", "", "", "", "", "Exc. Pulse Power", "Exc. Pulse Amplitude"]
    }
    create_parameter_card(notebook, "Setup - Main", setup_main_params)

    notebook.pack(fill="both", expand=True)
    root.mainloop()

create_gui()
