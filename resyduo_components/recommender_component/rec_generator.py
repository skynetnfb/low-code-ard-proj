from recommender_component import recommender


recommender = recommender.Recommender()

"""

Generate Prediction for Tag Components recommendation Data

"""

predictions=recommender.get_all_prediction('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\surprise_tag_comp_test_2.csv')


"""

Write Top n Recommendation to File for Project Component

"""

recommender.write_recommendation_to_file(top_n_recommendations = recommender.get_top_n(predictions=predictions,n=10), file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\recommender_component\\recommendation_storage\\recommendation_top10_project_component_0_to_276_cut_5_10.json')



"""
Generate Prediction for Components Libraries recommendation Data

"""


predictions=recommender.get_all_prediction('surprise_comp_lib_test.csv')
recommender.get_precision_recall_accuracy_fprate(predictions, 0.5)