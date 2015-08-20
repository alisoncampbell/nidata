"""
A data loader utility for downloading fMRI data from OpenfMRI.org

Adapted by: Alison Campbell
"""

import os

from sklearn.datasets.base import Bunch

from ...core.datasets import HttpDataset
from ...core.fetchers import readmd5_sum_file


class Laumann2015Dataset(HttpDataset):
# class [A CLASS]([A SUPER CLASS]) 

    def fetch(self, n_subjects=1, fetch_stimuli=False,
              url=None, resume=True, force=False, verbose=1):
    		# before the fetcher, construct URLS to download
			# Openfmri dataset ID ds000031
    		
    	file_list = [('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set01.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set02.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set03.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set04.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set05.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set06.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set07.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_set08.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_retinotopy.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_ses105.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_ses106.tgz', {'uncompress':True}),
                 ('ds031','https://s3.amazonaws.com/openfmri/tarballs/ds031_pilot_set.tgz', {'uncompress':True}),
                 ]		

        files = self.fetcher.fetch(file_list, resume=resume, force=force, verbose=verbose)

        print(files)

        # return Bunch(files=files) # this will only return a list of files in the 
        return Bunch(files=files)


        # specify the files to be used
        dataset={
            'func_task001'=[
                '/Users/Alison/ds031/sub00001/ses013/functional/sub00001_ses013_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses014/functional/sub00001_ses014_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses015/functional/sub00001_ses015_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses016/functional/sub00001_ses016_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses017/functional/sub00001_ses017_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses018/functional/sub00001_ses018_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses019/functional/sub00001_ses019_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses020/functional/sub00001_ses020_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses021/functional/sub00001_ses021_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses022/functional/sub00001_ses022_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses023/functional/sub00001_ses023_task001_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/ses024/functional/sub00001_ses024_task001_run001_bold.nii.gz'
            ]
            'func_ret'=[
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run001_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run002_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run003_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run004_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run005_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run006_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run007_bold.nii.gz',
                '/Users/Alison/ds031/sub00001/sesret/functional/sub00001_sesret_task008_run008_bold.nii.gz'
            ]
            'struct_pdt2'=[
                '/Users/Alison/ds031/sub00001/ses013/anatomy/sub00001_ses013_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses014/anatomy/sub00001_ses014_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses015/anatomy/sub00001_ses015_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses016/anatomy/sub00001_ses016_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses017/anatomy/sub00001_ses017_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses018/anatomy/sub00001_ses018_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses019/anatomy/sub00001_ses019_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses020/anatomy/sub00001_ses020_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses021/anatomy/sub00001_ses021_PDT2_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses022/anatomy/sub00001_ses022_PDT2_001.nii.gz'
            ]
            'struct_t2'=[
                '/Users/Alison/ds031/sub00001/ses016/anatomy/sub00001_ses016_T2w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses018/anatomy/sub00001_ses018_T2w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses021/anatomy/sub00001_ses021_T2w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses024/anatomy/sub00001_ses024_T2w_001.nii.gz'
            ]
            'struct_t1'=[
                '/Users/Alison/ds031/sub00001/ses015/anatomy/sub00001_ses015_T1w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses018/anatomy/sub00001_ses018_T1w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses021/anatomy/sub00001_ses021_T1w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/ses024/anatomy/sub00001_ses024_T1w_001.nii.gz',
                '/Users/Alison/ds031/sub00001/sesres/anatomy/sub00001_sesret_T1w_001.nii.gz'
            ]
            'diff'=[]
        }








