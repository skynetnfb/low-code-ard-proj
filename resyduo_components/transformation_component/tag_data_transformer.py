

from df_utils import DfUtils

def generate_tag_comp_data():
    dfutils = DfUtils()


    """

    01 df generation

    """
    dfutils.create_df_from_2_df_col(dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'),
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_5_5.csv',
    col_1='tags',
    col_2 ='components',
    row_cut=5,col_cut=5)

    dfutils.create_df_from_2_df_col(dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'),
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_5_10.csv',
    col_1='tags',
    col_2 ='components',
    row_cut=5,col_cut=10)

    dfutils.create_df_from_2_df_col(dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'),
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_0_0.csv',
    col_1='tags',
    col_2 ='components',
    row_cut=0,col_cut=0)


    """

    surprise df generation

    """

    dfutils.df_to_surprise_df(input_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_5_5.csv',
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\surprise_tag_comp_test_cut_5_5.csv',
    index_names = ["tagID", "componentID"],
    column_name='rating')

    dfutils.df_to_surprise_df(input_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_5_10.csv',
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\surprise_tag_comp_test_cut_5_10.csv',
    index_names = ["tagID", "componentID"],
    column_name='rating')

    dfutils.df_to_surprise_df(input_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\df_tag_comp_cut_0_0.csv',
    output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\tag_data\\surprise_tag_comp_test_cut_0_0.csv',
    index_names = ["tagID", "componentID"],
    column_name='rating')

generate_tag_comp_data()


