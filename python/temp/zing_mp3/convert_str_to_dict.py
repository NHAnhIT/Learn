data = 'WEB=9pgu832hai9noekunuaf5l8870; nhacvnrecuser=6e27954e6f5de0f68f29a27aeafb6841; _gid=GA1.2.23921102.1711212032; lhc_per={%22vid%22:%22q9idki295lzrpbbvxz0%22}; connect=OK; _ga=GA1.1.1238046859.1711212032; _ga_G2DWK13B5J=GS1.1.1711218085.2.1.1711218094.51.0.0; _ga_WFKDSCTZLX=GS1.1.1711218085.2.1.1711220803.60.0.0'
a = data.replace("; ", "',\n'")
result = "'" + a.replace("=", "': '") + "'"
print(result)