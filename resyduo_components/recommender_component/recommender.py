from matplotlib.pyplot import get
from surprise import Dataset,accuracy, NormalPredictor, Reader,SVD, KNNWithMeans,KNNBasic, KNNWithZScore
from surprise.model_selection import cross_validate, train_test_split,KFold
import heapq
import pandas as pd
from collections import defaultdict
from operator import itemgetter
import random
import math


class Recommender:
    """
    Metrics Evaluations
    """
    def precision_recall_at_k(self, predictions, k=10, threshold=0.5):
        """Return precision and recall at k metrics for each user"""

        # First map the predictions to each user.
        user_est_true = defaultdict(list)
        for  uid,_, true_r, est, _ in predictions:
            user_est_true[uid].append((est, true_r))
        #print(user_est_true)
        #display(user_est_true)

        precisions = dict()
        recalls = dict()
        for uid, user_ratings in user_est_true.items():

            # Sort user ratings by estimated value
            user_ratings.sort(key=lambda x: x[0], reverse=True)

            # Number of relevant items
            n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)
            #print('relevant: ',n_rel)

            # Number of recommended items in top k
            n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])
            #print('recommended: ',n_rec_k)

            # Number of relevant and recommended items in top k
            n_rel_and_rec_k = sum(
                ((true_r >= threshold) and (est >= threshold))
                for (est, true_r) in user_ratings[:k]
            )

            # Precision@K: Proportion of recommended items that are relevant
            # When n_rec_k is 0, Precision is undefined. We here set it to 0.

            precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 0

            # Recall@K: Proportion of relevant items that are recommended
            # When n_rel is 0, Recall is undefined. We here set it to 0.

            recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 0

        return precisions, recalls


    def get_true_positive(self, predictions, threshold):
        tp=0
        for  uid,iid, true_r, est, _ in predictions:
            if (true_r>0 and est>threshold):
                tp=tp+1
        return tp


    def get_true_negative(self, predictions, threshold):
        tn=0
        for  uid,iid, true_r, est, _ in predictions:
            if (true_r==0 and est<threshold):
                tn=tn+1
        return tn


    def get_false_negative(self, predictions, threshold):
        fn=0
        for  uid,iid, true_r, est, _ in predictions:
            if (true_r>0 and est<threshold):
                fn=fn+1
        return fn

    def get_false_positive(self, predictions, threshold):
        fp=0
        for  uid,iid, true_r, est, _ in predictions:
            if (true_r==0 and est>threshold):
                fp=fp+1
        return fp


    def get_precision_recall_accuracy_fprate(self,predictions, threshold):
        fp=self.get_false_positive(predictions, threshold)
        fn=self.get_false_negative(predictions, threshold)
        tp=self.get_true_positive(predictions, threshold)
        tn=self.get_true_negative(predictions, threshold)
        precision = tp/(tp+fp)
        recall = tp/(tp+fn)
        accuracy = (tp+tn)/(tp+tn+fp+fn)
        fprate = fp/(fp+tn)
        return precision,recall,accuracy,fprate



    def predict_and_validate(self,surprise_df='surprise df',sim_options={
                'name': 'msd',
                'user_based': True,
                'min_support':1,
                'shrinkage':0
                },threshold = 0.2,k=10,fold_split=10):
        df = pd.read_csv(surprise_df)
        #display(df)
        # A reader is still needed but only the rating_scale param is requiered.
        reader = Reader(rating_scale=(df['rating'].min(),df['rating'].max()))
        #print(df.columns)
        # The columns must correspond to user id, item id and ratings (in that order).
        data = Dataset.load_from_df(df[df.columns], reader)
        algo = KNNWithMeans(sim_options=sim_options)


        # define a cross-validation iterator
        kf = KFold(n_splits=fold_split)
        for trainset, testset in kf.split(data):
            # train and test algorithm.
            algo.fit(trainset)
            predictions = algo.test(testset)
            precisions, recalls = self.precision_recall_at_k(predictions, k=k, threshold=threshold)
            print('PRECISION:',sum(prec for prec in precisions.values()) / len(precisions))
            print('RECALL:',sum(rec for rec in recalls.values()) / len(recalls))
            # Compute and print Root Mean Squared Error
            accuracy.rmse(predictions, verbose=True)


    def get_all_prediction(self, surprise_df):
        
        df = pd.read_csv(surprise_df)
        #display(df)
        # A reader is still needed but only the rating_scale param is requiered.
        reader = Reader(rating_scale=(df['rating'].min(),df['rating'].max()))
        #print(df.columns)
        # The columns must correspond to user id, item id and ratings (in that order).
        data = Dataset.load_from_df(df[df.columns], reader)
        # sample random trainset and testset
        # test set is made of 25% of the ratings.
        trainset, testset = train_test_split(data, test_size=0.25)
        # Build an algorithm, and train it.
        algo = KNNBasic()
        algo.fit(trainset)
        predictions = algo.test(testset)
        return predictions



    def get_top_n(self, predictions, n=10):
        """Return the top-N recommendation for each user from a set of predictions.

        Args:
            predictions(list of Prediction objects): The list of predictions, as
                returned by the test method of an algorithm.
            n(int): The number of recommendation to output for each user. Default
                is 10.

        Returns:
        A dict where keys are user (raw) ids and values are lists of tuples:
            [(raw item id, rating estimation), ...] of size n.
        """

        # First map the predictions to each user.
        
        top_n = defaultdict(list)
        for  uid,iid, true_r, est, _ in predictions:
            top_n[uid].append((iid, est,true_r))

        # Then sort the predictions for each user and retrieve the k highest ones.
        for iid, user_ratings in top_n.items():
            user_ratings.sort(key=lambda x: x[1], reverse=True)
            top_n[iid] = user_ratings[:n]

        return top_n

    def get_top_n_by_id(self, predictions, n=5, id=''):
        top_n = self.get_top_n(predictions, n)
        for uid, user_ratings in top_n.items():
            if(uid== id):
                print(uid, [iid for (iid, _) in user_ratings])


    def get_success_rate(self, predictions):
        print('not implemented yet')

    """
    -------------------------
    old recommender functions
    -------------------------
    """
    def get_similar_projects (self, project, df2, cutoff = 0.1):
        df3=df2
        scores = []
        for row in range(0, len(df3)):
            sim_score= 1 - self.cosine(project,df3.loc[[row]])
            scores.append(sim_score)
        df3['scores']= scores
        for row in range(0, len(df3)):
            if (df3.loc[row,'scores'] <= cutoff or df3.loc[row,'scores'] == 0.0 or math.isnan(df3.loc[row,'scores'])):
                df3.drop(row, axis = 0 , inplace = True)
        df3.sort_values('scores', ascending=False, inplace = True)
        for i in list(df3.columns.values):
            if(df3[i].sum()==0):
                df3.drop(i, axis = 1, inplace = True)
        
        return df3

    def generate_input(self, df):
        input_list= []
        for i in range (0,len(df.columns)):
            input_list.append(random.randint(0,1))
        return input_list



    """
    -----------------------------
    end old recommender functions
    -----------------------------
    """