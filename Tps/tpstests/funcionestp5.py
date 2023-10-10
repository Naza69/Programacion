def repeat(choicelocal):
    while choicelocal.lower()!="si" and choicelocal.lower()!="no":
        choicelocal=("Respuesta invalida, intente nuevamente (Si o no)")
        if choicelocal.lower()=="si":
            break
        if choicelocal.lower()=="no":
            break
    if choicelocal.lower()=="si":
        return True
    else: 
        return False
def booldni(dnilocal):
    if len(str(dnilocal))==7 or len(str(dnilocal))==8:
        return True
    else:
        return False