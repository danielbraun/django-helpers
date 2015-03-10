from geoip import geolite2


def ip_to_country_code(ip):
    match = geolite2.lookup(ip)
    return match.country if match else None
