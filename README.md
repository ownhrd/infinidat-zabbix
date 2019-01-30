# infinidat-zabbix
## RUS
Мониторинг INFINIDAT.

* Импортировать скрипт `infinibox_zabbix.py` в `/usr/lib/zabbix/externalscripts`
* Поменять `login` и `password` в `infinibox_zabbix.py` (r/o user в INFINIBOX)
* Поменять IP-адрес от INFINIBOX в тимплейте (макро {$INFINIBOX_IP}) `Template_InfiniBox.xml`

## ENG
Monitoring INFINIDAT.

* Import script `infinibox_zabbix.py` in `/usr/lib/zabbix/externalscripts`
* Change `login` and `password` in `infinibox_zabbix.py` (r/o user in INFINIBOX)
* Change INFINIBOX IP-address in template (macro {$INFINIBOX_IP}) `Template_InfiniBox.xml`
