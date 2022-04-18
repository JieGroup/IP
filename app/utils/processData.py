import sys
import pdb
import sys
import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
# import rpy2.robjects.packages as rpackages
# import rpy2.robjects as robjects
# import rpy2.robjects.numpy2ri

# from rpy2.robjects.vectors import StrVector
from datetime import datetime, timedelta

from app.mongoDB import select_mongoDB_operator
from app import pyMongo

def print_func(msg):
    print(f'\n====== {msg} =======\n')


def countDB():
    response = {}
    print_func('summary stat')
    # print('total {} Q&As'.format(db.session.query(QandA).count()))
    mongoDB_operator = select_mongoDB_operator('SurveyAnswer')

    total_surveys_num = mongoDB_operator.get_all_documents_count()
    response['total surveys'] = total_surveys_num
    print('total {} surveys'.format(total_surveys_num))
    
    static_surveys_num = mongoDB_operator.get_all_documents_count(way='static')
    response['total static surveys'] = static_surveys_num
    print('total {} static surveys'.format(static_surveys_num))

    # print_func('missing ID')
    # print('total {} surveys without MturkID'.format(db.session.query(QandA).filter_by(topic='age', rounds=1, mturkID=None).count()))

    # for k in range(1,6):
    #     print('among them, {} is from round {}'.format(db.session.query(QandA).filter_by(topic='age', rounds=1, mturkID=None, surveyround=k).count(), k))
    
    return response


# def voterDescribe():

#     printJ('voter level: participation')

#     print('total {} voters with MturkID'.format(db.session.query(Voter).count()-1))
#     # for u in db.session.query(Voter):
#     #     if u.name is None:
#     #         continue
#     #     R = []
#     #     for q in db.session.query(QandA).filter_by(voter=u, topic='age', rounds=1):
#     #         R.append(q.surveyround)
#     #     print(f"voter {u.name} has participated rounds {R}")

#     printJ('voter level: uncertainty comparison between static and dynamic')
#     # TODO: need to define an uncertainty measure for dynamic answer

#     return


# def rmvTestData():
#     printJ('delete out-date-range data')
#     for q in db.session.query(QandA).filter_by(topic='MTurk'):
#         if q.answer.startswith('TEST') or q.answer.startswith('test'):
#             print(q.answer, q.starttime, q.digits)
#             print('removing test data with digit '+q.digits)
#             for q in db.session.query(QandA).filter_by(digits=q.digits):
#                 db.session.delete(q)
#                 db.session.commit()
#     printJ('deleted')

#     return


def build_UserProfile():
    '''
        use the built Q&A database (with completed mturkID) to fill the user profile (see model.py)
        so that we can easily perform user-level queries

        the following code is slow, can be refactored

        this creates 604 users, 603 of which are identifiable and the last one represents mturkID=None
    '''

    # for q in db.session.query(QandA):
    #     u = db.session.query(Voter).filter_by(name=q.mturkID)
    #     if u.count() == 0:
    #         user = Voter(
    #             name = q.mturkID
    #         )
    #     else:
    #         user = u.first()
    #     q.voter = user

    # db.session.commit()

    mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
    survey_answer_all_documents = mongoDB_operator.get_all_documents()
    print(f'survey_answer_all_documents: {survey_answer_all_documents}')
    for survey_answer_document in survey_answer_all_documents:

        mturk_id = survey_answer_document['mturk_id']
        print(f'mturk_id in build_UserProfile: {mturk_id}')
        mongoDB_operator = select_mongoDB_operator('Voter')
        voter_document = mongoDB_operator.search_document(mturk_id=mturk_id)

        if voter_document == None:
            mongoDB_operator.create_document(mturk_id=mturk_id)
        else:
            survey_template_id = survey_answer_document['survey_template_id']
            survey_answer_id = survey_answer_document['survey_answer_id']
            mongoDB_operator.update_document(mturk_id=mturk_id, survey_template_id=survey_template_id,
                                             survey_answer_id=survey_answer_id)

    return


# def fill_rounds_to_db():
#     '''
#         based on the T1-T5 excel info, confirm the T1-T5 collection time
#         then use the distribution time to fill 1-5 into the db variable "surveyround"

