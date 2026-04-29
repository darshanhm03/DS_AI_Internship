import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def select_and_detect():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()
    
    # Open file dialog to select images
    print("Select image(s) for detection...")
    file_paths = filedialog.askopenfilenames(
        title="Select Image(s) for YOLOv7 Detection",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
            ("All files", "*.*")
        ]
    )
    
    if not file_paths:
        print("No files selected. Exiting...")
        return
    
    print(f"\nSelected {len(file_paths)} image(s):")
    for i, path in enumerate(file_paths, 1):
        print(f"  {i}. {path}")
    
    # Run detection on each selected image
    print("\n" + "="*50)
    print("Starting YOLOv7 Detection...")
    print("="*50 + "\n")
    
    for file_path in file_paths:
        print(f"\nProcessing: {os.path.basename(file_path)}")
        print("-" * 50)
        
        # Build command
        cmd = [
            'python', 'detect.py',
            '--weights', 'yolov7.pt',
            '--conf', '0.25',
            '--img-size', '640',
            '--source', file_path,
            '--view-img'
        ]
        
        # Run detection
        subprocess.run(cmd)
        
        print("\n" + "="*50)
    
    print("\n✅ All detections completed!")
    print(f"Results saved in: runs/detect/")
    
    # Ask if user wants to select more images
    choice = input("\nWould you like to select more images? (y/n): ").strip().lower()
    if choice == 'y':
        select_and_detect()
    else:
        print("Goodbye! 👋")

if __name__ == "__main__":
    print("="*50)
    print("🎯 YOLOv7 Image Detection Tool")
    print("="*50)
    select_and_detect()
