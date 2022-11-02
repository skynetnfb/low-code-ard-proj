from recommender import Recommender


class RecGenerator():

    def generate_recommendations(self):
        recommender = Recommender()

        """

        Generate Prediction for Tag Components recommendation Data

        """

        tag_comp_predictions=recommender.get_all_prediction('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\surprise_tag_comp_cut_5_5.csv')


        """

        Write Top n Recommendation to File for Tag Component

        """

        recommender.write_recommendation_to_file(top_n_recommendations = dict(recommender.get_top_n(predictions=tag_comp_predictions,n=10)), file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\recommender_component\\recommendation_storage\\top10_rec_surprise_tag_comp_cut_5_5.json')



        """
        Generate Prediction for Components Libraries recommendation Data

        """

        comp_lib_predictions=recommender.get_all_prediction('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_5_5.csv')
        
        recommender.write_recommendation_to_file(top_n_recommendations = dict(recommender.get_top_n(predictions=comp_lib_predictions,n=10)), file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\recommender_component\\recommendation_storage\\top10_rec_surprise_comp_lib_cut_5_5.json')

rec_generator = RecGenerator()
rec_generator.generate_recommendations()