#         separate T1-T5 by 
#         T1: datetime(2021, 3, 9, 0, 0, 0) > q.starttime
#         T2: datetime(2021, 3, 16, 0, 0, 0) > q.starttime
#         T3: datetime(2021, 3, 23, 0, 0, 0) > q.starttime
#         T4: datetime(2021, 3, 31, 14, 55, 0) > q.starttime # the last few that do not match the time range may be problematic
#         T5: remaining
#     '''
#     for q in db.session.query(QandA):
#         current = q.surveyround
#         if datetime(2021, 3, 9, 0, 0, 0) > q.starttime:
#             q.surveyround = 1
#         elif datetime(2021, 3, 16, 0, 0, 0) > q.starttime:
#             q.surveyround = 2
#         elif datetime(2021, 3, 23, 0, 0, 0) > q.starttime:
#             q.surveyround = 3
#         elif datetime(2021, 3, 31, 14, 55, 0) > q.starttime:
#             q.surveyround = 4
#         else:
#             q.surveyround = 5
#         if current != None and q.surveyround != current:
#             sys.exit(f'mismatched surveyround with q.digits={q.digits}')

#     db.session.commit()

#     return


# def fill_mturkID_to_db():
#     '''
#         use the excel organized by Qin that maps mturkID and 8-digit (transfered from local)
#         to fill variable "mturkID" (see models.py)
#         this will serve as the "voter id" that was fogotten in earlier design
#     '''
#     for r in range(2,6):

#         # for T2-T5
#         printJ(f'Processing excel file for T{r}')

#         df = pd.read_csv(DIR + f"T{r}_dynamic.csv", header='infer')
#         for i in range(df.shape[0]):
#             # for each row, find the Q&A item by matching digit, and insert the mturkID

#             # print(df.loc[i, 'Actual Completion Code'], type(df.loc[i, 'Actual Completion Code']))
#             digit = str(int(df.loc[i, 'Actual Completion Code'])).zfill(8)
#             # print(i, digit)
#             # if i == 8:
#             #     print('debug')
#             #     # pdb.set_trace()
#             mturkID = df.loc[i, 'AmazonIdentifier']
#             for q in db.session.query(QandA).filter_by(digits=digit):
#                 if q.way != 'dynamic':
#                     print(f'file {r} at row {i}')
#                     sys.exit('the survey type from original db does not match excel!')
#                 q.mturkID = mturkID
#                 q.surveyround = r

#         df = pd.read_csv(DIR + f"T{r}_static.csv", header='infer')
#         for i in range(df.shape[0]):
#             # for each row, find the Q&A item by matching digit, and insert the mturkID

#             digit = str(df.loc[i, 'Actual Completion Code']).zfill(8)
#             mturkID = df.loc[i, 'AmazonIdentifier']
#             for q in db.session.query(QandA).filter_by(digits=digit):
#                 if q.way != 'static':
#                     print(f'file {r} at row {i}')
#                     sys.exit('the survey type from original db does not match excel!')
#                 q.mturkID = mturkID
#                 q.surveyround = r

#     # for T1
#     df = pd.read_csv(DIR + "T1_matched_id_type (n=603).csv", header='infer')
#     # print(df.head())
#     for i in range(df.shape[0]):
#         digit = str(df.loc[i, 't1_survey_code']).zfill(8)
#         mturkID = df.loc[i, 'worker_id']
#         for q in db.session.query(QandA).filter_by(digits=digit):
#             q.mturkID = mturkID
#             q.surveyround = 1

#     db.session.commit()
    
#     return


def export_data():
    '''
        organize into structured excel data, for Pandas based downstream analysis
        each row contains (mturkID, topic, param, answer, rounds, duration=starttime-endtime, surveyround)
        for each way (static or dynamic), we store an excel file named "way"
    '''
    # outdated = datetime(2021, 2, 26, 0, 0, 0) > q.starttime
    
    return


# def map_digit_type_for_T1():
#     '''
#         for T1 data, map the digit and type, so that we can distribute the corresponding
#         type to T2-T5 on Amazon Mturk
#     '''
#     digits, types, dates = [], [], []
#     for q in db.session.query(QandA).filter_by(topic='age', rounds=1):
#             # print(q.starttime, q.digits, q.way, q.topic, q.param, q.answer, q.rounds)
#             # print(q.mturkID)
#             digits.append(q.digits)
#             types.append(q.way)
#             dates.append(q.starttime)

