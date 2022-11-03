from service.utils_service import Utils

utils = Utils()

class  ComponentService:
    components_predictions = utils.get_predictions_without_ratings(file_path = 'src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json')

    def getAll(self):
        json = ComponentService.components_predictions
        print (type(list(json.keys())))
        comp_list = list(json.keys())
        comp_list.sort()
        return comp_list

    def get_component_by_id(self, id):
        components= ComponentService.components_predictions
        return components[id]
    
    def get_libs_by_component_id_list(self, id_list):
        lib_predictions = ComponentService.components_predictions
        result = []
        for i in id_list:
            result.append(lib_predictions[i])
        return result





