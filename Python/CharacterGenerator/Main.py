import random
import time
import Lists

print ("- - - - - CRIADOR DE PERSONAGENS, BETA 0.5 - - - - -\n")

seed_input = False
nsfw = False
id_min = 18
id_max = 80
id_min_par = 18
id_max_par = 80

def set_altura(idd):
      if idd <= 10:
            x = round(((random.uniform(raça[1], raça[2])) / 4), 2)
      elif idd <= 17:
            x = round(((random.uniform(raça[1], raça[2])) / 2), 2)
      elif idd <= 25:
            x = round((random.uniform(raça[1], raça[2])), 2)
      elif idd <= 50:
            x = round((random.uniform(raça[1], raça[2]) * 1.05), 2)
      else:
            x = round((random.uniform(raça[1], raça[2]) * 1.15), 2)

      return x

def set_profissão():
      n = random.randint(1, 100)

      if n <= 35:
            x = random.choice(Lists.trabalhos)
      elif n <= 65:
            x = random.choice(Lists.profissões_baixas)
      elif n <= 90:
            x = random.choice(Lists.profissões_médias)
      else:
            x = random.choice(Lists.profissões_altas)
      
      return x

def set_profissão_level():
      n = random.randint(1, 100)

      if n <= 5:
            x = random.randint(17, 20)
      elif n <= 25:
            x = random.randint(11, 16)
      elif n <= 75:
            x = random.randint(5, 10)
      else:
            x = random.randint(1, 5)
      
      return x

def set_salário(x, y):
      if x in Lists.trabalhos:
            z = random.randint(1, 100)
            z = z + round((z * y)/100)
      else:
            z = x[1]
            z = z + round((z * y)/100)

      return z

def set_gastos():
      n = random.randint(1, 100)
      if n <= 35:
            x = round(salário / 4)
            y = round((salário * 24) / 4)
            z = "economizar"
            n2 = 4
      elif n <= 75:
            x = round(salário / 3)
            y = round((salário * 24) / 3)
            z = "gastar habitualmente"
            n2 = 3
      else:
            x = round(salário / 2)
            y = round((salário * 24) / 2)
            z = "gastos exagerados"
            n2 = 2
      k = round(((salário * 24) * idade) / n2)
      return x, y, z, k

def set_status():
      n = random.randint(1, 100)
      if n <= 15:
            x = random.randint(1, 3)
      elif n <= 90:
        x = random.randint(3, 7)
      else:
           x = random.randint(8, 10)
      return x

def set_morais():
      n = random.randint(1, 5)
      match n:
            case 1:
                  x = "boas intenções"
            case 2:
                  x = "inclinamento ao bem"
            case 3:
                  x = "intenções neutras"
            case 4:
                  x = "inclinamento ao mal"
            case 5:
                  x = "más intenções"

      n = random.randint(1, 2)
      match n:
            case 1:
                  y = "com ideais claros"
            case 2:
                  y = "sem ideais claros"

      n = random.randint(1, 3)
      n2 = random.randint(1, 3)
      match n:
            case 1:
                  z = "seguidor da razão"
            case 2:
                  z = "segue a balança dentre razão e emocional"
            case 3:
                  z = "seguidor da emoção"
      match n2:
            case 1:
                  k = "propaga a ordem"
            case 2:
                  k = "propaga a balança dentre ordem e caos"
            case 3:
                  k = "propaga o caos"
      return x, y, z, k

def set_karma():
      n = random.randint(0, 100)
      if n <= 5:
            x = "extremamente negativo, ele nunca teve um momento onde sentiu felicidade de verdade"
      elif n <= 25:
            x = "negativo, grande parte das vezes se decepciona na vida"
      elif n <= 75:
            x = "neutro, sua vida tem uma boa balança dentre decepções e sucesso"
      elif n <= 95:
            x = "positivo, sua vida é cheia de momentos de vitória e felicidade"
      else:
            x = "extremamente positivo, ele nunca teve um momento onde sentiu tristeza de verdade"

      return x

def relacionamentos():
      n = random.randint(1, 100)
      if n <= 25:
            x = "solteiro"
      elif n <= 50:
            x = "namorando"
      elif n <= 75:
            x = "casado"
      elif n <= 85:
            x = "divorciado"
      elif n <= 95:
            x = "divorciado e prefere não falar de seu ex-marido"
      elif n <= 98:
            x = "viúvo"
      else:
            x = "viúvo e prefere não falar de seu ex-marido"
      return x
