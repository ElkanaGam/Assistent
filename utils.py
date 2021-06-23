from pathlib import Path


class simpleDataStructure:

    def __init__(self) -> None:
        self.data = {}

    def put(self, key, value):
        self.d[key] = value

    def extarct (self, key):
        try:
            return_value = self.data[key]
            return return_value
        except KeyError as e:
            return None
        except Exception as e:
            raise e
            





def create_data_from_file(file_path, data):
    file_name = file_path.stem
    # data = []
    for c in file_name:
        data.put(c,  file_path)


    
def create_data_base(path_to_dir, data):
    files_to_process = [f for f in Path(path_to_dir).iterdir() if f.is_file()]
    for f in files_to_process:
        create_data_from_file(f, data)




