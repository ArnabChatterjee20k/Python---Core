with open("Output4.xlsx","rb") as f:
    with open("newfile.xlsx","ab") as g:
        for i in f:
            g.write(i)
