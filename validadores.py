def filtrar_vacios(val):
    if isinstance(val, (int, float)):
        return val

    if not val:
        return 'Sin info'

    return str(val)


def es_numerica(val: str):
    posibles = ('precio', 'stock')

    for posible in posibles:
        if posible in val.lower():
            return True

    return False
