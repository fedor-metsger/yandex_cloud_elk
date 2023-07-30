# Ansible Collection - my_own_namespace.yandex_cloud_elk

Коллекция yandex_cloud_elk содержит роль для создания файла по указанному пути с указанным содержимым


### Installation

```ignorelang
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

## Compatibility 
| OS     | Release |
|--------|---------|
| Ubuntu | 20/22   |


##Usage

```yaml
---
- name: Test module
  hosts: localhost
  collections:
    - my_own_namespace.yandex_cloud_elk

  roles:
    - my_own_role
```

## Licensing

MIT

