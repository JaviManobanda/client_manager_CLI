import csv
import os
from clients.models import ClientModel


class Client_Services:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            read = csv.DictReader(f, fieldnames=ClientModel.schema())
            return list(read)

    def update_Client(self, update_client):
        clients = self.list_clients()
        update_clients = []

        for client in clients:
            if update_client.uid == client['uid']:
                update_clients.append(update_client.to_dict())
            else:
                update_clients.append(client)

        self._save_to_disk(update_clients)

    def deleted(self, delete_client):
        clients = self.list_clients()
        clients.remove(delete_client)
        self._save_to_disk(clients)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'

        with open(tmp_table_name, mode='a') as f:
            write = csv.DictWriter(f, fieldnames=ClientModel.schema())
            write.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
