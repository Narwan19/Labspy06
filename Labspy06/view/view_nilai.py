from model.daftar_nilai import kontak


def header():
    print("\n                       PROGRAM INPUT DATA MAHASISWA                      ")
    print("___________________________________________________________________________")
    print("\n  (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar")


def notoption():
    print(" __________________________")
    print("| Pilih opsi yang tersedia |")
    print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("  (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar  ")


def cetak():
    print("\n===========================================================================")
    print("========================== DAFTAR DATA MAHASISWA ==========================")
    print("===========================================================================")
    print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
    print("===========================================================================")
    no = 1
    for tabel in kontak.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
    print("===========================================================================")
    print("\n  (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar")


def nyari():
    from view.input_nilai import carive
    carive()
    print("  (T)ambah       (U)bah      (H)apus     (C)ari      (L)ihat     (K)eluar   ")