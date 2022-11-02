from service.utils_service import Utils

utils = Utils()

class  ComponentService:
    def getAll(self):
        json = utils.read_json_from_file(file_path = 'src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json')
        print (type(list(json.keys())))
        comp_list = list(json.keys())
        comp_list.sort()
        return comp_list 
