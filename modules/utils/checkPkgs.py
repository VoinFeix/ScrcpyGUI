import shutil

def checkPkgs():
    pkgs: list = ['adb', 'scrcpy']
    notFound = False

    for pkg in pkgs:
        print(f"[System]: Checking for {pkg}...")
        if not shutil.which(pkg):
            print(f"{pkg} not found.")
            notFound = True
        else:
            print(f"[System]: {pkg} found.")
    
    if notFound:
        raise Exception("Required Packages not found.")
