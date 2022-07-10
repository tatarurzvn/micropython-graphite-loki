def loki_log(message):
	import mrequests
	import config
	import ujson
	import utime
	import gc

	gc.enable()
	gc.collect()
	data = {"streams": [{"stream": {"esp_id":"1"}, "values": [[str(utime.time() + 946684800) + "000000000", message]]}]}
	res = mrequests.post(
		config.LOKI_BACKEND,
		auth=(config.LOKI_USERNAME, config.LOKI_API_KEY),
		headers={'content-type': 'Application/JSON'},
		data=ujson.dumps(data),
		)
	gc.collect()

class Metric:
	def __init__(self, name, val):
		self.name = name
		self.val = val

def send_to_graphite(metrics_list):
	import mrequests
	import config
	import ujson
	import utime
	import gc

	gc.enable()
	gc.collect()
	data = [
		{"name": m.name, "interval": 10, "value": m.val, "mtype": "gauge", "time": utime.time() + 946684800}
		for m in metrics_list
	]
	res = mrequests.post(
		config.GRAPHITE_BACKEND,
		headers={'content-type': 'Application/JSON', "Authorization": "Bearer " + config.GRAPHITE_USERNAME + ":" + config.GRAPHITE_API_KEY},
		data=ujson.dumps(data),
	)
	gc.collect()

def free(full=False):
	import gc

	F = gc.mem_free()
	A = gc.mem_alloc()
	T = F+A
	P = '{0:.2f}%'.format(F/T*100)
	if not full: 
		send_to_graphite([Metric('memtotal', T), Metric('memfree', F)])
		return P
	else : 
		return ('Total:{0} Free:{1} ({2})'.format(T,F,P))
