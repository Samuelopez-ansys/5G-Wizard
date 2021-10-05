# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 14:47:02 2021

@author: asligar
"""

from core_pd import PD
from core_cdf import CDF
import Lib.Utillities as utils
#from AEDTLib.HFSS import HFSS
#from AEDTLib.Desktop import Desktop
import pyaedt 
from pyaedt import Hfss
from pyaedt import Desktop
from Validation import Validate_Reference_Data


def run_pd(aedtapp):
    multi_run_enabled = False
    wizard = PD(aedtapp,output_path = './output/')
    
    if multi_run_enabled:
        wizard.multirun_state = True
        wizard.multi_setup_file_path = './example_projects/Multi_Setup_Run_PD.csv'

    else:
        wizard.multirun_state = False
        selected_project = '5G_28GHz_AntennaModule'
        selected_design = '4x1_array2'
        selected_setup = "Setup1:LastAdaptive"
        selected_freq = 28e9
        codebook_path = './example_projects/CodebookExample_Hpol_Renormalize.csv'
        #codebook_path = './example_projects/Codebook_for_ANSYS_Example1_Pin_6W_HVpol.csv'

        selected_eval_surf = '20mm_Surface'
        #selected_eval_surf = '25mm_Surface'
        selected_area = '1cm^2' #area in cm^2 as a string
        selected_pd_type = 'PD_n_plus'
        renormalize = True
        renorm_values= [1,.5,1,.5,.1]
    
        wizard.freq = selected_freq
        wizard.project_name = selected_project
        wizard.design_name = selected_design
        wizard.surface_name= selected_eval_surf
        wizard.averaging_area = utils.convert_units(selected_area,newUnits= 'meter^2') #area should be in meters^2
        wizard.setup_name = selected_setup
        wizard.path_to_codebook = codebook_path
        wizard.pd_type = selected_pd_type
        wizard.renormalize = renormalize
        wizard.renorm_values = renorm_values
    wizard.run_pd()

def run_cdf(aedtapp):
    multi_run_enabled = False
    wizard = CDF(aedtapp,output_path = './output/')
    
    if multi_run_enabled:
        wizard.multirun_state = True
        wizard.multi_setup_file_path = './example_projects/Multi_Setup_Run_CDF.csv'

    else:
        wizard.multirun_state = False
        selected_project = '5G_28GHz_AntennaModule'
        selected_design = '4x1_array2'
        selected_setup = "Setup1:LastAdaptive"
        selected_freq = 28e9
        renormalize = True
        renormalize_dB = False
        renorm_value= 10
        
        codebook_path = './example_projects/CodebookExample_Vpol.csv'

        cs_name = 'Global'
        
    
        wizard.freq = selected_freq
        wizard.project_name = selected_project
        wizard.design_name = selected_design

        wizard.setup_name = selected_setup
        wizard.path_to_codebook = codebook_path
        wizard.cs_name = cs_name
        wizard.renormalize = renormalize
        wizard. renormalize_dB = renormalize_dB
        wizard.renorm_value = renorm_value
        
    wizard.run_cdf()
    return wizard

def run_validate():
    validation = Validate_Reference_Data()
    validation_results = validation.run()

if __name__ == '__main__':
    with Desktop(specified_version="2021.2",new_desktop_session =False,close_on_exit =False):
        aedtapp = Hfss()

    run_pd(aedtapp)
    run_cdf(aedtapp)
    #run_validate()
