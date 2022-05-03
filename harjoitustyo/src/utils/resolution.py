def get_lower_res(screen_dimensions):
    """Palautta pienemmän ikkunavektorin x/y

    Args:
        screen_dimensions: Ikkunan koko taulukkona [x,y]

    Returns:
        Pienempi x/y -arvo
    """

    return min(screen_dimensions)


def get_font_size(lower_res):
    """Laskee fonttikoon riippuen ikkunan koosta

    Args:
        lower_res: Ikkunan pienempi x tai y -arvo

    Returns:
        Fonttikoko
    """

    return int(lower_res * 0.075)
