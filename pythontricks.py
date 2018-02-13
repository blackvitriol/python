# just adding some tricks here for referencing later
try:
    import json, sleep, tqdm
except ImportError:
    warnings.warn("Some libraries are missing from your Python..check the requirements.txt")

# create loading animations
size = 100
for _i in tqdm.tqdm(range(size)):
    time.sleep(0.5)
    size = 2+2
