def resize_video(width, height, max_width):
    if width > max_width:
        ratio = max_width / width
        new_width = int(width * ratio)
        new_height = int(height * ratio)
        return new_width, new_height
    return width, height
