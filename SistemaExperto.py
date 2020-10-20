
###########################################
#ENTRADA
'''
'Sibilancias inspiratorias'
'Disnea'
'Dolor en el pecho'
'Fatiga'
'Tos noctura'
'Estornudos'
'Taponamiento nasal'
'Secrecion nasal'
'Prurito nasal'
'Lagrimeo ocular'
'Prurito ocular'
'Lesiones pliegues (brazos-piernas)'
'Prurito'
'Piel seca'
'Ronchas'
'Hinchazon ocular/facial/labial' '''

def Diagnostica(txtsintoma1= "", txtsintoma2= "", txtsintoma3= "", txtsintoma4= "", txtsintoma5= "", txtsintoma6= "", txtsintoma7= "", txtsintoma8= "", txtsintoma9= "", txtsintoma10= ""):
    txtporcentaje = 0
    txtdiagnostico = ""
    txttratamiento = ""

    ###ASMA BLOQUE SINTOMA1
    s1 = 'Sibilancias inspiratorias'
    s2 = 'Disnea'
    s3 = 'Dolor en el pecho'
    s4 = 'Fatiga'
    s5 = 'Tos noctura'
    porcent1= 0
    porcent2 = 0
    porcent3 = 0
    porcent4 = 0
    porcent5 = 0

    if ( txtsintoma1 == s1 or txtsintoma2 == s1 or txtsintoma3 == s1 or txtsintoma4 == s1 or txtsintoma5 == s1 or txtsintoma6 == s1 or txtsintoma7 == s1 or txtsintoma8 == s1 or txtsintoma9 == s1 or txtsintoma10 == s1 ) :
        porcent1 = 30
    if ( txtsintoma1 == s2 or txtsintoma2 == s2 or txtsintoma3 == s2 or txtsintoma4 == s2 or txtsintoma5 == s2 or txtsintoma6 == s2 or txtsintoma7 == s2 or txtsintoma8 == s2 or txtsintoma9 == s2 or txtsintoma10 == s2 ) :
        porcent2 = 20
    if ( txtsintoma1 == s3 or txtsintoma2 == s3 or txtsintoma3 == s3 or txtsintoma4 == s3 or txtsintoma5 == s3 or txtsintoma6 == s3 or txtsintoma7 == s3 or txtsintoma8 == s3 or txtsintoma9 == s3 or txtsintoma10 == s3 ) :
        porcent3 = 20
    if ( txtsintoma1 == s4 or txtsintoma2 == s4 or txtsintoma3 == s4 or txtsintoma4 == s4 or txtsintoma5 == s4 or txtsintoma6 == s4 or txtsintoma7 == s4 or txtsintoma8 == s4 or txtsintoma9 == s4 or txtsintoma10 == s4 ) :
        porcent4 = 10
    if ( txtsintoma1 == s5 or txtsintoma2 == s5 or txtsintoma3 == s5 or txtsintoma4 == s5 or txtsintoma5 == s5 or txtsintoma6 == s5 or txtsintoma7 == s5 or txtsintoma8 == s5 or txtsintoma9 == s5 or txtsintoma10 == s5 ) :
        porcent5 = 20
    totalasma = porcent1 + porcent2 + porcent3 + porcent4 + porcent5

    #RINITIS BLOQUE SINTOMA2
    ss1 = 'Estornudos'
    ss2 = 'Taponamiento nasal'
    ss3 = 'Secrecion nasal'
    ss4 = 'Prurito nasal'
    ss5 = 'Lagrimeo ocular'
    ss6 = 'Prurito ocular'
    pporcent1 = 0
    pporcent2 = 0
    pporcent3 = 0
    pporcent4 = 0
    pporcent5 = 0
    pporcent6 = 0
    if ( txtsintoma1 == ss1 or txtsintoma2 == ss1 or txtsintoma3 == ss1 or txtsintoma4 == ss1 or txtsintoma5 == ss1 or txtsintoma6 == ss1 or txtsintoma7 == ss1 or txtsintoma8 == ss1 or txtsintoma9 == ss1 or txtsintoma10 == ss1 ) :
        pporcent1 = 15
    if ( txtsintoma1 == ss2 or txtsintoma2 == ss2 or txtsintoma3 == ss2 or txtsintoma4 == ss2 or txtsintoma5 == ss2 or txtsintoma6 == ss2 or txtsintoma7 == ss2 or txtsintoma8 == ss2 or txtsintoma9 == ss2 or txtsintoma10 == ss2 ) :
        pporcent2 = 15
    if ( txtsintoma1 == ss3 or txtsintoma2 == ss3 or txtsintoma3 == ss3 or txtsintoma4 == ss3 or txtsintoma5 == ss3 or txtsintoma6 == ss3 or txtsintoma7 == ss3 or txtsintoma8 == ss3 or txtsintoma9 == ss3 or txtsintoma10 == ss3 ) :
        pporcent3 = 15
    if ( txtsintoma1 == ss4 or txtsintoma2 == ss4 or txtsintoma3 == ss4 or txtsintoma4 == ss4 or txtsintoma5 == ss4 or txtsintoma6 == ss4 or txtsintoma7 == ss4 or txtsintoma8 == ss4 or txtsintoma9 == ss4 or txtsintoma10 == ss4 ) :
        pporcent4 = 25
    if ( txtsintoma1 == ss5 or txtsintoma2 == ss5 or txtsintoma3 == ss5 or txtsintoma4 == ss5 or txtsintoma5 == ss5 or txtsintoma6 == ss5 or txtsintoma7 == ss5 or txtsintoma8 == ss5 or txtsintoma9 == ss5 or txtsintoma10 == ss5 ) :
        pporcent5 = 15
    if ( txtsintoma1 == ss6 or txtsintoma2 == ss6 or txtsintoma3 == ss6 or txtsintoma4 == ss6 or txtsintoma5 == ss6 or txtsintoma6 == ss6 or txtsintoma7 == ss6 or txtsintoma8 == ss6 or txtsintoma9 == ss6 or txtsintoma10 == ss6 ) :
        pporcent6 = 15
    totalrinitis = pporcent1 + pporcent2 + pporcent3 + pporcent4 + pporcent5 + pporcent6

    #DERMATITIS ATOPICA BLOQUE SINTOMA3
    ds1 = 'Lesiones pliegues (brazos-piernas)'
    ds2 = 'Prurito'
    ds3 = 'Piel seca'
    Dporcen1 = 0
    Dporcen2 = 0
    Deporcen3 = 0
    if ( txtsintoma1 == ds1 or txtsintoma2 == ds1 or txtsintoma3 == ds1 or txtsintoma4 == ds1 or txtsintoma5 == ds1 or txtsintoma6 == ds1 or txtsintoma7 == ds1 or txtsintoma8 == ds1 or txtsintoma9 == ds1 or txtsintoma10 == ds1 ) :
        Dporcen1 = 25
    if ( txtsintoma1 == ds2 or txtsintoma2 == ds2 or txtsintoma3 == ds2 or txtsintoma4 == ds2 or txtsintoma5 == ds2 or txtsintoma6 == ds2 or txtsintoma7 == ds2 or txtsintoma8 == ds2 or txtsintoma9 == ds2 or txtsintoma10 == ds2 ) :
        Dporcen2 = 50
    if ( txtsintoma1 == ds3 or txtsintoma2 == ds3 or txtsintoma3 == ds3 or txtsintoma4 == ds3 or txtsintoma5 == ds3 or txtsintoma6 == ds3 or txtsintoma7 == ds3 or txtsintoma8 == ds3 or txtsintoma9 == ds3 or txtsintoma10 == ds3 ) :
        Deporcen3 = 25
    totaldermatitis = Dporcen1 + Dporcen2 + Deporcen3

    #URTICARIA - BLOQUE SINTOMA3
    Uporcen1 = 0
    Uporcen2 = 0
    us1 = 'Ronchas'
    us2 = 'Hinchazon ocular/facial/labial'
    if ( txtsintoma1 == us1 or txtsintoma2 == us1 or txtsintoma3 == us1 or txtsintoma4 == us1 or txtsintoma5 == us1 or txtsintoma6 == us1 or txtsintoma7 == us1 or txtsintoma8 == us1 or txtsintoma9 == us1 or txtsintoma10 == us1 ) :
        Uporcen1 = 75
    if ( txtsintoma1 == us2 or txtsintoma2 == us2 or txtsintoma3 == us2 or txtsintoma4 == us2 or txtsintoma5 == us2 or txtsintoma6 == us2 or txtsintoma7 == us2 or txtsintoma8 == us2 or txtsintoma9 == us2 or txtsintoma10 == us2 ) :
        Uporcen2 = 25
    totalurticaria = Uporcen1 + Uporcen2

    if ( totalasma >= 30 or totaldermatitis >= 50 or totalrinitis >= 50 or totalurticaria >= 50 ) :
        if ( totalasma >= 30 ) :
            txtporcentaje = totalasma
            txtdiagnostico = 'ASMA'
            txttratamiento = 'Tratamiento preventivo *Corticoide inhalado *Inmunoterapia / Tratamiento de crisis: Broncodilatadores'
        if ( totalrinitis >= 50 ) :
            txtporcentaje = totalrinitis
            txtdiagnostico = 'RINITIS'
            assert False, '# UNTRANSLATED VB LINE #108 [txttratamiento.Text = " *Corticoide tópico inhalado vía oral *Antihistamínico vía oral" Label12.Visible = True]'
        if ( totaldermatitis >= 50 ) :
            txtporcentaje = totaldermatitis
            txtdiagnostico = 'DERMATITIS'
            txttratamiento = ' *Emolientes e hidratantes de la piel *Corticoide tópico *Antihistamínico *Antibiótico'
        if ( totalurticaria >= 50 ) :
            txtporcentaje = totalurticaria
            txtdiagnostico = 'URTICARIA'
            txttratamiento = ' *Antihistamínico *Corticoide vía oral *Antileucotrieno'
    else:
        print('Síntomas insuficientes para determinar la enfermedad. Por favor, seleccione nuevamente.')

    return txtporcentaje, txtdiagnostico, txttratamiento



