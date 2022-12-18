
#* Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

# дизъюнкция    ⋁   ИЛИ
# конъюнкция    ⋀   И

def is_expression_true(x, y, z):
    return (not (x or y or z)) == ((not x) and (not y) and (not z))


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x}, {y}, {z}) -> {is_expression_true(x, y, z)}')