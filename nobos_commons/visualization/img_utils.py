from typing import List

import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw


def add_img_title(img, title, font_size: int = 18):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=font_size)
    # get text size
    text_size = font.getsize(title)

    # set button size + 10px margins
    bg_size = (text_size[0] + 20, text_size[1] + 40)
    draw.rectangle(((0, 30), bg_size), fill="black")
    draw.text((10, 30), title, fill=(255, 255, 255), font=font)

    # cv2.putText(img, title, (0, 30), font, font_scale, (0, 0, 255), 1, cv2.LINE_AA)
    img = np.asarray(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def rgb_to_bgr_color(rgb_color: List[int]):
    return [rgb_color[2], rgb_color[1], rgb_color[0]]