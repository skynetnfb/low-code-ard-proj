# importing the module
import pandas as pd
from IPython.display import display
from utils import *
from data_miner_component import file_reader
from transformation_component import df_utils


dfutils = df_utils.DfUtils()


class LybraryTranformation:


    def get_lib_list(self,path,id_list):
        lib_list=[]
        df_header=['projectID','libID','rating']
        df = pd.DataFrame(columns=df_header)
        filereader=file_reader.CodeReader()
        for i in id_list:
            libs = filereader.read_file(path,i)
            for j in libs:
                df2 = pd.DataFrame({'projectID': [i],
                                'libID': [j],
                                'rating': [1]})
                df = df.append(df2, ignore_index = True)

            lib_list = lib_list+libs
        #df.to_csv(output_df, index = False)
        #display(df)    
        lib_set = set(lib_list)
        return lib_set,df



    """
    Create Libraries Surprise DF
    """
    def create_lib_surprise_df(self, path,id_list, output_df):
        libs,temp_df = self.get_lib_list(path,id_list)
        display(len(temp_df))
        list_of_zeroes = [0]*(len(libs)*len(id_list))
        index = pd.MultiIndex.from_product([id_list, libs], names = ["userID", "itemID"])
        df = pd.DataFrame(index = index)
        df['rating'] = list_of_zeroes
        for i in range(0, len(temp_df)):
            #print (temp_df.loc[i,'userID'])
            df.loc[temp_df.loc[i,'userID'],temp_df.loc[i,'itemID']]=1
        df.to_csv(output_df)
        display(df)


    """
    add library information to 01 filled df
    """
    def add_libraries_to_df(self, df1,df2,output_file):
        df1=df1.set_index(['project_id'])  
        df2= df2[df2['rating'] != 0]
        df1['libraries']=''
        srs=df2.groupby(['userID'])['itemID'].apply(list)
        for i in srs.keys():
            df1.at[i,'libraries'] =srs [i]
        df1= df1[df1['libraries'] !='' ]
        df1 =dfutils.create_df_from_2_df_col(df1,output_file='out.csv',col_1='components', col_2 ='libraries',row_cut=0,col_cut=0)
        df1.to_csv(output_file)
        return df1