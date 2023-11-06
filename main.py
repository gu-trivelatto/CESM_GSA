"""
quickstart script

Author: Sina Hajikazemi
Date: 18.10.2023
"""

from Core.inputparse import Parser
from pathlib import Path
from Core.model import Model
import Core.visualize as Visual


techmap_dir_path = Path(".").joinpath("Data", "Techmap") # techmap directory path
ts_dir_path = Path(".").joinpath("Data", "TimeSeries") # time series directory path
# parser = Parser("DEModel",techmap_dir_path=techmap_dir_path, ts_dir_path=ts_dir_path ,scenario = "Base4twk")
parser = Parser("TestModel",techmap_dir_path=techmap_dir_path, ts_dir_path=ts_dir_path ,scenario = "Base")
print("### parsing started ###")
parser.parse()
input = parser.get_input()
print("### parsing finished ###")
print("#### building model started ###")
model = Model(input)
print("#### building model finished ###")
print("#### solving model started ###")
model.solve()

# get and sava model output in a binary file
Visual.save_output_pkl(output=model.get_output(),filename="output.pkl")

# load tha outpout from the binary file
output = Visual.read_output_pkl(filename="output.pkl")

print("#### solving model finished ###")

cs = list(model.data.dataset.conversion_subprocesses)[0]
co = list(model.data.dataset.commodities)[0]

Visual.visualize_data("Total_annual_co2_emission", model, output, cs, co)