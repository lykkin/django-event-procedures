def extract_context_var(var, kwargs):
    extract_var = kwargs
    for key in var.split('.'):
        try:
            if hasattr(extract_var, '__getitem__'):
                extract_var = extract_var[key]
            else:
                extract_var = getattr(extract_var, key)
        except LookupError:
            raise LookupError(key + ' could not be found in ' + str(extract_var)
                                + '. Source address: ' + var)
