def get_padded_binary(value, padded_length: int, base = 10):
    formatter = '{0:0' + f'{padded_length}' + 'b}'
    value = int(value, base) if base else int(value)
    return formatter.format(value)
