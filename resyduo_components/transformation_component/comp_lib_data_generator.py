
from df_utils import DfUtils
from libraries_tranformation import LibraryTranformation
import pandas as pd


dfutils = DfUtils()
lib_tranformer = LibraryTranformation()


class comp_lib_data_generator:


    def generate_comp_lib_data():
        #project_id_list = dfutils.get_all_project_id_from_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\components_data\\project_df_page_0_to_276_cut_0_0.csv')

        #lib_tranformer.create_lib_surprise_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\code-storage\\', project_id_list, output_df='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv')

        #lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_0_0.csv')   

        lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_5_5.csv',row_cut = 5, col_cut = 5)   
        
        lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_5_10.csv',row_cut = 5, col_cut = 10)  
        
        lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_10_10.csv',row_cut = 10, col_cut = 10) 
        
        lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_2_5.csv',row_cut = 2, col_cut = 5)

        lib_tranformer.add_libraries_to_df(df1=dfutils.json_df_to_pd_df('C:\\progetti\\low-code-ard-proj\\resyduo_components\\data_miner_component\\data_miner_storage\\all_project_detail_final_201022.txt'), df2 = pd.read_csv('C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\project_data\\proj_lib_cut_0_0.csv'), output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_2_10.csv',row_cut = 2, col_cut = 10)

        #dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_0_0.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_0_0.csv')

        dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_5_5.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_5_5.csv')

        dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_5_10.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_5_10.csv')

        dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_10_10.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_10_10.csv')

        dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_2_5.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_2_5.csv')
        
        dfutils.df_to_surprise_df( input_file = 'C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\comp_lib_df_cut_2_10.csv', index_names = ["componentID", "libID"], column_name='rating', output_file='C:\\progetti\\low-code-ard-proj\\resyduo_components\\transformation_component\\transformation_storage\\libraries_data\\surprise_df_comp_lib_df_cut_2_10.csv')

    generate_comp_lib_data ()



