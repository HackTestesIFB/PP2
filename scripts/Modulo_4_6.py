from perfis.models import Perfil

def Modulo_4_3():
    perfil = Perfil.objects.create(nome='Steve', email='steve@minecraft.com', telefone='n/a', nome_empresa='IFB')
    print(perfil.id) # Imprime o ID
    perfil.delete() # Deleta o perfil


def Modulo_4_4():
    p = Perfil.objects.create(nome='Steve', email='steve@minecraft.com', telefone='n/a', nome_empresa='IFB')
    p = Perfil.objects.get(id=1) #Perfil 1 deve existir
    print(p.nome)
    p = Perfil.objects.get(nome='Steve') #Steve deve existir - pesquisa pelo nome
    print(p.id)
    p = Perfil.objects.get(email='steve@minecraft.com') #Steve deve existir - pesquisa pelo email
    print(p.id)
    p.delete()


def Modulo_4_5():
    perfil_01 = Perfil.objects.create(nome='Steve', email='steve@minecraft.com', telefone='n/a', nome_empresa='IFB')
    perfil_02 = Perfil.objects.create(nome='Oswaldo', email='oswaldo@oswaldo.com', telefone='n/a', nome_empresa='IFB')
    perfis = Perfil.objects.filter(nome__startswith='Oswaldo') # Pesquisa pelo nome que comece com o padrão inserido
    for perfil in perfis:
        print(perfil.nome)
    perfil_01.delete()
    perfil_02.delete()


Modulo_4_3()
Modulo_4_3()
Modulo_4_5()

