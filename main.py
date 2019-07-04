import pprint
with open('Cook.txt', 'r', encoding='utf8') as f:
  dicts = dict()
  for line in f:
      if line.strip() == '':
          name = f.readline().strip()
          dicts.setdefault(name, list())
      else:
          counts = line.strip()
          count = 0
          while count < int(counts):
              stri = f.readline().strip().split('|')
              info_cook = {"ingridient_name": stri[0], "quantity": stri[1], "measure": stri[2]}
              dicts[name].append(info_cook)
              count += 1
print(dicts)



def get_shop_list_by_dishes(dishes, person_count):
  cook_dict = dict()
  for cook_name in dishes:
    if cook_name in dicts.keys():
        for items_list in dicts.keys():
            if cook_name == items_list:
                for item in dicts[items_list]:
                    for key, value in item.items():
                            if key == 'quantity':
                                values = int(value)
                                item[key] = values * 5         
                    for key, value in item.items():
                      if key == 'ingridient_name':
                        name = value
                        cook_dict.setdefault(value, dict())
                      elif key == 'measure':
                        cook_dict[name].setdefault(key,value.strip())
                      elif key == 'quantity':
                        cook_dict[name].setdefault(key,value)
    else:
      return('Нет блюда: ' + cook_name)
  return cook_dict
  

def main():
  dis = list()
  count_cook = int(input('\n\n Введите количество вводимых блюд: \n'))
  person = int(input('Введите количество персон: '))
  for i in range (count_cook):
      x=input("Введите наименования блюда: \n")
      dis.insert(i,x)
      i+=1
  pprint.pprint(get_shop_list_by_dishes(dis, person))

print(main())