#     file = 'digit_type_mapping.xlsx'
#     with pd.ExcelWriter(file) as writer:  
#         df = pd.DataFrame({
#           'digit': digits, 
#           'type': types,
#           'starttime': dates
#           })
#         df.to_excel(writer, sheet_name=f'Round 1')

#     return


def clear_db():
    '''
        Dangerous action: to remove all the queries in the database
    '''
    # for q in db.session.query(QandA).all():
    #     db.session.delete(q)
    #     db.session.commit()

    # for q in db.session.query(Voter).all():
    #     db.session.delete(q)
    #     db.session.commit()

    collection_list = pyMongo.db.list_collection_names()
    for collection_name in collection_list:
        pyMongo.db.drop_collection(collection_name)

    return 'done'


def sub_extra_interval(voter_answer_of_topic, num_range, depth="full"):
    '''A subroutine that extracts a list of intervals from user answers
        Input: 
            u_ans: Query return from b.session.query(QandA)
            num_range: numerical range, e.g., num_salary = [0, 150]
            depth: full (up to three answers) or shallow (only the first answer)
        Output:
            interval: [low, high] representing the narrowed-down range from multiple rounds
    '''
    # n_rounds = voter_answer.count()
    n_rounds = len(voter_answer_of_topic)
    if n_rounds == 0:
        return False, None, None

    low, high = num_range[0], num_range[1]

    # if the user-answer pair exists (i.e., a user is assigned a particular survey type in our context)
    K = n_rounds+1 if depth == "full" else 2

    for k in range(1, K):
        # param = voter_answer.filter_by(rounds=k).first().param
        # ans = voter_answer.filter_by(rounds=k).first().answer

        rounds_key = f'rounds_{k}'
        param = voter_answer_of_topic[rounds_key]['answer_type']
        ans = voter_answer_of_topic[rounds_key]['answer']
        
        if ans == "left":
            high = param
        elif ans == "right":
            low = param
        else:
            pass
    return True, low, high

def process_dynamic_data_to_plot(topic, num_range, surveyround=None):
    '''
    Handle surveyround in later version
    '''
    # for u in db.session.query(Voter).filter_by().all():
    #     if u.name is None:
    #         continue
    #     u_ans = db.session.query(QandA).filter_by(
    #         surveyround=surveyround,
    #         topic=topic,
    #         way="dynamic",
    #         mturkID=u.name
    #         )
        
    #     # print(f'User {u.name} participated {u_ans.count()} rounds')
    #     f, l, h = sub_extra_interval(u_ans, num_range, depth = "shallow")
    #     if f: intervals_shallow.append([l, h])
        
    #     f, l, h = sub_extra_interval(u_ans, num_range, depth = "full")
    #     if f: intervals_full.append([l, h])

    intervals_shallow = [] # round 1
    intervals_full = [] # round X
    mongoDB_operator = select_mongoDB_operator('Voter')
    voter_all_documents = mongoDB_operator.get_all_documents()
    for voter_document in voter_all_documents:
        mturk_id = voter_document['mturk_id']
        if mturk_id == None:
            continue
        
        mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
        survey_answer_documents = mongoDB_operator.get_all_documents(mturk_id=mturk_id, way='dynamic')
        print('dynamic1')
        for survey_answer_document in survey_answer_documents:
            print(f'dynamic survey_answer_document: {survey_answer_document}')
            if 'survey_answers' in survey_answer_document and topic in survey_answer_document['survey_answers']:
                voter_answer_of_topic = survey_answer_document['survey_answers'][topic]
                # print(f'User {u.name} participated {u_ans.count()} rounds')
                print('dynamic2')
                f, l, h = sub_extra_interval(voter_answer_of_topic, num_range, depth = "shallow")
                if f: intervals_shallow.append([l, h])
                
                f, l, h = sub_extra_interval(voter_answer_of_topic, num_range, depth = "full")
                if f: intervals_full.append([l, h])
    
    return intervals_shallow, intervals_full

