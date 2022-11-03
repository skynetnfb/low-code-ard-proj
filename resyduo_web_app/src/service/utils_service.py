import json

class Utils:
    def read_json_from_file(self, file_path = 'resyduo_web_app\\src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json'):
        with open(file_path) as f:
            data = f.read()
        js = json.loads(data)
        return js

    def get_predictions_without_ratings(self, file_path = 'resyduo_web_app\\src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json'):
        js = self.read_json_from_file(file_path = file_path)
        for i in js:
            temp = []
            for j in range(0,len(js[i])):
                lib,est,true_r =js[i][j]
                temp.append(lib)
            js[i] = temp
        return js
