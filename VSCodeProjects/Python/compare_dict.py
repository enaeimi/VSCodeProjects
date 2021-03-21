second_part = True
print(""" \nSIMPLE SCRIPT COMPARAISON EXEMPLE\n """)
script_1 = {"name":"TOTO", "version":2, "steps": [
        {"step":5000,"desc":"Test WLR 3 :CRPTxx ;", "content":"blabla"},
        {"step":5010,"desc":"Test WLR 4 :CRPTxx ;", "content":"blublu"},
        {"step":5020,"desc":"Test WLR 7 :CRPTxx ;", "content":"blublu"},
        {"step":5030,"desc":"Test WLR 5 :CRPTxx ;", "content":"blublux"},
        {"step":6000,"desc":"Test WLR 90 :CRPTxx ;", "content":"blaaaublux"},
  ]
}

script_2 = {"name":"TOTO", "version":3, "steps": [
          {"step":5000,"desc":"Test WLR 3 :CRPTxx ;", "content":"blabla"},
          {"step":5020,"desc":"Test WLR 7 :CRPTxx ;", "content":"blublu"},
          {"step":5030,"desc":"Test WLR 5 :CRPTyy ;", "content":"blublux"},
          {"step":6000,"desc":"Test WLR 90 :CRPTxx ;", "content":"blaaaublux"},
          {"step":7000,"desc":"Test WLR 901 :CRPTxx ;", "content":"blaaaublux"},
  ]
}


def compare(obj_1, obj_2, key):
  if len(obj_1) == len(obj_2) and len(obj_1) == 0:
    return {}
  
  # Get keys
  reference   = obj_1 if len(obj_1) != 0 else obj_2
  keys        = list(reference[0].keys())

 # Get dict from list because to get the steps we do a database select and thus get a list
  dict_obj_1  = {y[key]:y for y in obj_1}
  dict_obj_2  = {y[key]:y for y in obj_2}

  # Sort keys

  keys_list   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))
  keys_list.sort()

  # Test every keys

  compared = []
  for current_key in keys_list:
    current_compare = {"key": current_key, "values": [], "diff": False, "key_name":key}

 

    diff = not current_key in dict_obj_1 or not current_key in dict_obj_2
    if not diff:
      diff = not all([dict_obj_1[current_key][x] == dict_obj_2[current_key][x] for x in keys])

    for el in [dict_obj_1, dict_obj_2]:
      if current_key in el:
        current_compare["values"].append({x:y for x,y in el[current_key].items() if x != key})
      else:
        current_compare["values"].append(None)

    current_compare["diff"] = diff
    compared.append(current_compare)
  return compared
 
def compare_full(obj_1, obj_2, key):
  if len(obj_1) == len(obj_2) and len(obj_1) == 0:
    return {}

  # Get keys
  reference   = obj_1 if len(obj_1) != 0 else obj_2

  keys        = list(reference[0].keys())

  # Get dict from list because to get the steps we do a database select and thus get a list
  dict_obj_1  = {y[key]:y for y in obj_1}
  dict_obj_2  = {y[key]:y for y in obj_2}

 # Sort keys
  keys_list   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))
  keys_list.sort()

  # Test every keys

  compared = []
  for current_key in keys_list:
    current_compare = {"key": current_key, "values": [], "diff": False, "key_name":key}
    diff = not current_key in dict_obj_1 or not current_key in dict_obj_2

    if not diff:
      diff = not all([dict_obj_1[current_key][x] == dict_obj_2[current_key][x] for x in keys])
 
    # full
    diffs = {x:dict_obj_1[current_key][x] == dict_obj_2[current_key][x] for x in keys}

    for el in [dict_obj_1, dict_obj_2]:
      if current_key in el:
        current_compare["values"].append({x:y for x,y in el[current_key].items() if x != key})
      else:
        current_compare["values"].append(None)

    current_compare["diff"] = diff
    current_compare["diffs"] = diffs

    compared.append(current_compare)
  return compared
 