def Control(txtenfermedad= "", L1= False, M1= False, A1= False, L2= False, M2= False, A2= False, L3= False, M3= False, A3= False, L4= False, M4= False, A4= False, L5= False, M5= False, A5= False, L6= False, M6= False, A6= False):

    """ASMA"""
    porcen1 = 0
    porcen2 = 0
    porcen3 = 0
    porcen4 = 0
    porcen5 = 0
    porcen6 = 0
    porcentajenuevo= 0
    txtMensaje= ""

    if txtenfermedad == 'ASMA':
        #sibilancias espiratorias
        if L1 ==True:
            porcen1 = 10
        if M1 ==True:
            porcen1 = 20
        if A1 ==True:
            porcen1 = 30
        #disneax
        if L2 ==True:
            porcen2 = 5
        if M2 ==True:
            porcen2 = 15
        if A2 ==True:
            porcen2 = 20
        #dolor en el pecho
        if L3 ==True:
            porcen3 = 5
        if M3 ==True:
            porcen3 = 15
        if A3 ==True:
            porcen3 = 20
        #fatiga
        if L4 ==True:
            porcen4 = 3
        if M4 ==True:
            porcen4 = 7
        if A4 ==True:
            porcen4 = 10
        #tos nocturna
        if L5 ==True:
            porcen5 = 5
        if M5 ==True:
            porcen5 = 15
        if A5 ==True:
            porcen5 = 20
        porcentajenuevo = porcen1 + porcen2 + porcen3 + porcen4 + porcen5
        #RINITIS
    elif txtenfermedad == 'RINITIS':
        #estornudos
        if L1 ==True:
            porcen1 = 5
        if M1 ==True:
            porcen1 = 10
        if A1 ==True:
            porcen1 = 15
        #taponamiento nasal
        if L2 ==True:
            porcen2 = 5
        if M2 ==True:
            porcen2 = 10
        if A2 ==True:
            porcen2 = 15
        #secrecion nasal
        if L3 ==True:
            porcen3 = 5
        if M3 ==True:
            porcen3 = 10
        if A3 ==True:
            porcen3 = 15
        #prurito nasal
        if L4 ==True:
            porcen4 = 10
        if M4 ==True:
            porcen4 = 15
        if A4 ==True:
            porcen4 = 25
        #lagrimeo ocular
        if L5 ==True:
            porcen5 = 5
        if M5 ==True:
            porcen5 = 10
        if A5 ==True:
            porcen5 = 15
        #prurito ocular
        if L6 ==True:
            porcen6 = 5
        if M6 ==True:
            porcen6 = 10
        if A6 ==True:
            porcen6 = 15
        porcentajenuevo = porcen1 + porcen2 + porcen3 + porcen4 + porcen5 + porcen6
        #DERMATITIS
    elif txtenfermedad == 'DERMATITIS':
        #lesiones en pliegues
        if L1 ==True:
            porcen1 = 10
        if M1 ==True:
            porcen1 = 15
        if A1 ==True:
            porcen1 = 25
        #prurito
        if L2 ==True:
            porcen2 = 10
        if M2 ==True:
            porcen2 = 35
        if A2 ==True:
            porcen2 = 50
        #piel seca
        if L3 ==True:
            porcen3 = 10
        if M3 ==True:
            porcen3 = 15
        if A3 ==True:
            porcen3 = 25
        porcentajenuevo = porcen1 + porcen2 + porcen3
        #URTICARIA
    elif txtenfermedad == 'URTICARIA':
        #ronchas
        if L1 ==True:
            porcen1 = 25
        if M1 ==True:
            porcen1 = 50
        if A1 ==True:
            porcen1 = 75
        #hinchazon
        if L2 ==True:
            porcen2 = 10
        if M2 ==True:
            porcen2 = 15
        if A2 ==True:
            porcen2 = 25
        porcentajenuevo = porcen1 + porcen2

    if porcentajenuevo > 1 and porcentajenuevo < 30:
        txtMensaje = 'Felicitaciones! El paciente ha obtenido un CONTROL TOTAL de su enfermedad. No tiene limitaciones respecto a su diagnóstico'
    if porcentajenuevo > 31 and porcentajenuevo < 50:
        txtMensaje = 'Cerca del Objetivo! La enfermedad está BIEN CONTROLADA aunque se deberá revisar el plan de medicación y consultar al paciente por el plan de control ambiental y/o alimentario'
    if porcentajenuevo > 51 and porcentajenuevo < 101:
        txtMensaje = 'Lejos del Objetivo! Pueda que la enfermedad NO ESTÉ CONTROLADA. El paciente no está tomando la medicación ni siguiendo las indicaciones de control ambiental y/o alimentario'

    return(porcentajenuevo, txtMensaje)

txtporcentaje, txtdiagnostico, txttratamiento= Diagnostica("Sibilancias inspiratorias", "Dolor en el pecho", "Fatiga", 'Tos noctura')
print(txtporcentaje)
print(txtdiagnostico)
print(txttratamiento)

print("\n\nahora control")
decision, mensaje= Control('ASMA',True,False,False,False,False,False,True,False,False)
print(decision)
print(mensaje)
