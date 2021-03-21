second_part = True

print(""" \nSIMPLE SCRIPT COMPARAISON EXEMPLE\n """)

script_1 = {"scr_id":"scr1", "version":1, "steps": [
        {"step":5000,"desc":"Test WLR 3 :CRPTxx ;", "content":"blabla"},
        {"step":5010,"desc":"Test WLR 4 :CRPTxx ;", "content":"blublu"},
        {"step":5020,"desc":"Test WLR 7 :CRPTxx ;", "content":"blublu"},
        {"step":5030,"desc":"Test WLR 5 :CRPTxx ;", "content":"blublux"},
        {"step":6000,"desc":"Test WLR 90 :CRPTxx ;", "content":"blaaaublux"},
  ]
}

script_2 = {"scr_id":"scr2", "version":2, "steps": [
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



def compare_sequence_new(dict_obj_1, dict_obj_2, deeps = {}):
    # key       = sequences["key"]
    # deeps     = {} if "deeps" not in sequences else sequences["deeps"]
    # compares  = {} if "compare" not in sequences else sequences["compare"]

    if len(dict_obj_1) == len(dict_obj_2) and len(dict_obj_1) == 0:
      return {}

    resultats = {"routes": {}}

    # Get keys
    reference   = dict_obj_1 if len(dict_obj_1) != 0 else dict_obj_2
    keys        = list(reference.keys())


    # Sort keys
    keys_list   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))
    keys_list.sort()

    # Test every keys
    for current_key in keys_list:
      if current_key not in deeps: 
        diff = not current_key in dict_obj_1 or not current_key in dict_obj_2
        # diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])
        resultats["routes"][current_key] = {"values": [dict_obj_1[current_key],dict_obj_2[current_key]], "diff" : diff}
        
    for current_key in keys_list:
      if current_key in deeps: 
        dict_object_1  = {y[deeps[current_key]['key']]:y for y in dict_obj_1[current_key]}
        dict_object_2  = {y[deeps[current_key]['key']]:y for y in dict_obj_2[current_key]}
        keys_list   = list(set(dict_object_1.keys()).union(set(dict_object_2.keys())))
        keys_list.sort()
        for el in keys_list: 

          
          
          
          resultats["routes"][current_key] ={"values":{el : ""} }



    return resultats


def compare_sequence_new2(dict_obj_1, dict_obj_2):
  
  resultats = {"routes": {}}

  keys_list_route   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))
  keys_list_route.sort()
  for current_key_route in keys_list_route:
    if current_key_route not in {"operations"}: 
      diff = not current_key_route in dict_obj_1 or not current_key_route in dict_obj_2
      # diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])
      resultats["routes"][current_key_route] = {"values": [dict_obj_1[current_key_route],dict_obj_2[current_key_route]], "diff" : diff}


  if len(dict_obj_1["operations"]) != 0:
    keys_list_operation   = list(set(dict_obj_1["operations"][0].keys()).union(set(dict_obj_2["operations"][0].keys())))
    keys_list_operation.sort()



  resultats["routes"]["operations"] = {}

  dic_op1  = {y["ope_nmb"]:y for y in dict_obj_1["operations"]}
  dic_op2  = {y["ope_nmb"]:y for y in dict_obj_2["operations"]}
  # Sort keys
  keys_list_opvalues   = list(set(dic_op1.keys()).union(set(dic_op2.keys())))
  keys_list_opvalues.sort()

  op3 =  dict_obj_1["operations"] + [ i for i in  dict_obj_2["operations"] if i not in  dict_obj_1["operations"]]

  for operation in keys_list_opvalues:
    resultats["routes"]["operations"][operation] = {}

    #ajouter diff pour route
    diff = not operation in dic_op1 or not operation in dic_op2
    
    for current_key_op in keys_list_operation:
      if current_key_op not in {"script"}: 
        # diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])
        # diff = not current_key in dict_obj_1["operations"][index] or not current_key in dict_obj_2["operations"][index]
        diff = not current_key_op in dic_op1[operation] or not current_key_op in dic_op2[operation]
        
        if current_key_op in dic_op1[operation].keys() and current_key_op in dic_op2[operation].keys():
          resultats["routes"]["operations"][operation][current_key_op] = {"values": [dic_op1[operation][current_key_op],dic_op2[operation][current_key_op]],"diff" : diff}
        elif current_key_op in dic_op1[operation].keys() and current_key_op not in dic_op2[operation].keys():
          resultats["routes"]["operations"][operation][current_key_op] = {"values": [dic_op1[operation][current_key_op],"None"],"diff" : diff}
        elif current_key_op not in dic_op1[operation].keys() and current_key_op in dic_op2[operation].keys():
          resultats["routes"]["operations"][operation][current_key_op] = {"values": ["None",dic_op2[operation][current_key_op]],"diff" : diff}
      else:

        
        #script of operation 
        if len(dic_op1[operation]["script"]) != 0 :
          keys_list_script   = list(set(dic_op1[operation]["script"].keys()).union(set(dic_op1[operation]["script"].keys())))
          keys_list_script.sort()
        resultats["routes"]["operations"][operation]["script"] = {}
        for current_key_script in keys_list_script:

          if current_key_script not in {"steps"}: 
            diff = not current_key_script in dic_op1[operation]["script"] or not current_key_script in dic_op2[operation]["script"]
            # diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])
            resultats["routes"]["operations"][operation]["script"][current_key_script] = {"values": [dic_op1[operation]["script"][current_key_script], 
              dic_op2[operation]["script"][current_key_script]], "diff" : diff}
          
          else:
            #Steps of script
            if len(dic_op1[operation]["script"]["steps"]) !=0:
              keys_list_step   = list(set(dic_op1[operation]["script"]["steps"][0].keys()).union(set(dic_op2[operation]["script"]["steps"][0].keys())))
              keys_list_step.sort()



            dic_step1  = {y["step"]:y for y in dic_op1[operation]["script"]["steps"]}
            dic_step2  = {y["step"]:y for y in dic_op2[operation]["script"]["steps"]}
            # Sort keys
            keys_list_step_values   = list(set(dic_step1.keys()).union(set(dic_step2.keys())))
            keys_list_step_values.sort()

            resultats["routes"]["operations"][operation]["script"]["steps"] = {}

            for step in keys_list_step_values:

              resultats["routes"]["operations"][operation]["script"]["steps"][step] = {}

               #ajouter diff pour route
              diff = not step in dic_step1 or not step in dic_step1

              for current_key_step in keys_list_step:
                diff = not current_key_step in  dic_step1[step] or not current_key_step in dic_step2[step]
                # diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])
                resultats["routes"]["operations"][operation]["script"]["steps"][step][current_key_step] = {"values": [dic_step1[step][current_key_step],
                  dic_step2[step][current_key_step]], "diff" : diff}

  return resultats



