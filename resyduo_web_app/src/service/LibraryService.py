from service.utils_service import Utils

utils = Utils()

class  LibraryService:
    components_predictions = utils.get_predictions_without_ratings(file_path = 'src\\rec_storage\\top10_rec_surprise_comp_lib_cut_5_5.json')
    def get_libs_by_component_id_list(self, id_list):
        id_list = list(set(id_list))
        lib_predictions = LibraryService.components_predictions
        result = []
        for i in id_list:
            result.extend(lib_predictions[i])
        print('result:',result)
        return result