import PySimpleGUI as sg
sg.theme('DarkBlue')

win_W = 300
win_H = 300
filename = None
startup = True

#file funtions
file_new = 'New   (CTRL+N)'
file_open = 'Open (CTRL+O)'
file_save = 'Save (CTRL+S)'


FileMenu =[['File',[file_new, file_open, file_save, 'Save As', 'Exit  (Alt+F4)']],
                  ['Tools', ['Word count']],
                  ['Help', ['About']]]

layout = [[sg.Menu(FileMenu)],
          [sg.Text('>New File<', font=('Arial', '12'), size=(win_W, 1), key='-INFO-')],
          [sg.Multiline(font=('Arial', '12'), size=(win_W, win_H), key='-BODY-')]]
          
window = sg.Window('NotePad', layout=layout, margins = (0,0), resizable = True,return_keyboard_events=True)
window.read(timeout=1)
window.maximize()
window['-BODY-'].expand(expand_x =True, expand_y=True)

        
def new_file() -> str:
    window['-BODY-'].update(value='')
    window['-INFO-'].update(value = '> New File <')
    filename = None
    return filename

def open_file() ->str:
    try:
        filename: str = sg.popup_get_file('Open', no_window = True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename,tuple):
        with (filename, 'r') as f:
            window['-BODY-'].update(value=f.read())
        window['-INFO-'].update(value=filename)
    return filename
    
def savefile(filename: str):
    if filename not in (None, ''):
        with (filename, 'w') as f:
            f.write(values.get('-BODY-'))
        window['-INFO-'].update(value=filename)
    else:
        save_file_as()
    
def save_file_as() ->str:
    try:
        filename: str = sg.popup_get_file('Save File',save_as = True, no_window = True)
    except:
        return
    if filename not in (None, '') and not isinstance(filename,tuple):
        with (filename, 'w') as f:
            f.write(values.get('-BODY-'))
        window['-INFO-'].update(value=filename)
    return filename
    
    
def word_count():
    words = [w for w in values['-BODY-'].split(' ') if w != '\n']
    word_count_ = len(words)
    sg.PopupQuick('word count:{:,d}'.format(word_count_), auto_close = True)
    
def about_me():
    sg.PopupQuick('ALL aboutthe programming', auto_close = False)
   
while True:
    event, values = window.read()
    
    if event in (None, 'Exit'):
        break
    
    if event in (file_new, 'n:78'):
        filename = new_file()
    
    if event in (file_open, 'o:79'):
        filename  = open_file()
    
    if event in (file_save, 's:83'):
        savefile(filename)
          
    if event in ('Save As',):
        filename = save_file_as()
        
    if event in ('Word count',):
        word_count()
    
    if event in ('About',):
        about_me()