print(""" \nIn DEPTH COMPARAISON EXEMPLE\n """)

def compare_sequence(obj_1, obj_2, sequences = {}):
  key       = sequences["key"]
  deeps     = {} if "deeps" not in sequences else sequences["deeps"]
  compares  = {} if "compare" not in sequences else sequences["compare"]

  if len(obj_1) == len(obj_2) and len(obj_1) == 0:
    return {}

  # Get keys
  reference   = obj_1 if len(obj_1) != 0 else obj_2
  keys        = list(reference.keys())

  # Get dict from list because to get the steps we do a database select and thus get a list
  dict_obj_1  = obj_2
  dict_obj_2  = obj_1

  # Sort keys
  keys_list   = list(set(dict_obj_1.keys()).union(set(dict_obj_2.keys())))
  keys_list.sort()

  # Test every keys
  compared = []
  for current_key in keys_list:
    current_compare = {"key": current_key, "values": [], "diff": False, "key_name":key}
    # current_compare = {current_key : {"values": [], "diff": False} }

    # for simple_key in keys_list if x not in deeps:
    diff = not current_key in dict_obj_1 or not current_key in dict_obj_2
    if not diff:
      diff = not all([dict_obj_1[x] == dict_obj_2[x] for x in keys if x not in deeps])





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

  script_3 = {"scr_id":"scr3", "version": 3, "steps":[
        {"step":5000,"desc":"Test WLR 3 :CRPTxx ;", "content":"blabla"},
        {"step":5020,"desc":"Test WLR 67 :CRPTxx ;", "content":"blublu"},
        {"step":5030,"desc":"Test WLR 5 :CRPTyy ;", "content":"blublux"},
        {"step":7000,"desc":"Test WLR 901 :CRPTxx ;", "content":"blaaaublux"}
    ]
  }

  route_1 = {
    "rte_name": "routeA","rte_type": "type1","rte_desc":"xxxxxxxxxx", "operations": [
      {"facility":"CROLFA", "ope_nmb":"10", "ope_desc": "TOTO", "script":script_1},
      {"facility":"CROLFA", "ope_nmb":"20", "ope_desc": "TATO", "script":script_2},
      {"facility":"CROLFA", "ope_nmb":"30", "ope_desc": "TYTO", "script":script_3}
    ]
  }

  route_2 = {
    "rte_name": "routeB","rte_type": "type2","rte_desc":"yyyyyyyy", "operations": [
      {"facility":"CROLFA", "ope_nmb":"10", "ope_desc": "TOTO", "script":script_1},
      {"facility":"CROLFA", "ope_nmb":"30", "ope_desc": "TYTO", "script":script_2}
    ]
  }

  # compared = compare_sequence(route_1, route_2, sequences = 
  #     {"key":"rte_name", "deeps":{
  #       "operations":{"key":"ope_nmb", "compare":{"scripts": {"key":"scr_id"}}},
  #       "script":   {"key":"scr_id", "compare":{"steps": {"key":"step"}}}
  #       }
  #     }
  # )

  # compared = compare_sequence_new(route_1, route_2, deeps = 
  #     {"operations" :{"key":"ope_nmb", "scripts": {"key":"scr_id"}},
  #       "script"    :{"key":"scr_id", "steps": {"key":"step_nmb"}}
  #     }
  # )

  compared = compare_sequence_new2(route_1, route_2)

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
