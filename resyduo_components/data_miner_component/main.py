from data_miner_component.data_miner import DataMiner
from transformation_component.comp_lib_data_generator import comp_lib_data_generator 
from transformation_component.tag_data_transformer import generate_tag_comp_data 
from recommender_component.rec_generator import Recommender


def main():

    data_miner = DataMiner()
    recommender = Recommender()



    data_miner.generate_project_data()
    comp_lib_data_generator()
    generate_tag_comp_data()




if __name__ == "__main__":
    main()