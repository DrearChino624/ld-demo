from time import sleep
from ldclient import LDClient, Config
from ldclient.context import Context

SDK_KEY = "sdk-6fdeedc6-d051-46d6-a560-121efb306b8f"  # tu SDK Dev
FLAG_KEY = "demo-python-2"                            # flag que ya funciona

client = LDClient(Config(SDK_KEY))
context = Context.create("k8s-app")

print("Aplicación iniciada dentro de Kubernetes...")

while True:
    detail = client.variation_detail(FLAG_KEY, context, False)
    print(f"[K8s App] Flag value: {detail.value} - Reason: {detail.reason}")
    sleep(5)
