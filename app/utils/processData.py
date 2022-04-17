import sys
import pdb
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri

from rpy2.robjects.vectors import StrVector
from datetime import datetime, timedelta

from app.mongoDB import select_mongoDB

def sub_extra_interval(u_ans, num_range, depth="full"):
    '''A subroutine that extracts a list of intervals from user answers
        Input: 
            u_ans: Query return from b.session.query(QandA)
            num_range: numerical range, e.g., num_salary = [0, 150]
            depth: full (up to three answers) or shallow (only the first answer)
        Output:
            interval: [low, high] representing the narrowed-down range from multiple rounds
    '''
    n_rounds = u_ans.count()
    if n_rounds == 0:
        return False, None, None

    low, high = num_range[0], num_range[1]

    # if the user-answer pair exists (i.e., a user is assigned a particular survey type in our context)
    K = n_rounds+1 if depth == "full" else 2

    for k in range(1, K):
        param = u_ans.filter_by(rounds=k).first().param
        ans = u_ans.filter_by(rounds=k).first().answer
        if ans == "left":
            high = param
        elif ans == "right":
            low = param
        else:
            pass
    return True, low, high


def analyze_numeric(surveyround, topic, num_range):
    '''surveyround means T1-T5. only consider T1 for current paper revision'''

    r = robjects.r
    utils = rpackages.importr('utils')
    utils.chooseCRANmirror(ind=1) # select the first mirror in the list

    # activate python numpy -> R matrix (optional)
    
    rpy2.robjects.numpy2ri.activate()

    # install common packages
    packnames = () #('ggplot2', 'BiocManager')
    names_to_install = [x for x in packnames if not rpackages.isinstalled(x)]
    if len(names_to_install) > 0:
        utils.install_packages(StrVector(names_to_install))
    # install Icens package
    # r('BiocManager::install("Icens")')

    # load db data

    mongoDB_operator = select_mongoDB('Voter')
    n_user = mongoDB_operator.document_count()
    # n_user = db.session.query(Voter).count()
    intervals_shallow = [] # round 1
    intervals_full = [] # round X
    print(f'Recall that there are {n_user} users')

    for voter_document in mongoDB_operator.all_documents():
        # if voter_document.
        pass


    for u in db.session.query(Voter).filter_by().all():
        if u.name is None:
            continue
        u_ans = db.session.query(QandA).filter_by(
            surveyround=surveyround,
            topic=topic,
            way="dynamic",
            mturkID=u.name
            )
        
        # print(f'User {u.name} participated {u_ans.count()} rounds')
        f, l, h = sub_extra_interval(u_ans, num_range, depth = "shallow")
        if f: intervals_shallow.append([l, h])
        
        f, l, h = sub_extra_interval(u_ans, num_range, depth = "full")
        if f: intervals_full.append([l, h])

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

    # plot static data
    v = [] # empirical obs
    for u in db.session.query(Voter).filter_by().all():
        if u.name is None:
            continue
        u_ans = db.session.query(QandA).filter_by(
            surveyround=surveyround,
            topic=topic,
            way="static",
            mturkID=u.name
            )
        if u_ans.count() > 0: # if this user answered a static survey
            a = int(u_ans.first().answer)
            if a >= num_range[0] and a <= num_range[1]:  # to remove infeasible answer
            # note that we did not remove the bad answer in the cleaning func, to eval the quality later
                v.append(a)
    print(f'There are {len(v)} users who answered this static question')
    v = np.array(v)

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

