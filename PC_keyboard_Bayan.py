import pgzrun

# Размер окна
WIDTH = 800
HEIGHT = 560
TITLE = "PC keyboard BAYAN"

# Словарь "Значение клавиши" : [НОТА, (x,y позиция кнопки)]
nots_spisok = {
               # Правая клавиатура
               "keys.Q":[sounds.a1, (693,152)], "keys.A":[sounds.a1_d, (711,163)], "keys.Z":[sounds.b1, (730,175)], "keys.W":[sounds.c2, (693, 178)], "keys.S":[sounds.c2_d, (711, 190)], "keys.X":[sounds.d2, (730, 202)],
               "keys.E":[sounds.d2_d, (693, 205)], "keys.D":[sounds.e2, (711, 217)], "keys.C":[sounds.f2, (730, 229)], "keys.R":[sounds.f2_d, (693, 232)], "keys.F":[sounds.g2, (711, 244)], "keys.V":[sounds.g2_d, (730, 256)],
               "keys.T":[sounds.a2, (693, 259)], "keys.G":[sounds.a2_d, (711, 271)], "keys.B":[sounds.b2, (730, 283)], "keys.Y":[sounds.c3, (693, 286)], "keys.H":[sounds.c3_d, (711, 298)], "keys.N":[sounds.d3, (730, 310)],
               "keys.U":[sounds.d3_d, (693, 313)], "keys.J":[sounds.e3, (711, 325)], "keys.M":[sounds.f3, (730, 337)], "keys.I":[sounds.f3_d, (693, 340)], "keys.K":[sounds.g3, (711, 352)], "keys.COMMA":[sounds.g3_d, (730, 364)],
               "keys.O":[sounds.a3, (693, 367)], "keys.L":[sounds.a3_d, (711, 379)], "keys.PERIOD":[sounds.b3, (730, 391)], "keys.P":[sounds.c4, (693, 394)], "keys.SEMICOLON":[sounds.c4_d, (711, 406)], "keys.SLASH":[sounds.d4, (730, 418)],
               "keys.LEFTBRACKET":[sounds.d4_d, (693, 421)], "keys.QUOTE":[sounds.e4, (711, 433)], "keys.RSHIFT":[sounds.f4, (730, 445)], "keys.RIGHTBRACKET":[sounds.f4_d, (693, 448)], "keys.BACKSLASH":[sounds.g4, (711, 460)],
               # Левая клавиатура
               "keys.KP_MINUS":[sounds.b, (122, 217)], "keys.KP_PLUS":[sounds.b_min, (86, 196)], "keys.KP_ENTER":[sounds.b_7, (68, 186)],
               "keys.KP_MULTIPLY":[sounds.e, (122, 240)], "keys.KP_9":[sounds.e_maj, (104, 229)], "keys.KP_6":[sounds.e_min, (86, 219)], "keys.KP_3":[sounds.e_7, (68, 208)],
               "keys.KP_DIVIDE":[sounds.a, (122, 263)], "keys.KP_8":[sounds.a_maj, (104, 251)], "keys.KP_5":[sounds.a_min, (86, 241)], "keys.KP_2":[sounds.a_7, (68, 230)],
               "keys.NUMLOCKCLEAR":[sounds.d, (122, 284)], "keys.KP_7":[sounds.d_maj, (104, 273)], "keys.KP_4":[sounds.d_min, (86, 263)], "keys.KP_1":[sounds.d_7, (68, 252)],
               "keys.PAGEUP":[sounds.g, (122, 306)], "keys.PAGEDOWN":[sounds.g_maj, (104, 295)], "keys.RIGHT":[sounds.g_min, (86, 285)],
               "keys.HOME":[sounds.c, (122, 328)], "keys.END":[sounds.c_maj, (104, 317)], "keys.UP":[sounds.c_min, (86, 307)], "keys.DOWN":[sounds.c_7, (68, 296)],
               "keys.INSERT":[sounds.f, (122, 350)], "keys.DELETE":[sounds.f_maj, (104, 339)], "keys.LEFT":[sounds.f_min, (86, 329)]
               }

xout = (-30, -30) # Позиция x,y за экраном

# Создаем кнопки, которые будут появляться при нажатии
knopka1 = Actor("ball", xout)
knopka2 = Actor("ball", xout)
knopka3 = Actor("ball", xout)
knopka4 = Actor("ball", xout)
knopka5 = Actor("ball", xout)

# Кнопка "ABOUT", логотип
about = Actor("about_knob", (400, 530))
logo = Actor("logo", (400, 60))


# При нажатии клавиши будет играть соответствующая нота
def on_key_down(key):
    # Смотрим ключи словаря:
    for i in nots_spisok.keys():
        # Если str нажатой клавиши совпадает с ключем словаря,
        if str(key) == i:
            # Воспроизводим значение (ноту) этого ключа
            nots_spisok[i][0].play(-1)
            # Отображаем нажатую кнопку на экране
            # Если графическая кнопка не задействована на экране в данный момент,
            # то используем ее. Так для всех кнопок
            if knopka1.pos == xout:
                knopka1.pos = nots_spisok[i][1]
            elif knopka2.pos == xout:
                knopka2.pos = nots_spisok[i][1]
            elif knopka3.pos == xout:
                knopka3.pos = nots_spisok[i][1]
            elif knopka4.pos == xout:
                knopka4.pos = nots_spisok[i][1]
            else:
                knopka5.pos = nots_spisok[i][1]


# При отпускании клавиши звучащая нота выключается
def on_key_up(key):
    for i in nots_spisok.keys():
        if str(key) == i:
            # Отключаем звучание соответствующей ноты
            nots_spisok[i][0].stop()
            # Убираем отпущеную кнопку с экрана
            if knopka1.pos == nots_spisok[i][1]:
                knopka1.pos = xout
            elif knopka2.pos == nots_spisok[i][1]:
                knopka2.pos = xout
            elif knopka3.pos == nots_spisok[i][1]:
                knopka3.pos = xout
            elif knopka4.pos == nots_spisok[i][1]:
                knopka4.pos = xout
            else:
                knopka5.pos = xout

# About manual
def on_mouse_down(pos):
    # Вызов странички с инструкцией при клике мышью на "ABOUT"
    if about.collidepoint(pos):
        about.image = "instruction_full"
        about.y = 300
    # Спрятать при клике мышью не на инструкцию
    else:
        about.image = "about_knob"
        about.y = 530

# Рисуем объекты
def draw():
    screen.clear()
    screen.blit("bajan_full", (0,0))
    logo.draw()
    knopka1.draw()
    knopka2.draw()
    knopka3.draw()
    knopka4.draw()
    knopka5.draw()
    about.draw()
    

# Запуск приложения
pgzrun.go()
