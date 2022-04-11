def get_lower_res(screen_dimensions):
    return min(screen_dimensions)


def get_font_size(lower_res):
    return int(lower_res * 0.075)
