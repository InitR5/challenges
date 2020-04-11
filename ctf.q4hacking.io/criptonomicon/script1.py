import subprocess
FRASE="""./snow -p "{0}" -C -Q mensaje-interceptado.txt"""


with open("rockyou.txt") as dic:
    for line in dic:
        line=line.strip()
        try:
            valor=subprocess.check_output(FRASE.format(line),shell=True)
            if "LTN{" in str(valor):
                print(valor)
                print(line)
        except Exception as e:
            pass
