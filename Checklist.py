import PySimpleGUI as sg

def janela_inicial():
    sg.theme('LightBrown12')
    
    layout = [
        [sg.Frame('Afazer', [[sg.Checkbox(''), sg.Input('')]], key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Formatar')]
    ]

    return sg.Window('Checklist', layout=layout, finalize=True)

#criar a janela
janela = janela_inicial()

#criando as regras
while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
   
    elif event == 'Formatar':
        janela.close()
        janela = janela_inicial()