def process_static_data_to_plot(topic, num_range, surveyround=None):
    '''
    Handle surveyround in later version
    '''
    # plot static data
    # v = [] # empirical obs
    # for u in db.session.query(Voter).filter_by().all():
    #     if u.name is None:
    #         continue
    #     u_ans = db.session.query(QandA).filter_by(
    #         surveyround=surveyround,
    #         topic=topic,
    #         way="static",
    #         mturkID=u.name
    #         )
    #     if u_ans.count() > 0: # if this user answered a static survey
    #         a = int(u_ans.first().answer)
    #         if a >= num_range[0] and a <= num_range[1]:  # to remove infeasible answer
    #         # note that we did not remove the bad answer in the cleaning func, to eval the quality later
    #             v.append(a)

    v = [] # empirical obs
    mongoDB_operator = select_mongoDB_operator('Voter')    
    for voter_document in mongoDB_operator.get_all_documents():
        mturk_id = voter_document['mturk_id']
        if mturk_id == None:
            continue
        
        mongoDB_operator = select_mongoDB_operator('SurveyAnswer')
        survey_answer_documents = mongoDB_operator.get_all_documents(mturk_id=mturk_id, way='static')
        print('static1')
        if len(list(survey_answer_documents)) > 0:
            print('static2')
            survey_answer_document = survey_answer_documents[0]
            if 'survey_answers' in survey_answer_document and topic in survey_answer_document['survey_answers']:
                voter_answer = survey_answer_document['survey_answers'][topic]
                if voter_answer >= num_range[0] and voter_answer <= num_range[1]:  # to remove infeasible answer
                # note that we did not remove the bad answer in the cleaning func, to eval the quality later
                    v.append(voter_answer)

    return v

