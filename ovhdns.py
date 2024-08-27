import os
import ovh
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Récupérer les valeurs des variables d'environnement
application_key = os.getenv('OVH_APPLICATION_KEY')
application_secret = os.getenv('OVH_APPLICATION_SECRET')
consumer_key = os.getenv('OVH_CONSUMER_KEY')
zone_name = os.getenv('ZONE_NAME')
subdomain = os.getenv('SUBDOMAIN')
record_id = os.getenv('RECORD_ID')
public_ip = os.getenv('PUBLIC_IP')

# Initialiser le client OVH
client = ovh.Client(
    endpoint='ovh-eu',
    application_key=application_key,
    application_secret=application_secret,
    consumer_key=consumer_key
)

# Récupérer les informations de l'enregistrement DNS existant
print(f'Fetching record for {subdomain}.{zone_name}')
result = client.get(f'/domain/zone/{zone_name}/record/{record_id}')
print(result)

# Mettre à jour l'enregistrement DNS avec la nouvelle adresse IP
print(f'Updating target record for {subdomain}.{zone_name}')
result = client.put(f'/domain/zone/{zone_name}/record/{record_id}',
    fieldType='A',
    subDomain=subdomain,
    target=public_ip,
    ttl=60
)
print(result)

# Rafraîchir la zone DNS pour appliquer les changements
print(f'Refreshing zone {zone_name}')
result = client.post(f'/domain/zone/{zone_name}/refresh')
print(result)

