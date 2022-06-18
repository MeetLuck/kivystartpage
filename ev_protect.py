def ev_protect():
    import PySimpleGUI as sg
    from layout.mysettings import base 
    class ifield(base):
        fg,bg = 'black','#bbb'
        font  = ('맑은 고딕',15,'normal')
        pad   = (1,1)
        #font  = ('Centry Gothic',16,'normal')

    class hfield(base):
        fg,bg = '#024','#aaa'
        font  = ('맑은 고딕',14,'normal')
        #font  = ('Centry Gothic',16,'normal')
        color =(fg,bg)
    sg.set_options(font=ifield.font)
    sg.theme_background_color(base.bg)

    def head_B(text,key,size=(12,0),font=hfield.font,color=hfield.color,pad=(0,1),border_width=1):
        return sg.B(text,key=key,enable_events=True,size=size,font=font,button_color=color,pad=pad,border_width=border_width)

    def NO_I(key,size=(6,0),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
        return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)
    def Time_I(key,size=(6,0),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
        return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)
    def dong_I(key,size=(12,1),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
        return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)
    def kind_I(key,size=(12,1),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
        return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)
    def etc_I(key,size=(12,1),font=ifield.font,fg=ifield.fg,bg=ifield.bg,border_width=1):
        return sg.I(key=key,size=size,font=font,background_color=bg,text_color=fg,pad=ifield.pad,border_width=border_width,justification='c',enable_events=True)
    def post_I(key,size=(6,1),font=ifield.font,fg=base.fg,bg=base.bg,border_width=1):
        return sg.I(key=key,size=size,readonly=True,font=font,disabled_readonly_background_color=bg,disabled_readonly_text_color=fg,
               pad=ifield.pad,border_width=border_width,justification='c')
    def ev1_I(key,size=(6,1),font=ifield.font,fg=base.fg,bg=base.bg,border_width=1):
        return sg.I(key=key,size=size,readonly=True,font=font,disabled_readonly_background_color=bg,disabled_readonly_text_color=fg,
               pad=ifield.pad,border_width=border_width,justification='c')
    def col_I(key,size=(12,1),font=ifield.font,fg=base.fg,bg=base.bg,border_width=1):
        return sg.I(key=key,size=size,readonly=True,font=font,disabled_readonly_background_color=bg,disabled_readonly_text_color=fg,
               pad=ifield.pad,border_width=border_width,justification='c')

    row_head = [ head_B('NO','no',size=(6,1)),head_B('일시','time',size=(6,1)),head_B('동-호수','dongho'),head_B('분류','kind'),head_B('초소','post',size=(6,1)), head_B('EV','ev1',size=(6,1)),
                 head_B('보양X','noprotect'),head_B('2호기(설치)','ev2'),head_B('보양재 제거','remove'),head_B('비고','etc')]
    row1  = [ NO_I('rc11'), Time_I('rc12'), dong_I('rc13'), kind_I('rc14'), post_I('rc15'), ev1_I('rc16'),col_I('rc17'), col_I('rc18'), col_I('rc19'), etc_I('rc110')]
    row2  = [ NO_I('rc21'), Time_I('rc22'), dong_I('rc23'), kind_I('rc24'), post_I('rc25'), ev1_I('rc26'),col_I('rc27'), col_I('rc28'), col_I('rc29'), etc_I('rc210')]
    row3  = [ NO_I('rc31'), Time_I('rc32'), dong_I('rc33'), kind_I('rc34'), post_I('rc35'), ev1_I('rc36'),col_I('rc37'), col_I('rc38'), col_I('rc39'), etc_I('rc310')]
    row4  = [ NO_I('rc41'), Time_I('rc42'), dong_I('rc43'), kind_I('rc44'), post_I('rc45'), ev1_I('rc46'),col_I('rc47'), col_I('rc48'), col_I('rc49'), etc_I('rc410')]
    row5  = [ NO_I('rc51'), Time_I('rc52'), dong_I('rc53'), kind_I('rc54'), post_I('rc55'), ev1_I('rc56'),col_I('rc57'), col_I('rc58'), col_I('rc59'), etc_I('rc510')]
    row6  = [ NO_I('rc61'), Time_I('rc62'), dong_I('rc63'), kind_I('rc64'), post_I('rc65'), ev1_I('rc66'),col_I('rc67'), col_I('rc68'), col_I('rc69'), etc_I('rc610')]
    row7  = [ NO_I('rc71'), Time_I('rc72'), dong_I('rc73'), kind_I('rc74'), post_I('rc75'), ev1_I('rc76'),col_I('rc77'), col_I('rc78'), col_I('rc79'), etc_I('rc710')]
    row8  = [ NO_I('rc81'), Time_I('rc82'), dong_I('rc83'), kind_I('rc84'), post_I('rc85'), ev1_I('rc86'),col_I('rc87'), col_I('rc88'), col_I('rc89'), etc_I('rc810')]
    row9  = [ NO_I('rc91'), Time_I('rc92'), dong_I('rc93'), kind_I('rc94'), post_I('rc95'), ev1_I('rc96'),col_I('rc97'), col_I('rc98'), col_I('rc99'), etc_I('rc910')]
    row10 = [ NO_I('rc101'),Time_I('rc102'),dong_I('rc103'),kind_I('rc104'),post_I('rc105'),ev1_I('rc106'),col_I('rc107'),col_I('rc108'),col_I('rc109'),etc_I('rc1010')]
    row11 = [ NO_I('rc111'),Time_I('rc112'),dong_I('rc113'),kind_I('rc114'),post_I('rc115'),ev1_I('rc116'),col_I('rc117'),col_I('rc118'),col_I('rc119'),etc_I('rc1110')]
    row12 = [ NO_I('rc121'),Time_I('rc122'),dong_I('rc123'),kind_I('rc124'),post_I('rc125'),ev1_I('rc126'),col_I('rc127'),col_I('rc128'),col_I('rc129'),etc_I('rc1210')]
    row13 = [ NO_I('rc131'),Time_I('rc132'),dong_I('rc133'),kind_I('rc134'),post_I('rc135'),ev1_I('rc136'),col_I('rc137'),col_I('rc138'),col_I('rc139'),etc_I('rc1310')]
    row14 = [ NO_I('rc141'),Time_I('rc142'),dong_I('rc143'),kind_I('rc144'),post_I('rc145'),ev1_I('rc146'),col_I('rc147'),col_I('rc148'),col_I('rc149'),etc_I('rc1410')]
    row15 = [ NO_I('rc151'),Time_I('rc152'),dong_I('rc153'),kind_I('rc154'),post_I('rc155'),ev1_I('rc156'),col_I('rc157'),col_I('rc158'),col_I('rc159'),etc_I('rc1510')]

    layout = [ row_head,                                                                                        
                row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15
            ]
    window = sg.Window('전출입 및 승강기 현황',layout,background_color=base.bg, margins=(40,30), size=base.size, resizable=True,
                        keep_on_top=False,finalize=True)

    def find_ev1(dong):
        only_evs = 107,131,132,133,134,135,137,143
        return 1 if (int(dong) in only_evs) else None

    def find_must_ev2(dong):
        only_ev2 = 104,123,124,125,138
        return 1 if (int(dong) in only_ev2) else None

        
    def find_post(dong):
        dong_post =[ (None,),(101,103,107), (102,104,111,112,113,114),(105,106,107,108,109,110),(None,),(115,120,121),\
                    (116,117,118,119,123,124,125),(122,126,130,131,132),(127,128,128,133),(134,135,140,141,142,143,144),(136,137,138,139) ]
        posts = [0,1,2,3,4,5,6,7,8,9,10]
        for _post,dongs in zip(posts,dong_post):
            if int(dong) in dongs: return _post
        raise Exception('invalid dong {}'.format(dong))

    def get_value(key): return window[key].get()

    def row_values(row_no):
        # [ row[0], row[1],   row[2],  row[3],  row[4] row[5],  row[6],  row[7],보양재 제거,비고 ]
        # [ 순번,   일시,   동-호수,    분류,   초소,   EV,     보양X,  2호기(설치),보양재 제거,비고 ]
        #   r11,    r12,    r13,        r14,    r15,    r16,    r17,    r18,        r19,        r10
        row = ['']*10
        dong,ho = None,None
        for col in range(1,10+1):
            r1c1 = 'rc{}{}'.format(row_no,col)
            row[col-1] =  get_value(r1c1)
            window[r1c1].update(value=row[col-1])

        for  col in range(1,10+1):
            if len(row[2]) >= 3:
                dong = row[2][:3]
                if row[2].find('-') != -1:
                    t,_ho = row[2].split('-')
                    if len(_ho) >=3:
                        ho = _ho
                print('==> ',dong,ho)
                #print('dong,ho =>',dong,ho)
            if not dong: continue
            # NOTE dong
            row[4] = find_post(dong)
            row[5] = find_ev1(dong)
            #if find_ev1(dong):
            condition1 = ho and (int(ho) in range(101,104+1)) and row[3]
            condition1 = condition1 and ('전' in row[3] or '짐' in row[3] )
            if condition1 or row[9] and 'X' in row[9]:
                print(row[3])
                row[6] = '보양X'
            else:
                row[6] = ''
            if find_must_ev2(dong):
                row[7] = '{}-2'.format(dong)
            if row[1] and int(row[1]) == 9 and  row[5] != 1:
                row[8] = '주간'
            else:
                row[8] = ''
            if row[6] == '보양X': row[8] = ''

            # NOTE window[key=r1c1]
            r1c1 = 'rc{}{}'.format(row_no,col)
            window[r1c1].update(value=row[col-1])

        return row


    while True:
        event,values = window.read(timeout=1000*30)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event in ['no','time','dongho','kind','post','ev1','noprotect','ev2','remove','etc']:
            pass
            #print(event)
        else:
            #row1 = get_value('rc11'), get_value('rc12')
            rows = []
            for row_no in range(1,15+1):
                #print(row_no)
                rows.append( row_values(row_no) )
            print(rows)


    window.close()

if __name__ == '__main__':
    ev_protect()
