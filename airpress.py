import tkinter as tk
import math

class AirPressureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Air Pressure Meter")
        self.master.geometry("400x400")

        # Initial air pressure level
        self.airpress_level = 50  

        # Label for Air Pressure
        self.airpress_label = tk.Label(master, text="Air Pressure", font=("Verdana", 16))
        self.airpress_label.pack(pady=10)

        # Canvas for the air pressure display
        self.canvas = tk.Canvas(master, width=300, height=300, bg="DeepSkyBlue")
        self.canvas.pack()

        # Entry widget for changing air pressure level
        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        # Button to update the air pressure level
        self.update_btn = tk.Button(master, text="UPDATE", command=self.update_airpress_level)
        self.update_btn.pack()

        # Display initial air pressure level
        self.update_airpress_meter()

    def update_airpress_meter(self):

        # Clear previous air pressure level
        self.canvas.delete("airpress_meter")

        # Ensure air pressure level doesn't exceed 100%
        airpress_level = min(self.airpress_level, 100)

        # Air pressure meter parameters
        gauge_center = (150, 150)
        gauge_radius = 120

        # Calculate start and extend angles based on the air pressure level
        start_angle = 180 if airpress_level == 0 else 180 - (airpress_level * 1.8)
        extent_angle = 180 - start_angle

        # Draw air pressure meter outline
        self.canvas.create_arc(gauge_center[0]-gauge_radius, gauge_center[1]-gauge_radius,
                               gauge_center[0]+gauge_radius, gauge_center[1]+gauge_radius,
                               start=0, extent=180, outline="black", width=2, tags="gast_")
        self.canvas.create_line(gauge_center[0]-gauge_radius, gauge_center[1],
                               gauge_center[0]+gauge_radius, gauge_center[1],
                               fill="black", width=2, tags="airpress_meter")
        
        #Draw air pressure level lines
        for angle in range (10, 171, 10):
            x1 = gauge_center[0] + gauge_radius * math.cos(math.radians(angle))
            y1 = gauge_center[1] + gauge_radius * math.sin(math.radians(angle))
            x2 = gauge_center[0] + (gauge_radius - 10) * math.cos(math.radians(angle))
            y2 = gauge_center[1] + (gauge_radius - 10) * math.sin(math.radians(angle))
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=2, tags="airpress_meter")

        # Draw air pressure level indicator
            self.canvas.create_arc(gauge_center[0]-gauge_radius, gauge_center[1]-gauge_radius,
                                   gauge_center[0]+gauge_radius, gauge_center[1]+gauge_radius,
                                   start=start_angle, extent=extent_angle, outline="orange", width=10, tags="airpress_meter" )
            
    def show_message(self, message):
        popup = tk.Toplevel(self.master)
        popup.title("Message")
        popup.geometry("200x100")
        label = tk.Label(popup, text=message)
        label.pack(pady=10)

        ok_btn = tk.Button(popup, text="OK", command=popup.destroy)
        ok_btn.pack()

    def update_airpress_level(self):

        #Error checking for input
        try:
            new_airpress_level = float(self.entry.get())
            if new_airpress_level < 0:
                raise ValueError("Air pressure level cannot be negative")
            elif new_airpress_level > 100:
                self.show_message("Too much air pressure")
                new_airpress_level = 100
        except ValueError as e:
            self.show_message(str(e))
            return
        
        self.airpress_level = new_airpress_level
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.airpress_level))
        self.update_airpress_meter()


def main():
    root = tk.Tk()
    app = AirPressureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


    