compared = compare(script_1["steps"], script_2["steps"], key="step")
# compared = compare_full(script_1["steps"], script_2["steps"], key="step")
print(""" \nIn DEPTH COMPARAISON EXEMPLE\n """)

 
def compare_sequence(obj_1, obj_2, sequences = {}):

  key       = sequences["key"]
  deeps     = {} if "deeps" not in sequences else sequences["deeps"]
  compares  = {} if "compare" not in sequences else sequences["compare"]

  if len(obj_1) == len(obj_2) and len(obj_1) == 0:
    return {}

  # Get keys
  reference   = obj_1 if len(obj_1) != 0 else obj_2
  keys        = list(reference[0].keys())
  # Get dict from list because to get the steps we do a database select and thus get a list
  dict_obj_1  = {y[key]:y for y in obj_1}
  dict_obj_2  = {y[key]:y for y in obj_2}
  # Sort keys
  keys_list   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))

  keys_list.sort()

  # Test every keys
  compared = []
  for current_key in keys_list:
    current_compare = {"key": current_key, "values": [], "diff": False, "key_name":key}
    diff = not current_key in dict_obj_1 or not current_key in dict_obj_2
    if not diff:
      diff = not all([dict_obj_1[current_key][x] == dict_obj_2[current_key][x] for x in keys if x not in deeps])

    deep_compared = {}
    # deeps
    for deep, sub_sequences in deeps.items():
      if current_key in dict_obj_1 and current_key in dict_obj_2:
        compared_deep = compare_sequence([dict_obj_1[current_key][deep]], [dict_obj_2[current_key][deep]], sub_sequences)
        deep_compared[deep] = compared_deep
      elif current_key in dict_obj_1:
        deep_compared[deep] = [dict_obj_1, None]
      else:
        deep_compared[deep] = [None,dict_obj_2]
   
    # compares
    sequences_compared = {}
    for comp, sub_sequences in compares.items():
      if current_key in dict_obj_1 and current_key in dict_obj_2:
        compared_deep = compare_sequence(dict_obj_1[current_key][comp], dict_obj_2[current_key][comp], sub_sequences)
        sequences_compared[comp] = compared_deep
      elif current_key in dict_obj_1:
        sequences_compared[comp] = dict_obj_1
      else:
        sequences_compared[comp] = dict_obj_2

    index = 0
    for el in [dict_obj_1, dict_obj_2]:
      if current_key in el:
        values_comp = {}
        for c_key, y in el[current_key].items():
          if c_key == key: continue
          elif c_key in deep_compared:
            print("\n",current_key,deep_compared[c_key])
            values_comp[c_key] = None if len(deep_compared[c_key]) == 1 else deep_compared[c_key][index]
            if values_comp[c_key] is not None and "values" in values_comp[c_key]:
              values_comp[c_key] = values_comp[c_key]["values"]
          elif c_key in sequences_compared:
            values_comp[c_key] = sequences_compared[c_key]
          else:
            values_comp[c_key] = y

        current_compare["values"].append(values_comp)
      else:
        current_compare["values"].append(None)
      index += 1

    current_compare["diff"] = diff
    compared.append(current_compare)
  return compared

 

if second_part:
  print(""" \nOPERATION / SCRIPT COMPARAISON EXEMPLE\n """)

  script_3 = {"name":"TOTY", "version": 2, "steps":[
        {"step":5000,"desc":"Test WLR 3 :CRPTxx ;", "content":"blabla"},
        {"step":5020,"desc":"Test WLR 67 :CRPTxx ;", "content":"blublu"},
        {"step":5030,"desc":"Test WLR 5 :CRPTyy ;", "content":"blublux"},
        {"step":7000,"desc":"Test WLR 901 :CRPTxx ;", "content":"blaaaublux"}
  ]}

  route_1 = {
    "name": "toto", "operations": [
      {"operation":"10", "name": "TOTO", "script":script_1},
      {"operation":"20", "name": "TATO", "script":script_2},
      {"operation":"30", "name": "TYTO", "script":script_3}
    ]
  }

  route_2 = {
    "name": "toto", "operations": [
      {"operation":"10", "name": "TOTO", "script":script_1},
      {"operation":"30", "name": "TWTO", "script":script_2}
    ]
  }

  compared = compare_sequence(route_1["operations"], route_2["operations"], sequences =
      {"key":"operation", "deeps":{
          "script": {"key":"name", "compare":{"steps": {"key":"step"}}}
        }
      }
  )

def show(compared, level = 0):
  if type(compared) == list:
    for el in compared:
      show(el, level + 1)
  elif type(compared) == dict and "key" in compared and "diff" in compared:
    print("\n%s %s - %s: %s"%(level*"   ","X" if compared["diff"] else " ",compared["key_name"],compared["key"]))
    show(compared["values"], level + 1)
  elif type(compared) == dict:
    for k, v in compared.items():
      if type(v) != list and type(v) != dict:
        print("%s%s: %s"%(level*"   ", k, v))
      else:
        print("%s%s:"%(level*"   ", k))
        show(v, level + 1)
  else:
    print("%s%s"%(level*"   ",compared))

show(compared)