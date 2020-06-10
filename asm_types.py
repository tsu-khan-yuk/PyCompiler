# Ідентифікатори
# Містять великі букви латинского алфавіту та цифри. Починаються з букви.
# Константи
# Шістнадцятерічні, десяткові, двійкові та текстові константи
# Директиви
# END,
# SEGMENT - без операндів, ENDS, ASSUME,
# MACRO (без параметрів або з одним параметром) ENDM
# DB,DW,DD з одним операндом - константою (строкові константи тільки для DB)
# Розрядність даних та адрес
# 16- розрядні дані та зміщення в сегменті, 32 -розрядні дані та зміщення не
# використовуються
# Адресація операндів пам'яті
# Базова індексна адресація із зміщенням по ідентифікатору (Val1[bp+si],Val1[bx+di]
# Заміна сегментів
# Префікси заміни сегментів можуть задаватись явно, а при необхідності автоматично
# генеруються транслятором

# Cbw
# Inc reg
# Adc reg,reg
# Cmp reg,mem
# And mem,reg
# Mov reg,imm
# Or mem,imm
# Jbe
# Де reg – 8 або 16-розрядні РЗП
# mem – адреса операнда в пам’яті
# imm - 8 або 16 розрядні безпосередні дані (константи)
from re import findall
from .Instrument.Command import Command


cmd_stack = {
    # todo: add names of macro and segments
    "macro": dict(),
    "segment": dict()
}


# todo: добавить структуру для записи комнад и строчек сегментов

lables = []

# Macro = dict()

data = {
    "segments": [],
    "constants": [],
    "lables": []
}
