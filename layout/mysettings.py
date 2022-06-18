import PySimpleGUI  as sg
# Add your dictionary to the PySimpleGUI themes
print("import mysettings.py")

class base:
    width = 600 *2
    height = int(3.3/5 * width)
    font = '"Century Gothic" 12'
    size = (width,height)
    fg,bg = "#89b","#001025"
    color = (fg,bg)
class files(base):
    font ='맑은고딕 12 bold'
    color=('#09f',base.bg)
class cmds(base):
    font ='"Centry Gothic" 11 italic'
    size =(25,1)
    color=('#08f',base.bg)
class folders(base):
    font ='맑은고딕 11 bold'
    color=('#679','black')
    #color=('#679',base.bg)
    size =(14,1)
class cal(base):
    font  = '"Century Gothic" 10 bold'
    #color = ('#cccc00',base.bg)
class AS(base):
    #fg,bg = '#50586C',base.bg
    #fg,bg = base.fg,'#001040'
    fg,bg = base.fg,base.bg
class lbox(base):
    font = '"Century Gothic" 14'
    fg ='#ddd'
    bg = '#03f'

sg.theme('Dark')
sg.set_options(font=base.font,text_color=base.fg,background_color=base.bg,button_color=(base.fg,base.bg) )
sg.theme_background_color(base.bg)
sg.theme_button_color( (base.fg,base.bg) )
sg.theme_element_background_color(base.bg)
sg.theme_input_text_color(base.fg)
sg.theme_input_background_color(base.bg)
# Switch your theme to use the newly added one. You can add spaces to make it more readable
#sg.theme('White')

