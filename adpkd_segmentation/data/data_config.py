import os

# %%
dataroot = "data_copy/"

labeled_dirs = [
    os.path.join(dataroot, "training-data-01-60MR"),
    os.path.join(dataroot, "training_data-61-110MR_AX_SSFSE_ABD_PEL_50"),
]

unlabeled_dirs = [os.path.join(dataroot, "unlabelled_data")]
