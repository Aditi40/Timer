import random,time,math
from pyray import *

backgroundColor,buttonColor = SKYBLUE,BLACK

set_trace_log_level(LOG_NONE)
ScreenWidth,ScreenHeight = 800,450 
init_window(ScreenWidth,ScreenHeight, "Timer")

time = 100
second = 0
over = False
pause = True

def stopButton():
    global pause,second
    ORect = Rectangle(600,250,200,200)
    draw_rectangle_lines_ex(ORect,5,buttonColor)
    draw_text("\n   Stop",600,250,40,buttonColor)
    if (check_collision_point_rec(get_mouse_position(),ORect)):
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            second = 0
            draw_text("TIME UP!!!",0,330,120,buttonColor)
            pause = False

def pauseButton():
    global pause
    PRect = Rectangle(600,0,200,200)
    draw_rectangle_lines_ex(PRect,5,buttonColor)
    draw_text("  Pause\n     &\n   Play",600,0,40,buttonColor)
    if (check_collision_point_rec(get_mouse_position(),PRect)):
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            if pause == True:
                pause = False
                
            elif pause == False:
                pause = True

def setTimer():
    global second
    HPlus = Rectangle(0,0,200,100)
    MPlus = Rectangle(200,0,200,100)
    SPlus = Rectangle(400,0,200,100)
    draw_rectangle_lines_ex(HPlus,5,buttonColor)
    draw_rectangle_lines_ex(MPlus,5,buttonColor) 
    draw_rectangle_lines_ex(SPlus,5,buttonColor)
    draw_text(" +1h   +1m  +1s",0,10,80,buttonColor)
    
    if (check_collision_point_rec(get_mouse_position(),HPlus)):
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            second += 3600
    if (check_collision_point_rec(get_mouse_position(),MPlus)):
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            second += 60
    if (check_collision_point_rec(get_mouse_position(),SPlus)):
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            second += 1

def draw():
    draw_text(f"{math.floor(second/3600)}:{math.floor(second/60)%60}:{second%60}",0,135,180,buttonColor)

def update():
    global time,second
    time += get_frame_time()
    if time > 1 and pause:
        time = 0
        second -= 1
    if second < 1:
        second = 0
        draw_text("TIME UP!!!",0,330,120,buttonColor)
    if pause == False:
        draw_text("Paused",0,330,120,buttonColor)

while not window_should_close():
    begin_drawing()
    clear_background(backgroundColor)
    update()
    pauseButton()
    stopButton()
    draw()
    setTimer()
    end_drawing()
close_window()
