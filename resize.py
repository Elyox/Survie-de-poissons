def console_resize(width=80, height=24, buffer_height=600):
    '''Sets up the console size and buffer height.

    <at> param width {int} Width of console in column value.
    <at> param height {int} Height of console in row value.
    <at> param buffer_height {int} Buffer console height in row value.
    '''
    from ctypes import windll, byref, create_string_buffer
    from ctypes.wintypes import SMALL_RECT, _COORD
    # Active console screen buffer
    # STD_OUTPUT_HANDLE -> -11, STD_ERROR_HANDLE -> -12)
    STDERR = -12
    # SMALL_RECT input
    LEFT = 0
    TOP = 0
    RIGHT = width - 1
    BOTTOM = height - 1
    # handle
    hdl = windll.kernel32.GetStdHandle(STDERR)
    csbi = create_string_buffer(22)

    res = windll.kernel32.GetConsoleScreenBufferInfo(hdl, csbi)

    if res:
        import struct
        (bufx, bufy, curx, cury, wattr,
         left, top, right, bottom,
         maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)

    # current_width = right - left + 1
    # current_height = bottom - top + 1
    current_buffer_height = bufy

    if buffer_height < height:
        buffer_height = height
    # order of resizing avoiding some problems
    if current_buffer_height > buffer_height:
        rect = SMALL_RECT(LEFT, TOP, RIGHT, BOTTOM)  # (left,top,right,bottom)
        windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))

        bufsize = _COORD(width, buffer_height)  # columns, rows
        windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)
    else:
        bufsize = _COORD(width, buffer_height)  # columns, rows
        windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)

        rect = SMALL_RECT(LEFT, TOP, RIGHT, BOTTOM)  # (left,top,right,bottom)
        windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))