while True:
      if seed_input == False:
            seed = round(random.uniform(-999999999, 999999999), 9)
            random.seed(seed)
      else:
            seed = seed_input
            random.seed(seed)
            seed_input = False

      nome, sobrenome = random.choice(Lists.p_nome), random.choice(Lists.s_nome)
      idade = random.randint(id_min, id_max)
      raça = random.choice(Lists.raças)
      altura = set_altura(idade)
      profissão = set_profissão()
      profissão_nível = set_profissão_level()
      salário = set_salário(profissão, profissão_nível)
      salário_mês = salário * 24
      despesas, despesas_mês, gastos, banco = set_gastos()
      
      músculos = set_status()
      gordura = set_status()
      aparência = set_status()
      aprendizado = set_status()
      acadêmico = set_status()
      consenso = set_status()
      persuasão = set_status()
      percepção = set_status()
      criatividade = set_status()

      intenções, ideais, razão, ordem = set_morais()
      karma = set_karma()

      relaciona = relacionamentos()
      raça_parceiro = random.choice(Lists.raças)
      idade_parceiro = random.randint(id_min_par, id_max_par)
      altura_parceiro = set_altura(idade_parceiro)

      # DESCRIÇÃO DE PERSONAGEM
      print("__________PERSONAGEM NOVO__________\n")

      print(f"Seu nome é {nome} {sobrenome}. Ele é um homem {raça[0]} de {altura} metros de altura e {idade} anos.\n"
            f"Ele é um {profissão[0]}, seu nível de carreira é {profissão_nível} e ele ganha {salário_mês} pence o mês ({salário}/dia).\n"
            f"Suas despesas mensais vão até {despesas_mês} pence por mês ({despesas}/dia) por conta de seu hábito de {gastos}.\n"
            f"Seu banco atualmente guarda uma quantia de {banco} pence quê vem juntando durante sua vida.\n")
      print(f"Seu número de identidade é {seed} (seed).\n")

      print("- - - - - ATRIBUTOS FÍSICOS - - - - -\n"
            f"Sua massa muscular é de categoria {músculos} ({Lists.cat_mus[músculos - 1]});\n"
            f"Gordura corporal de categoria {gordura} ({Lists.cat_gor[gordura - 1]});\n"
            f"Aparência de categoria {aparência} ({Lists.cat_apa[aparência - 1]}).\n")
      
      print("- - - - - ATRIBUTOS MENTAIS - - - - -\n"
            f"Seu aprendizado é de categoria {aprendizado} ({Lists.cat_apr[aprendizado - 1]});\n"
            f"Conhecimento acadêmico de categoria {acadêmico} ({Lists.cat_aca[acadêmico - 1]});\n"
            f"Consenso de categoria {consenso} ({Lists.cat_con[consenso - 1]}).\n")
      
      print("- - - - - ATRIBUTOS SOCIAIS - - - - -\n"
            f"Sua persuasão é de categoria {persuasão} ({Lists.cat_pes[persuasão - 1]});\n"
            f"Percepção de categoria {percepção} ({Lists.cat_pec[percepção - 1]});\n"
            f"Criatividade de categoria {criatividade} ({Lists.cat_cri[criatividade - 1]}).\n")
      
      print(f"Atualmente ele está {relaciona}. ")
      if relaciona in ("casado", "namorando"):
            print(f"Seu parceiro se chama {random.choice(Lists.p_nome)} {sobrenome}.\n"
                  f"Ele é um {raça_parceiro[0]} de {altura_parceiro} metros e tem {idade_parceiro} anos.\n")
      elif relaciona in ("divorciado", "viúvo"):
            print(f"Seu parceiro se chamava {random.choice(Lists.p_nome)} {sobrenome}.\n"
                  f"Ele era um {raça_parceiro[0]} de {altura_parceiro} metros e tinha {idade_parceiro} anos.\n")
      else:
            print("")

      print(f"Ele possui {intenções} {ideais}; {razão} e {ordem}.\n"
            f"Sueu karma é {karma}; o fluxo do karma não terá isso mudando tão cedo.")

      # INPUT DEPOIS DE GERAÇÃO
      x_input = input("\n> ")

      match x_input:
            case "":
                  continue
            case "seed":
                  try:
                        seed_input = float(input("Qual seed?\n> "))
                        time.sleep(1)
                  except ValueError:
                        print("FALHOU! Valor inválido! Reset...")
                        seed_input = False
                        time.sleep(1)
            case "set id":
                  try:
                        id_min = int(input("Min > "))
                        id_max = int(input("Max > "))
                        print(f"Min = {id_min} / Max = {id_max}")
                        time.sleep(1)
                  except ValueError:
                        print("FALHOU! Valor inválido! Reset...")
                        id_min = 18
                        id_max = 80
                        time.sleep(1)
            case "set id par":
                  try:
                        id_min_par = int(input("Min > "))
                        id_max_par = int(input("Max > "))
                        print(f"Min = {id_min_par} / Max = {id_max_par}")
                        time.sleep(1)
                  except ValueError:
                        print("FALHOU! Valor inválido! Reset...")
                        id_min_par = 18
                        id_max_par = 80
                        time.sleep(1)
