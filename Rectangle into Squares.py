def sq_in_rect(lng, wdth):
    squares = []
    area = lng * wdth
    if lng != wdth:
        while area > 0:
            if lng < wdth:
                squares.append(lng)
                wdth = wdth - lng
                area -= lng * lng
            else:
                squares.append(wdth)
                lng = lng - wdth
                area -= wdth * wdth
        return squares