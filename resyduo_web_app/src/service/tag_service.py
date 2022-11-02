from service.utils_service import Utils

utils = Utils()

class  TagService:
    def getAll(self):
        json = utils.read_json_from_file(file_path = 'src\\rec_storage\\top10_rec_surprise_tag_comp_cut_5_5.json')
        print (type(list(json.keys())))
        tag_list = list(json.keys())
        tag_list.sort()
        return tag_list 

