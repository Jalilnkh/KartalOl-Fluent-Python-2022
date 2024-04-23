import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Canvas, Scrollbar
import pandas as pd
from tkinter import messagebox

bpath = '/home/omniaz/Desktop/omniaz/code/pipeline/dvc/data/analysis/recognition_dataset_V2024419/generated_datasets/training_dataset_202444/enrollments/POL0BARS00019164/'
image_paths = [bpath+"1456_zabka_standard_11_listopada_71_12032024_daniel_dairy_2_app_data_i17_POL0BARS00019164_16_229.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_14_290.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_17_297.png",
        bpath+"1456_zabka_standard_11_listopada_71_12032024_daniel_dairy_2_app_data_i17_POL0BARS00019164_16_229.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_14_290.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_17_297.png",
        bpath+"1456_zabka_standard_11_listopada_71_12032024_daniel_dairy_2_app_data_i17_POL0BARS00019164_16_229.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_14_290.png",
        bpath+"1460_zabka_standard_jana_III_sobieskiego_55a_08032024_karolina_dairy_2_app_data_i17_POL0BARS00019164_17_297.png"]

# Load the CSV file
csv_pth = "/home/omniaz/Downloads/zabka_standard_11_listopada_71_12032024_daniel_dairy_2_app_data_i17/zabka_standard_11_listopada_71_12032024_daniel_dairy_2_app_data_i17_sku.csv"

def update_csv(classid, trackid, df):
    # Set the 'id' of the clicked image to -1 in the dataframe
    df.loc[(df['classid'] == classid) & (df['trackid'] == trackid), 'classid'] = -1
    df.to_csv(csv_pth, index=False)

def on_image_click(event, classid, trackid,  df):
    # Confirmation before making a change
    result = messagebox.askquestion("Update Record", f"Set ID {classid} to -1?")
    if result == 'yes':
        update_csv(classid, trackid, df)

def visualization(enroll_img_paths, vid_img_paths, sku_id, trackid, csv_pth):
    df = pd.read_csv(csv_pth)
    app = tk.Tk()
    app.title('Dual Side Image Display Example with Scrollbars')

    # Create frames for the left and right image groups, inside canvas for scrolling
    left_canvas = Canvas(app)
    left_scrollbar = Scrollbar(app, orient="vertical", command=left_canvas.yview)
    left_scrollable_frame = tk.Frame(left_canvas)

    left_scrollable_frame.bind(
        "<Configure>",
        lambda e: left_canvas.configure(
            scrollregion=left_canvas.bbox("all")
        )
    )

    left_canvas.create_window((0, 0), window=left_scrollable_frame, anchor="nw")
    left_canvas.configure(yscrollcommand=left_scrollbar.set)

    right_canvas = Canvas(app)
    right_scrollbar = Scrollbar(app, orient="vertical", command=right_canvas.yview)
    right_scrollable_frame = tk.Frame(right_canvas)

    right_scrollable_frame.bind(
        "<Configure>",
        lambda e: right_canvas.configure(
            scrollregion=right_canvas.bbox("all")
        )
    )

    right_canvas.create_window((0, 0), window=right_scrollable_frame, anchor="nw")
    right_canvas.configure(yscrollcommand=right_scrollbar.set)

    left_canvas.pack(side="left", fill="both", expand=True)
    left_scrollbar.pack(side="left", fill="y")
    right_canvas.pack(side="right", fill="both", expand=True)
    right_scrollbar.pack(side="right", fill="y")
    # Lists to hold photo images to avoid garbage collection issues
    left_images = []
    right_images = []

    # Load and display images for the left frame
    for path in enroll_img_paths:
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        left_images.append(photo)
        label = tk.Label(left_scrollable_frame, image=photo)
        label.pack(padx=5, pady=5, side='top')
    id_value = sku_id
    # Load and display images for the right frame
    for path in vid_img_paths:
        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        right_images.append(photo)
        label = tk.Label(right_scrollable_frame, image=photo)
        label.pack(padx=5, pady=5, side='top')
        label.bind("<Double-Button-1>", lambda e, id_val=id_value: on_image_click(e, id_val, trackid, df))
    app.mainloop()

if __name__ == "__main__":
    enroll_img_paths = image_paths[:3]
    vid_img_paths = image_paths
    sku_id = 'POL0YOGH00019809'
    trackid = 120
    visualization(enroll_img_paths, vid_img_paths, sku_id, trackid, csv_pth)
