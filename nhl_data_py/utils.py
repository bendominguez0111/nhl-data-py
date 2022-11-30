from nhl_data_py.stats import BASE_URL, VERSION

build_endpoint = lambda endpoint, base=[BASE_URL, VERSION]: '/'.join([*base, endpoint])
