conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

sub_a = conjunto_a.issubset(conjunto_b)  # True (Todos elementos de A pertencem a B?)
sub_b = conjunto_b.issubset(conjunto_a)  # False (Todos elementos de B pertencem a A?)

print(sub_a)
print(sub_b)