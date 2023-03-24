######## Modul este fisier.
# #import functioan din modulul respectiv.
# #Varianta 1
#
# import my_functions
# result = my_functions.my_sum(2, 7)
# print('result', result)
#
# # Varianta 2
#
# from my_functions import my_sum
# result = my_functions.my_sum(2, 7)
# print('result', result)
#
# # Varianta 3 - alias
#
# import my_functions as f
#
# # Varianta 4
#
# from my_functions import my_sum as s
#
# # Mai multe functii
#
# from my_functions import min_from_list, my_sum
#
# # Astfel putem impartii codul.

################ Pachete ###########  --- foldere

#from my_functions.integer  #### numele pachet(director).Numele modul(fisier)

## __init__.py  # un pachet va trebui sa aibe un fisier de init. Versiune mai mici de 3.2
## Sa ne obisnuim sa il trecem, versiuni mai vechi sau module care nu vor porni.


# print("__file__", __file__"")
#
# Print("__name__", __name__)
# modulele sunt pentru a face split si organizarea. un singur entry_script.

# if __name__ == "__main__":   #ma scriem
#     main()
#



