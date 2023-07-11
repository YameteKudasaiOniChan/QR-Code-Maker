import customtkinter
from PIL import Image
import config
import qrcode
from datetime import datetime

def create_qrcode():
    data = text_input.get()
    global image_label
    image_label.destroy()
    img = qrcode.make(data)
    current_time = datetime.now()
    name = current_time.strftime('%Y_%m%d%H%M%S%f')
    img.save(name+".png")
    image = customtkinter.CTkImage(Image.open(name+".png"), size=(200, 200))
    image_label = customtkinter.CTkLabel(app, image=image, text="", corner_radius=10, width=200, height=200)
    image_label.pack(pady=80)

app = customtkinter.CTk(config.app_color)
app.title("QRCODE MAKER")
app.minsize(config.app_size[0], config.app_size[1])
app.maxsize(config.app_size[0], config.app_size[1])
app.iconbitmap("icon.ico")


text_input = customtkinter.CTkEntry(
    master=app,
    width=300,
    height=32,
    corner_radius=10,
    border_width=1,
    fg_color=config.app_color,
    text_color=config.Color,
    placeholder_text_color=config.Color,
    border_color=config.Color,
    font=(config.input_font, 18),
    placeholder_text="Text, Url or ...")
create_btn = customtkinter.CTkButton(
    master=app,
    width=150,
    height=32,
    corner_radius=10,
    fg_color=config.Color,
    hover_color=None,
    text_color=config.TextColor,
    font=(config.input_font, 18),
    anchor="center",
    text="CREATE",
    command=create_qrcode)
image_label = customtkinter.CTkLabel(app, image=None, text="",fg_color=config.qr_back, width=200, height=200)

text_input.pack(pady=50)
create_btn.pack()
image_label.pack(pady=80)


app.mainloop()