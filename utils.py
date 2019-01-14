def read_df(filename, index_col = 'date'):
    import feather
    return feather.read_dataframe(filename).set_index(index_col)   