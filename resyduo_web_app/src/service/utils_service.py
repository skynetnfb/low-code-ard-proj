import json

class Utils:
    def read_json_from_file(self, file_path = 'resyduo_web_app\\src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json'):
        with open(file_path) as f:
            data = f.read()
        js = json.loads(data)
        return js