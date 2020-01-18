from view.view_nilai import nyari,cetak,header,notoption
from view.input_nilai import inputan,edit,delett
header()
while True:

    c = input("\nPilih Opsi: ")

    # EXIT PROGRAM
    if c.lower() == 'k':
        print("TERIMA KASIH ANDA TELAH MENGGUNAKAN PROGRAM INI :)")
        ext = input("\nTekan ENTER untuk keluar dari program")
        if ext == '':
            break
        else:
            break

    # PRINT DATA
    elif c.lower() == 'l':
        cetak()

    # MENAMBAH DATA
    elif c.lower() == 't':
        inputan()

    # EDIT DATA
    elif c.lower() == 'u':
        edit()

    # MENCARI DATA
    elif c.lower() == 'c':
        nyari()

    # HAPUS DATA
    elif c.lower() == 'h':
        delett()

    else:
        notoption()