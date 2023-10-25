import os
import platform

import glob


def get_font_list():
    """
    Find truetype tonts list from system.
    """

    os_system = platform.system()

    if os_system == 'Windows':
        font_path = os.path.abspath("C:/Windows/Fonts")
        font_list = glob(
            os.path.abspath(os.path.join(font_path, '*.ttf'))
        )

    elif os_system == 'Linux':
        font_path = os.path.abspath("/usr/share/fonts/truetype")
        font_list = glob(
            os.path.abspath(os.path.join(font_path, '*', '*.ttf'))
        )

    return font_list



def get_default_kor_font():
    os_system = platform.system()

    if os_system == 'Windows':
        return os.path.abspath("C:/Windows/Fonts/malgun.ttf")

    elif os_system == 'Linux':
        return os.path.abspath("/usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf")
    


