import yaml


def to_yaml(data):
    return yaml.safe_dump(data, default_flow_style=False,
                          encoding='utf-8', allow_unicode=True),
