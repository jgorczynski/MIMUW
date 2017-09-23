import subprocess

inStr = "Ala ma kota\nKot ma psa\n..."
res = subprocess.run(["grep", "-v", "A"], input=inStr.encode(), stdout=subprocess.PIPE)

print("Kod powrotu to: " + str(res.returncode))
print("Standardowe wyjście z komendy to: " + res.stdout.decode())

subprocess.run(["sleep 1; ls -ld /etc/pa*"], shell=True)