def analyze_numeric(topic, num_range, surveyround=None):
    '''surveyround means T1-T5. only consider T1 for current paper revision'''

    # r = robjects.r
    # utils = rpackages.importr('utils')
    # utils.chooseCRANmirror(ind=1) # select the first mirror in the list

    # activate python numpy -> R matrix (optional)
    
    # rpy2.robjects.numpy2ri.activate()

    # install common packages
    # packnames = () #('ggplot2', 'BiocManager')
    # names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
    # if len(names_to_install) > 0:
    #     utils.install_packages(StrVector(names_to_install))
    # install Icens package
    # r('BiocManager::install("Icens")')

    # load db data

    mongoDB_operator = select_mongoDB_operator('Voter')
    n_user = mongoDB_operator.get_all_documents_count()
    # n_user = db.session.query(Voter).count()
    print(f'Recall that there are {n_user} users')
    
    intervals_shallow, intervals_full = process_dynamic_data_to_plot(topic=topic, num_range=num_range)
    print(f'intervals_shallow: ', intervals_shallow)
    print(f'intervals_full: ', intervals_full)

    v = process_static_data_to_plot(topic=topic, num_range=num_range)
    print(f'There are {len(v)} users who answered this static question')
    v = np.array(v)

    response = {
        'intervals_shallow': intervals_shallow,
        'itervals_full': intervals_full,
    }
    return response
    n = len(intervals_shallow)
    print(f'There are {n} users who answered this dynamic question')

    intervals_shallow_r = r.matrix(np.array(intervals_shallow), nrow=n, ncol=2) # this generates Python var
    intervals_full_r = r.matrix(np.array(intervals_full), nrow=n, ncol=2)

    # Pythonian codes to run R (wrapping all R-content in R functions)
    r['source']('NPMLE-source.R')
    grid = np.arange(num_range[0], num_range[1]+1, 1)
    x = robjects.FloatVector(list(grid))

    res_shallow = r['NPMLE'](intervals_shallow_r, x)
    cdf_round1 = res_shallow.rx2("cdf")
    res_full = r['NPMLE'](intervals_full_r, x)
    cdf_roundx = res_full.rx2("cdf")
    # print(res_shallow.names)
    
    

    # prepare statistics for the figure 
    # static data treated as raw data in another random experiment
    grid_raw = np.sort(v)
    cdf_raw = 1.*np.arange(len(v))/(len(v)-1)

    # estimated NPMLE mean
    round1_mean = np.sum(grid * np.diff(np.concatenate((np.array([0]), cdf_round1))))
    roundx_mean = np.sum(grid * np.diff(np.concatenate((np.array([0]), cdf_roundx))))
    raw_mean = np.sum(grid_raw * np.diff(np.concatenate((np.array([0]), cdf_raw))))
    # print('means of round 1, x, and raw: ', round1_mean, roundx_mean, raw_mean)
    alpha = 0.5
    v_noise = v + np.random.laplace(scale=(num_range[1]-num_range[0])/alpha, size=v.shape[0])
    DP_mean = v_noise.mean()

    return 5
    # NOTE: experimentally found that the DP variance is too large
    print(f'MAE for IP-x and DP on {topic}:', np.abs(roundx_mean-raw_mean), np.abs(DP_mean-raw_mean))

    # for QQ plot and L2 distance: expand cdf_round1 and cdf_roundx to match cdf_raw
    cdf_round1_match, cdf_roundx_match = np.zeros(cdf_raw.shape), np.zeros(cdf_raw.shape)
    for i in range(cdf_raw.shape[0]):
        idx = np.where(grid >= grid_raw[i])[0][0]
        cdf_round1_match[i] = cdf_round1[idx]
        cdf_roundx_match[i] = cdf_roundx[idx]

    # calculate L2 (Harald) distance between CDF https://en.wikipedia.org/wiki/Energy_distance
    # assuming that the grid is on integers
    L2_round1, L2_roundx = 0, 0
    for i in range(grid_raw.shape[0]):
        if i == 0:
            L2_round1 += (grid_raw[i] - num_range[0]) * (cdf_round1_match[i] - cdf_raw[i]) ** 2
            L2_roundx += (grid_raw[i] - num_range[0]) * (cdf_roundx_match[i] - cdf_raw[i]) ** 2
        else:
            L2_round1 += (grid_raw[i] - grid_raw[i-1]) * (cdf_round1_match[i] - cdf_raw[i]) ** 2
            L2_roundx += (grid_raw[i] - grid_raw[i-1]) * (cdf_roundx_match[i] - cdf_raw[i]) ** 2
    print('L2_round1, L2_roundx: ', L2_round1, L2_roundx)

    # calculate coverage for roundx
    n = v.shape[0]
    cov_shallow, cov_full = np.zeros(len(intervals_shallow)), np.zeros(len(intervals_full))
    for i in range(len(intervals_shallow)):
        cov_shallow[i] = v[np.logical_and(v>intervals_shallow[i][0], v<=intervals_shallow[i][1])].shape[0] / n
    for i in range(len(intervals_full)):
        cov_full[i] = v[np.logical_and(v>intervals_full[i][0], v<=intervals_full[i][1])].shape[0] / n
    print('cov_shallow, cov_deep: ', cov_shallow.mean(), cov_full.mean())

    plotting = True
    if plotting:

        # 25%, 50%, 75% quantizers of the range and the raw CDF values
        # col 0 : y value, 1 : hat{F}_round1, 2 : hat{F}_roundx, 3 : hat{F}_raw
        discrete = np.zeros((3, 4))
        for i in range(3):
            discrete[i,0] = num_range[0] + (num_range[1]-num_range[0])*0.25*(i+1)
            idx = np.where(grid_raw <= discrete[i,0])[0][-1]
            discrete[i,1] = cdf_round1_match[idx]
            discrete[i,2] = cdf_roundx_match[idx]
            discrete[i,3] = cdf_raw[idx]

        # # draw traditional CDF figure
        f = plt.figure(figsize=(5, 6))
        # plt.subplot(1,2,1)
        plt.ylabel('Distribution function', fontsize=14)
        plt.xlabel(r'$y$')
        plt.plot(grid, cdf_round1, 'b-.', label="Round 1")
        plt.plot(grid, cdf_roundx, 'r-', label="Round X")
        plt.plot(grid_raw, cdf_raw, 'k-', label="Point data")
        plt.ylim([0, 1])
        for i in range(3): # show the category frequency
            plt.plot(discrete[i,0], discrete[i,3], 'k*', markersize=6)
            plt.plot([discrete[i,0],discrete[i,0]], [0,discrete[i,3]], 'k:')

        plt.legend(fontsize=14, loc="upper left")
        plt.tight_layout()
        # plt.show()
        plt.savefig(f"/Users/zhanzhan/Documents/survyQin/testQQ_{surveyround}_{topic}.pdf", bbox_inches='tight')
    print('\n')

